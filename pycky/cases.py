from .arguments import Arguments
# Import PYCKY global
from .glb import PYCKY
from .checks.check import Checklist

def case(*args, **kwargs):
    # Only build the arguments and such if we're testing.
    if PYCKY.testing:
        checklist = Checklist()
        checklist.arguments = Arguments(args, kwargs)
        return checklist
    else:
        def identity(inspectable):
            return inspectable
        return identity