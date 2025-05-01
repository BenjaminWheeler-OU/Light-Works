#!/usr/bin/env python

#Refer to README.MD for project setup and resources

import os
import sys
import traci
import sumo
import options
from sumolib import checkBinary
import learningAlgorithm
import export

useGUI = options.runGUI()

if __name__ == "__main__":
    try:
        if not 'SUMO_HOME' in os.environ:
            os.environ['SUMO_HOME'] = os.path.dirname(sumo.__file__)
        SUMO_HOME = os.environ['SUMO_HOME']
        sumo_binary = checkBinary('sumo-gui' if useGUI else 'sumo')
        sumo_cfg = os.path.join('data/norman', 'norman.sumo.cfg')
        traci.start([sumo_binary, '-c', sumo_cfg])
        
        # run the learning algorithm    
        learningAlgorithm.doAlgorithm()
    except Exception as e:
        if "Connection closed by SUMO" in str(e):
            print("SUMO simulation completed successfully")
        else:
            print("An unexpected error occurred:", str(e))
            sys.exit(1)
        export.exportData()
        sys.exit(0)  # Use exit code 0 to indicate normal termination