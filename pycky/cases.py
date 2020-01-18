from itertools import chain

from .modifiers.deferrable import deferrable

# Import PYCKY global
from .glb import PYCKY

from .test import Test
from .printer import ColorfulPrinter

printer = ColorfulPrinter()


@deferrable
def case(*args, **kwargs):
    """Decorates a given checklist in order to run its checks."""
    def inner(checklist):
        # Only save the tests if we are actually testing
        if PYCKY.testing:
            def execute():
                actual = checklist.inspectable(*args, **kwargs)
                for check in checklist.checklist:
                    message = printer.success if check.do(actual) else printer.failure
                    print(message.format(
                        inspectable=checklist.inspectable.__name__,
                        arguments=_repr_args_kwargs(*args, **kwargs),
                        check=check.describe(),
                        actual=repr(actual),
                    ))
            PYCKY.tests.append(Test(
                execute,
                checklist.inspectable
            ))
        return checklist.inspectable
    return inner


def _repr_args_kwargs(*args, **kwargs):
    """Returns a comma-separated string with the args and kwargs given."""
    return ", ".join(chain(
        (repr(arg) for arg in args),
        ("{}={}".format(key, repr(value)) for key, value in kwargs.items())
    ))