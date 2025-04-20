#!/usr/bin/env python
import os
import sys
import traci
import sumo

SUMO_PATH = os.path.dirname(sumo.__file__)
#os.environ['SUMO_PATH'] = SUMO_PATH
print(SUMO_PATH)

traci.start([os.path.join(SUMO_PATH, 'bin/sumo-gui')])