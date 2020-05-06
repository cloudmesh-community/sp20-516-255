#  sp20-516-255 E.Cloudmesh.Common.5

#Develop a program that demonstrates the use of cloudmesh.common.Shell
from cloudmesh.common.Shell import Shell

dirResult = Shell.run('dir')
print(dirResult)