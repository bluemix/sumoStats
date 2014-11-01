import sys
import random
from subprocess import call
import os
import errno

 
mapFile = "Kad100.net.xml"
routeFile = "Kad100.rou.xml"		# the generated route file (output)

seed = "5"
minDistance = "100"
fringeFactor = "1"
beginTime = "0"
endTime = "750"					# 1000 vehicles will be generated

SUMO_HOME = "/home/bluemix/SUMO/sumo-0.19.0"

# ----------- generate routes ----------- 
retcode = call(['python', SUMO_HOME + "/tools/trip/randomTrips.py",
				'-n', mapFile,
				'-r', routeFile, 
				'--fringe-factor', str(fringeFactor),
				'-s', str(seed),
				'--min-distance', str(minDistance),
				'-b', str(beginTime), '-e', str(endTime)]);
