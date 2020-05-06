# sp20-516-255 E.Cloudmesh.Common.1

# Program that demonstrates the use of banner, HEADING, and VERBOSE.

from cloudmesh.common.util import banner
from cloudmesh.common.util import HEADING
from cloudmesh.common.debug import VERBOSE

bannerText = "Banner Test"

## banner
banner(bannerText, "*", color="BLUE")

## HEADING
headingText = "Heading Test"
HEADING(headingText)

#VERBOSE
verboseText = {"Banner": bannerText, "Heading": headingText}
VERBOSE(verboseText)