#  sp20-516-255 E.Cloudmesh.Common.5

## Develop a program that demonstartes the use of StopWatch
from cloudmesh.common.StopWatch import StopWatch
import time

StopWatch.start("Test_Start")
time.sleep(10)
StopWatch.stop("Test_Start")
print (StopWatch.get('Test_Start'))
