#!/usr/bin/env python

#Make sure to install requirements.txt with pip:
#pip install -r requirements.txt

#Virtual environments will also work:
#https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/

import os
import sys
import traci
import sumo
from sumolib import checkBinary

#Sumo expects the environment variable SUMO_PATH to be set to the directory of the Sumo installation
#If there is none, set it to the directory of the Sumo import
if not "SUMO_PATH" in os.environ:
    os.environ["SUMO_PATH"] = os.path.dirname(sumo.__file__)
SUMO_PATH = os.environ["SUMO_PATH"]

sumo_binary = checkBinary('sumo-gui')
traci.start([sumo_binary])