#!/usr/bin/env python

#Refer to README.MD for project setup and resources

import os
import sys
import traci
import sumo
from sumolib import checkBinary

if __name__ == "__main__":
    if not "SUMO_PATH" in os.environ:
        os.environ["SUMO_PATH"] = os.path.dirname(sumo.__file__)
    SUMO_PATH = os.environ["SUMO_PATH"]
    
    sumo_binary = checkBinary('sumo-gui')
    sumo_cfg = os.path.join('normanFiles', 'norman.sumo.cfg')
    traci.start([sumo_binary, '-c', sumo_cfg])