import sys
import random
from subprocess import call

tripInfoFile = "Kad100.trips.xml"
statsFile = "Kad100.stats.xml"		# statistics file results (output)

retcode = call(['python', 'networkStatistics.py',		
				'-t', tripInfoFile,
				'-o', statsFile], stdout=sys.stdout, stderr=sys.stderr)

