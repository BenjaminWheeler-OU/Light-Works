#!/usr/bin/env python
import os
import sys
import traci
import sumo

SUMO_PATH = os.path.abspath('.venv/lib/python3.13/site-packages/sumo')
os.environ['SUMO_PATH'] = SUMO_PATH

traci.start([os.path.join(SUMO_PATH, 'bin/sumo-gui')])