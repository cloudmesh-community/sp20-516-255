# sp20-516-255 E.Cloudmesh.Common.1

# Program that demonstrates the use of banner, HEADING, and VERBOSE.

from cloudmesh.common.Flatdict import FlatDict

data = {
'name': 'Gregor'
'address':{
'city': 'Raleigh',
'state': 'NC'
}
}
flat = FlatDict(data, sep=".")