from ShowBaseGlobal import *
from DirectSession import *

# If specified in the user's Configrc, create the direct session
if base.wantDIRECT:
    direct = base.direct = DirectSession()
else:
    # Otherwise set the values to None
    direct = base.direct = None

