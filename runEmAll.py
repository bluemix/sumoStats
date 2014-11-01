import sys
import random
from subprocess import call


retcode = call(['python', "genNet.py"]);		# ----------- generate SUMO network ----------- 

retcode = call(['python', "genRoutes.py"]);		# ----------- generate routes 		----------- 

retcode = call(['python', "runSUMO.py"]);		# ----------- run SUMO 				----------- 

retcode = call(['python', "genStats.py"]);		# ----------- generate stats 		----------- 






