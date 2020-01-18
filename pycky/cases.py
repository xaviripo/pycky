from .modifiers.deferrable import deferrable
from .arguments import Arguments
# Import PYCKY global
from .glb import PYCKY
from .test import Test
from .printers import BasicPrinter


@deferrable
def case(*args, **kwargs):
    """Decorates a given checklist in order to run its checks."""
    def inner(checklist):
        # Only save the tests if we are actually testing
        if PYCKY.testing and \
        (PYCKY.follow_imports or checklist.inspectable.__module__ in PYCKY.modules):
            arguments = Arguments(args, kwargs)
            def execute():
                actual = arguments.apply(checklist.inspectable)
                for check in checklist.checklist:
                    (PYCKY.printer.success
                    if check.do(actual)
                    else PYCKY.printer.failure)(
                        inspected=checklist.inspectable,
                        arguments=arguments,
                        check=check,
                        actual=actual,
                    )
            PYCKY.tests.append(Test(
                execute,
                checklist.inspectable
            ))
        return checklist.inspectable
    return inner