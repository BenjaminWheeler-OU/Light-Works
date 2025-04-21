#!/usr/bin/env python
import os
import sys
import traci
import sumo
from sumolib import checkBinary

#SUMO_PATH = os.path.dirname(sumo.__file__)

sumo_binary = checkBinary('sumo-gui')
traci.start([sumo_binary])