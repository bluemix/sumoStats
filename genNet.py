import sys
import random
from subprocess import call



netCfgName = "Kad100.netcfg"

retcode = call(['netconvert', '-c', netCfgName]);



