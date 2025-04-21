# A basic reinforcement learning algorithm that modifies a set of intersection cycle times and optimizes for minimum total waiting time
# Needs to get and set data in SUMO, will export a .xlsx file with the results, will also export the final sim to SUMO
# Author: Levin Ward

import random
import copy

# these should all be set in the GUI
cycleTimeRange = (50, 120) # in seconds
defaultCycleTime = 60 # in seconds

populationSize = 10
generations = 10
survivalRate = 0.1
mutateFactor = 0.1
bestPopulation = None

class Population:
    # default constructor
    def __init__(self):
        self.intersections = []
        self.totalWaitingTime = 999999999999
        for i in range(10):
            # start with random cycle times, coordinates are random for now, will get them from SUMO later
            self.intersections.append(Intersection(defaultCycleTime, (random.uniform(0, i), random.uniform(0, i)))) 

class Intersection:
    cycleTime = 60 # in seconds
    coordinates = (0, 0)
    
    def __init__(self, cycleTime, coordinates):
        self.cycleTime = cycleTime
        self.coordinates = coordinates
    
    def getCycleTime(self):
        return self.cycleTime
    
    def getCoordinates(self):
        return self.coordinates
    
    def setCycleTime(self, cycleTime):
        self.cycleTime = cycleTime

def main():
    populations = []
    
    print("Starting learning algorithm")
    # initialze populations
    for i in range(populationSize):
        populations.append(Population())
    
    # initialize the best population
    bestPopulation = copy.deepcopy(populations[0])
    
    # repeat for each generation
    for g in range(generations):
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
        
        # death and evolution time!
        if g != generations - 1:
            # select the top 10% of populations
            survivingPopulations = populations[:int(populationSize * survivalRate)]
            # evolve the surviving populations
            populations = evolvePopulations(survivingPopulations)
    
    # print the best population after all generations (will export to excel and SUMO later)
    print(f"Best population total waiting time after all generations: {bestPopulation.totalWaitingTime}")
        
def setSimCycleTime(intersections, cycleTime):
    pass
    # TODO: set the cycle time in SUMO
    #print("Setting cycle time in SUMO")
    #for i in range(len(intersections)):
        #print(f"Setting cycle time for intersection {intersections[i].getCoordinates()} to {cycleTime} seconds")

def runSim(population):
    # TODO: set each intersection cycle time in SUMO
    setSimCycleTime(population.intersections, defaultCycleTime)
    # TODO: run the simulation
    #print("Running simulation")
    return getTotalWaitingTime()  # Return the waiting time instead of just printing

def getTotalWaitingTime():
    # TODO: get the total waiting time from SUMO
    #print("Getting total waiting time")
    return random.uniform(0, 100)
    
def evolvePopulations(survivingPopulations):
    # Evolve the surviving populations by mutating the cycle times by mutateFactor
    newPopulations = []
    for population in survivingPopulations:
        # each surviving population will have (1 / survivalRate) new children to ensure the population stays the same size
        for i in range(int(1 / survivalRate)):
            newPopulation = Population()
            for intersection in population.intersections:
                newPopulation.intersections.append(Intersection(intersection.cycleTime * (1 + (random.uniform(-mutateFactor, mutateFactor))), intersection.coordinates))
            newPopulations.append(newPopulation)
    
    return newPopulations

if __name__ == "__main__":
    main()