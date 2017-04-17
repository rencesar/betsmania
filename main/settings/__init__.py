import sys
import os

from .base import *
from .dirs import *

try:
    from .custom import *
except ImportError:
    pass

if os.environ.get('INTEGRATION_TEST', False):
    from .test import *

# if DEBUG and 'test' not in sys.argv:
#     from dev import *
