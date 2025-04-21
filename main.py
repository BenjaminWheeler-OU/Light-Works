#!/usr/bin/env python
import os
import sys
import traci
import sumo

SUMO_PATH = os.path.dirname(sumo.__file__)

sumo_bin = os.path.join(SUMO_PATH, 'bin/sumo-gui')

if os.path.exists(sumo_bin):
    traci.start([sumo_bin])
elif os.path.exists(sumo_bin+".exe"):
    traci.start([sumo_bin+".exe"])
else:
    print(f"Could not find sumo binary at: {sumo_bin}", file=sys.stderr)
    exit(1)