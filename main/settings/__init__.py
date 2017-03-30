import sys

from .base import *
from .dirs import *

try:
    from .custom import *
except ImportError:
    pass

# if DEBUG and 'test' not in sys.argv:
#     from dev import *