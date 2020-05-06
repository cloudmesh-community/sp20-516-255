# sp20-516-255 E.Cloudmesh.Common.3
# Develop a program that demonstrates the use of FlatDict.
from cloudmesh.common.Flatdict import FlatDict

data = {
'name': 'Prafull',
'address': {
            'city': 'Portland',
            'state': 'OR'
            }
        }
flat = FlatDict(data, sep=".")
print(flat)

