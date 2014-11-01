#!/usr/bin/env python
"""
@file    runner.py
@author  Lena Kalleske
@author  Daniel Krajzewicz
@author  Michael Behrisch
@date    2009-03-26
@version $Id: runner.py 14678 2013-09-11 08:53:06Z behrisch $

Tutorial for traffic light control via the TraCI interface.

SUMO, Simulation of Urban MObility; see http://sumo.sourceforge.net/
Copyright (C) 2009-2012 DLR/TS, Germany

This file is part of SUMO.
SUMO is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 3 of the License, or
(at your option) any later version.
"""

import os, sys
import optparse
import subprocess
import random
import time
import collections
import copy
from subprocess import call
import argparse

# we need to import python modules from the $SUMO_HOME/tools directory
SUMO_HOME = "/home/bluemix/SUMO/sumo-0.19.0"

try:
    sys.path.append(os.path.join(SUMO_HOME, "tools")) 
    from sumolib import checkBinary
except ImportError:
    sys.exit("please declare environment variable 'SUMO_HOME' as the root directory of your sumo installation (it should contain folders 'bin', 'tools' and 'docs')")


import traci

mapFile = "Kad100.net.xml"
routeFile = "Kad100.rou.xml"		# the generated route file (output)
tripInfoFile = "Kad100.trips.xml"	# the generated trip file (output, to extract statistics from it)
PORT = "8833"

def run():
	traci.init(int(PORT))
	step = 0
	while traci.simulation.getMinExpectedNumber() > 0:
		traci.simulationStep()
		step += 1
	traci.close()


# this is the main entry point of this script
if __name__ == "__main__":

    sumoBinary = checkBinary('sumo')
  
    sumoProcess = subprocess.Popen([sumoBinary, 
				'-n', mapFile ,
				'-r', routeFile, 
				'--remote-port', PORT,
				'--tripinfo-output', tripInfoFile], stdout=sys.stdout, stderr=sys.stderr)
    run()
    sumoProcess.wait()
