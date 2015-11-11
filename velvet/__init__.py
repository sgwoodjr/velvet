"""\
Beautiful signal processing and communications algorithms in Python.

The following commands are available:

  >>> from velvet import *

Communications
    biterr              - Bit error rate

Modems
    CPMMOD              - Continous phase modulation

Pulse Shapes
    rectpulse           - Rectangular pulse

Signal Processing
    conv                - Convolution
    upsample            - Upsample data

"""

from .commfunc import *
from .cpmmod import *
from .pulses import *
from .sigproc import *
from .utils import *
from .validation import *
