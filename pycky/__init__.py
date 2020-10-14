"""Unit testing framework for Python."""

# Initialize the global package so that we don't get non-defined errors when
# trying to import it from the bin/pycky script.
from pycky.glb import *

from . import cases
from . import checks
from . import modifiers
from . import printers

__all__ = [
    "cases",
    "checks",
    "modifiers",
    "printers",
]