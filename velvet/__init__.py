"""\
Beautiful signal processing and communications algorithms in Python.

The following commands are available:

  >>> from velvet import *

Channel Models
    awgn                - Additive white Gaussian noise channel

Communications
    berawgn             - Theoretical BER for AWGN
    biterr              - Bit error rate

Math
    qfunc               - Q-function

Modems
    CPMMOD              - Continous phase modulation

Pulse Shapes
    rectpulse           - Rectangular pulse

Signal Processing
    conv                - Convolution
    upsample            - Upsample data

"""

from .channel import *
from .commfunc import *
from .cpmmod import *
from .pulses import *
from .sigproc import *
from .utils import *
from .validation import *
