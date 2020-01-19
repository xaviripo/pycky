from .modifiers.deferrable import deferrable
from .arguments import Arguments
# Import PYCKY global
from .glb import PYCKY
from .printers import BasicPrinter


@deferrable
def case(*args, **kwargs):
    """Decorates a given checklist in order to run its checks."""
    def inner(checklist):
        # Only save the tests if we are actually testing
        if PYCKY.testing and \
        (PYCKY.follow_imports or checklist.inspectable.__module__ in PYCKY.modules) and \
        (checklist.inspectable.__name__ in PYCKY.modules[checklist.inspectable.__module__] or \
        '*' in PYCKY.modules[checklist.inspectable.__module__]):
            checklist.arguments = Arguments(args, kwargs)
            PYCKY.tests.append(checklist)
        return checklist.inspectable
    return inner