from itertools import chain

from .modifiers.deferrable import deferrable

# Import PYCKY global
from .glb import PYCKY


@deferrable
def case(*args, **kwargs):
    """Decorates a given checklist in order to run its checks."""
    def inner(checklist):
        # Only save the tests if we are actually testing
        if PYCKY.testing:
            def test():
                actual = checklist.inspectable(*args, **kwargs)
                for check in checklist.checklist:
                    if not check.do(actual):
                        print("Expected {}({}) to {}, got {} instead.".format(
                            checklist.inspectable.__name__,
                            _repr_args_kwargs(*args, **kwargs),
                            check.describe(),
                            repr(actual),
                        ))
            PYCKY.tests.append(test)
        return checklist.inspectable
    return inner


def _repr_args_kwargs(*args, **kwargs):
    """Returns a comma-separated string with the args and kwargs given."""
    return ", ".join(chain(
        (repr(arg) for arg in args),
        ("{}={}".format(key, repr(value)) for key, value in kwargs.items())
    ))