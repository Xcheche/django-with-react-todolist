from .base import *

# Try to import local settings if they exist
try:
    from .local import *
except ImportError:
    pass