from .modifiers.deferrable import deferrable
from .arguments import Arguments
# Import PYCKY global
from .glb import PYCKY
from .printers import BasicPrinter


@deferrable
def case(*args, **kwargs):
    """Decorates a given checklist in order to run its checks."""
    # Only build build the arguments and such if we're testing.
    if PYCKY.testing:
        def inner(checklist):
            # Save the checklist and the arguments to run it with to the global
            checklist.arguments = Arguments(args, kwargs)
            PYCKY.tests.append(checklist)
            return checklist.inspectable
    else:
        def inner(inspectable):
            return inspectable
    return inner