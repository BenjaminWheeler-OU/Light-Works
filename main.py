#!/usr/bin/env python

#Refer to README.MD for project setup and resources

import os
import sys
import traci
import sumo
from sumolib import checkBinary
import learningAlgorithm

useGUI = True

if __name__ == "__main__":
    try:
        if not "SUMO_PATH" in os.environ:
            os.environ["SUMO_PATH"] = os.path.dirname(sumo.__file__)
        SUMO_PATH = os.environ["SUMO_PATH"]
        
        sumo_binary = checkBinary('sumo-gui' if useGUI else 'sumo')
        sumo_cfg = os.path.join('normanFiles', 'norman.sumo.cfg')
        traci.start([sumo_binary, '-c', sumo_cfg])
        
        # run the learning algorithm
        learningAlgorithm.doAlgorithm()
    except Exception as e:
        if "Connection closed by SUMO" in str(e):
            print("SUMO simulation completed successfully")
        else:
            ("An unexpected error occurred:", str(e))
        sys.exit(0)  # Use exit code 0 to indicate normal termination