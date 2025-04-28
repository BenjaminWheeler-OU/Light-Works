# A basic reinforcement learning algorithm that modifies a set of intersection cycle times and optimizes for minimum total waiting time
# Needs to get and set data in SUMO, will export a .xlsx file with the results, will also export the final sim to SUMO
# Author: Levin Ward

import random
import copy
import traci
import sumolib
from sumolib import checkBinary
import sys

# these should all be set in the GUI
cycleTimeRange = (50, 120) # in seconds
defaultCycleTime = 60 # in seconds

populationSize = 10
generations = 10
survivalRate = 0.1
mutateFactor = 0.2
bestPopulation = None

class Population:
    # default constructor
    def __init__(self):
        self.intersections = []
        self.totalWaitingTime = 999999999999 # big ass number
        
        # Get all traffic lights (intersections) from SUMO
        traffic_lights = traci.trafficlight.getIDList()
        
        for tl_id in traffic_lights:
            # Get the current cycle time
            current_cycle_time = traci.trafficlight.getPhaseDuration(tl_id)
            # Create a new intersection with the current cycle time and position
            self.intersections.append(Intersection(current_cycle_time, tl_id))

class Intersection:
    cycleTime = 60 # in seconds
    myId = ""
    
    def __init__(self, cycleTime, myId):
        self.cycleTime = cycleTime
        self.myId = myId
    
    def getCycleTime(self):
        return self.cycleTime
    
    def getMyId(self):
        return self.myId
    
    def setCycleTime(self, cycleTime):
        self.cycleTime = cycleTime

def main():
    # Initialize SUMO
    sumo_binary = checkBinary('sumo')
    traci.start([sumo_binary, "-c", "example/data/cross.sumocfg"])
    
    populations = []
    
    print("Starting learning algorithm")
    # initialze populations
    for i in range(populationSize):
        populations.append(Population())
    
    # initialize the best population
    bestPopulation = copy.deepcopy(populations[0])
    
    # repeat for each generation
    for g in range(generations):
        print(f"Start running sims for gen {g}")
        # run the simulation for each population
        for population in populations:
            population.totalWaitingTime = runSim(population)
    
        # start a new generation with surviving populations and evolve
        # sort populations by lowest total waiting time
        populations.sort(key=lambda x: x.totalWaitingTime, reverse=True)
        
        # if this has the new best population, save (copy) it
        if populations[0].totalWaitingTime < bestPopulation.totalWaitingTime:
            bestPopulation = copy.deepcopy(populations[0])
            print(f"New best population total waiting time: {bestPopulation.totalWaitingTime}")  
            
        # print the total waiting time of the best population
        print(f"Best total waiting time in the {g}th generation: {populations[0].totalWaitingTime}, best overall: {bestPopulation.totalWaitingTime}\n")      
        
        print("Start evolution")
        # death and evolution time!
        if g != generations - 1:
            # select the top 10% of populations
            survivingPopulations = populations[:int(populationSize * survivalRate)]
            # evolve the surviving populations
            populations = evolvePopulations(survivingPopulations)
        
        print("Evolutions Complete!")
    
    # print the best population after all generations (will export to excel and SUMO later)
    print(f"Best population total waiting time after all generations: {bestPopulation.totalWaitingTime}")
    print(f"Average total waiting time after all generations: {bestPopulation.totalWaitingTime / len(bestPopulation.intersections)}")
    
    # Close SUMO connection
    traci.close()

def generate_routefile():
    random.seed(42)  # make tests reproducible
    N = 3600  # number of time steps
    # demand per second from different directions
    pWE = 1. / 10
    pEW = 1. / 11
    pNS = 1. / 30
    with open("example/data/cross.rou.xml", "w") as routes:
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
    
    for i in range(len(intersections)):
        print(f"Setting cycle time for intersection {intersections[i].getMyId()} to {intersections[i].getCycleTime()} seconds")
        traci.trafficlight.setPhaseDuration(intersections[i].myId, intersections[i].getCycleTime())

def runSim(population):
    # set each intersection cycle time in SUMO
    setSimCycleTime(population.intersections)
    
    run()
    return getTotalWaitingTime()  # Return the waiting time instead of just printing

def getTotalWaitingTime():
    # Read the tripinfo output file to get total waiting time
    total_waiting = 0
    try:
        import xml.etree.ElementTree as ET
        tree = ET.parse('example/tripinfo.xml')
        root = tree.getroot()
        
        for trip in root.findall('tripinfo'):
            waiting_time = float(trip.get('waitingTime', 0))
            total_waiting += waiting_time
            
    except Exception as e:
        print(f"Error reading tripinfo file: {e}")
        return 999999999999  # Return a large number if we can't read the file
    
    print(f"Total waiting time: {total_waiting}")
    return total_waiting

def evolvePopulations(survivingPopulations):
    # Evolve the surviving populations by mutating the cycle times by mutateFactor
    newPopulations = []
    for population in survivingPopulations:
        # each surviving population will have (1 / survivalRate) new children to ensure the population stays the same size
        for p in range(int(1 / survivalRate)):
            # Create a new population with the same structure but mutated values
            newPopulation = copy.deepcopy(population)
            
            # Mutate each intersection from the original population
            for intersection in population.intersections:
                rand = 1.0 + random.uniform(-mutateFactor, mutateFactor)
                mutated_cycle_time = intersection.cycleTime * rand
                print(f"Mutated cycle time for intersection {intersection.myId}: {mutated_cycle_time}")
                intersection.cycleTime = mutated_cycle_time
                
            newPopulations.append(newPopulation)
    
    return newPopulations

def run():
    """execute the TraCI control loop"""
    step = 0
    # we start with phase 2 where EW has green
    traci.trafficlight.setPhase("0", 2)
    while traci.simulation.getMinExpectedNumber() > 0:
        traci.simulationStep()
        if traci.trafficlight.getPhase("0") == 2:
            # we are not already switching
            if traci.inductionloop.getLastStepVehicleNumber("0") > 0:
                # there is a vehicle from the north, switch
                traci.trafficlight.setPhase("0", 3)
            else:
                # otherwise try to keep green for EW
                traci.trafficlight.setPhase("0", 2)
        step += 1
    # Don't close traci here, let the main function handle it

if __name__ == "__main__":
    main()
    
