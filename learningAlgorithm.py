# A basic reinforcement learning algorithm that modifies a set of intersection cycle times and optimizes for minimum total waiting time
# Needs to get and set data in SUMO, will export a .xlsx file with the results, will also export the final sim to SUMO
# Author: Levin Ward

import random
import copy
import traci
import sumolib
from sumolib import checkBinary
import sys
import tests.safeMemoryAccess
import emissionsCalc
import profitEstimator
import os
import options
# these should all be set in the GUI
cycleTimeRange = (50, 120) # in seconds
defaultCycleTime = 60 # in seconds

populationSize = 10
generations = 2
survivalRate = 0.1
mutateFactor = 0.2
bestPopulation = None
sumo_binary = checkBinary('sumo-gui')
sumo_cfg = os.path.join('data/norman', 'norman.sumo.cfg')
class Population:
    # default constructor
    def __init__(self):
        self.intersections = []
        self.totalWaitingTime = float('inf')
        self.totalEmissions = float('inf')
        
        # Get all traffic lights (intersections) from SUMO
        traffic_lights = traci.trafficlight.getIDList()
        traffic_lights_access = tests.safeMemoryAccess.SafeMemoryAccess(traffic_lights)
        
        for i in range(len(traffic_lights)):
            tl_id = traffic_lights_access.safe_read(i, 40)
            # Set the cycle time to a random number in the range of cycleTimeRange
            cycleTime = random.randint(cycleTimeRange[0], cycleTimeRange[1])
            traci.trafficlight.setPhaseDuration(tl_id, cycleTime)

            # Create a new intersection with the current cycle time and position
            self.intersections.append(Intersection(cycleTime, tl_id))

class Intersection:
    cycleTime = 60 # in seconds
    myId = ""
    
    def __init__(self, cycleTime, myId):
        self.cycleTime = cycleTime
        self.myId = myId
    
    def getCycleTime(self):
        return self.cycleTime
    
    def getMyId(self):
        if self.myId == 0:
            print(f"ERROR: myId is 0.")
            
        return self.myId
    
    def setCycleTime(self, cycleTime):
        self.cycleTime = cycleTime

startingEmissions = 0
startingWaitingTime = 0

def doAlgorithm():
    global bestPopulation  # Declare bestPopulation as global
    
    populationSize = options.get('population-size')
    generations = options.get('generations')
    survivalRate = options.get('survival-rate')
    mutateFactor = options.get('mutate-factor')
    
    populations = []

    print("Starting learning algorithm")
    # initialize populations
    for i in range(populationSize):
        populations.append(Population())
        
    populations_access = tests.safeMemoryAccess.SafeMemoryAccess(populations)
    
    # initialize the best population
    bestPopulation = copy.deepcopy(populations_access.safe_read(0, 76))
    
    initialEmissions = bestPopulation.totalEmissions
    startingWaitingTime = bestPopulation.totalWaitingTime
    
    # repeat for each generation
    for g in range(generations):
        print(f"Start running sims for gen {g}")
        # run the simulation for each population
        for i in range(len(populations)):
            population = populations_access.safe_read(i, 83)
            if population is not None:
                (population.totalWaitingTime, population.totalEmissions) = runSim(population)
                print(f"\nPopulation {i} total waiting time: {population.totalWaitingTime}")
    
        # start a new generation with surviving populations and evolve
        # sort populations by lowest total waiting time
        populations.sort(key=lambda x: x.totalWaitingTime, reverse=True)
        
        # if this has the new best population, save (copy) it
        if len(populations) == 0:
            print("No populations found")
        elif populations[0].totalWaitingTime < bestPopulation.totalWaitingTime:
            bestPopulation = copy.deepcopy(populations[0])
            print(f"New best population total waiting time: {bestPopulation.totalWaitingTime}")  
            
        # print the total waiting time of the best population
        print(f"Best total waiting time in the {g}th generation: {populations[0].totalWaitingTime}, best overall: {bestPopulation.totalWaitingTime}\n")      
        
        print("Start evolution")
        # death and evolution time!
        if g != generations - 1:
            # select the top 10% of populations
            survivingPopulations = populations[int(populationSize * survivalRate):] 
            # evolve the surviving populations
            populations = evolvePopulations(survivingPopulations)
        
        print("Evolutions Complete!")
    
    # print the best population after all generations (will export to excel and SUMO later)
    print(f"\nBest population total waiting time after all generations: {bestPopulation.totalWaitingTime}")
    print(f"Average waiting time after all generations: {bestPopulation.totalWaitingTime / len(bestPopulation.intersections)}")
    
    # TODO: Send this and the best population to the excel file
    emissions_reduced = emissionsCalc.calculate_emissions(initialEmissions, bestPopulation.totalWaitingTime)
    profit_saved = profitEstimator.estimate_profit(bestPopulation.totalWaitingTime, startingWaitingTime)
    
    # Close SUMO connection
    traci.close()

