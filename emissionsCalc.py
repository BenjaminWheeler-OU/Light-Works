import sumo
from sumolib import checkBinary
import os
import traci

def get_waiting_time():
    waiting_times = {}
    for vehicle_id in traci.vehicle.getIDList():
        # Get the vehicle's waiting time (time spent at traffic lights)
        waiting_time = traci.vehicle.getWaitingTime(vehicle_id)
        waiting_times[vehicle_id] = waiting_time
    return waiting_times

# returns the difference between the starting and ending emissions (in grams)
def calculate_emissions(startingEmissions, endingEmissions):
    return endingEmissions - startingEmissions

if __name__ == "__main__":
    if not "SUMO_PATH" in os.environ:
        os.environ["SUMO_PATH"] = os.path.dirname(sumo.__file__)
    SUMO_PATH = os.environ["SUMO_PATH"]
    
    sumo_binary = checkBinary('sumo-gui')
    sumo_cfg = os.path.join('data/norman', 'norman.sumo.cfg')
    traci.start([sumo_binary, '-c', sumo_cfg])
    
    step = 0
    total_simulation_emissions = 0
    
    while step < 1000:  # Run simulation for 1000 steps
        traci.simulationStep()
        
        # Get vehicles and calculate emissions
        vehicles = traci.vehicle.getIDList()
        current_emissions = calculate_emissions(vehicles)
        total_simulation_emissions += current_emissions
        
        step += 1
    
    print(f"\nTotal CO2 emissions for entire simulation: {total_simulation_emissions:.2f} grams")
    traci.close()