def generate_routefile():
    random.seed(42)  # make tests reproducible
    N = 1000  # number of time steps
    # demand per second from different directions
    pWE = 1. / 10
    pEW = 1. / 11
    pNS = 1. / 30
    with open("data/norman/norman.rou.xml", "w") as routes:
        print("""<routes>
        <vType id="typeWE" accel="0.8" decel="4.5" sigma="0.5" length="5" minGap="2.5" maxSpeed="16.67" \
guiShape="passenger"/>
        <vType id="typeNS" accel="0.8" decel="4.5" sigma="0.5" length="7" minGap="3" maxSpeed="25" guiShape="bus"/>

        <route id="right" edges="51o 1i 2o 52i" />
        <route id="left" edges="52o 2i 1o 51i" />
        <route id="down" edges="54o 4i 3o 53i" />""", file=routes)
        vehNr = 0
        for i in range(N):
            if random.uniform(0, 1) < pWE:
                print('    <vehicle id="right_%i" type="typeWE" route="right" depart="%i" />' % (
                    vehNr, i), file=routes)
                vehNr += 1
            if random.uniform(0, 1) < pEW:
                print('    <vehicle id="left_%i" type="typeWE" route="left" depart="%i" />' % (
                    vehNr, i), file=routes)
                vehNr += 1
            if random.uniform(0, 1) < pNS:
                print('    <vehicle id="down_%i" type="typeNS" route="down" depart="%i" color="1,0,0"/>' % (
                    vehNr, i), file=routes)
                vehNr += 1
        print("</routes>", file=routes)

def setSimCycleTime(intersections):
    # set the cycle time in SUMO
    intersections_access = tests.safeMemoryAccess.SafeMemoryAccess(intersections)
    
    for i in range(len(intersections)):
        intersection = intersections_access.safe_read(i, 153)
        
        programs = traci.trafficlight.getAllProgramLogics(intersection.getMyId())

        if not programs:
            print(f"Warning: No programs found for intersection {intersection.getMyId()}")
            return

        # Pick the active program (assuming programs[0])
        program = programs[0]

        # Modify the phases
        for phase in program.phases:
            if "r" in phase.state:  # If this phase contains a red light
                phase.duration = intersection.getCycleTime()

        # Apply the modified program
        traci.trafficlight.setProgramLogic(intersection.getMyId(), program)

def runSim(population):
    # set each intersection cycle time in SUMO
    setSimCycleTime(population.intersections)
    traci.load(['-c', sumo_cfg])
    int_ids = traci.trafficlight.getIDList()
    for intersection in population.intersections:
        traci.trafficlight.setPhaseDuration(intersection.getMyId(), intersection.getCycleTime())
    
    return run()

def get_waiting_time():
    waiting_times = {}
    for vehicle_id in traci.vehicle.getIDList():
        # Get the vehicle's waiting time (time spent at traffic lights)
        waiting_time = traci.vehicle.getWaitingTime(vehicle_id)
        waiting_times[vehicle_id] = waiting_time
    return waiting_times

def evolvePopulations(survivingPopulations):
    # Evolve the surviving populations by mutating the cycle times by mutateFactor
    newPopulations = []
    
    for i, population in enumerate(survivingPopulations):
        # each surviving population will have (1 / survivalRate) new children to ensure the population stays the same size
        for p in range(int(1 / survivalRate)):
            # Create a new population with the same structure but mutated values
            newPopulation = copy.deepcopy(population)
            
            # Mutate each intersection from the original population
            intersections_access = tests.safeMemoryAccess.SafeMemoryAccess(population.intersections)
            for j in range(len(population.intersections)):
                intersection = intersections_access.safe_read(j, 198)
                if intersection is not None:
                    rand = 1.0 + random.uniform(-mutateFactor, mutateFactor)
                    mutated_cycle_time = intersection.cycleTime * rand
                    #print(f"Mutated cycle time for intersection {intersection.myId}: {mutated_cycle_time}")
                    intersection.cycleTime = mutated_cycle_time
            
            newPopulations.append(newPopulation)
    
    return newPopulations

def get_waiting_time(vehicles):
    current_waiting_time = 0
    for vehicle_id in vehicles:
        # Get the vehicle's waiting time (time spent at traffic lights)
        current_waiting_time += traci.vehicle.getWaitingTime(vehicle_id) * traci.simulation.getDeltaT()
    
    return current_waiting_time

def get_emissions(vehicles):
    current_emissions = 0
    for vehicle_id in vehicles:
        current_emissions += 250 * traci.simulation.getDeltaT() # assume each vehicle emits 250 grams of CO2 per second
    return current_emissions

def run():
    # simply run the simulation for a set amount of time at the highest possible simulation speed
    step = 0
    total_waiting_time = 0
    total_emissions = 0
    
    while step < 1000:  # Run simulation for 1000 steps
        traci.simulationStep()
        
        # Get vehicles and calculate total waiting time
        vehicles = traci.vehicle.getIDList()
        current_waiting_time = get_waiting_time(vehicles)
        total_waiting_time += current_waiting_time
        total_emissions += get_emissions(vehicles)
        
        step += 1
    
    return total_waiting_time, total_emissions
