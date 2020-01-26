from types import LambdaType, MethodType

from ..checks.check import Check, Checklist
from .modifier import Modifier


defer = Modifier()


@defer.modifier(Check)
def defer_check(check):
    def generate_expected(self):
        self.expected = self.expected()
    check.generate_expected = MethodType(generate_expected, check)
    return check


@defer.modifier(Checklist)
def defer_checklist(checklist):
    def generate_actual(self):
        self.actual = _defer_function(self.inspectable)(
            *self.arguments.args, **self.arguments.kwargs
        )
    checklist.generate_actual = MethodType(generate_actual, checklist)
    return checklist


def _defer_function(func):
    """Given a function, returns a deferred version of itself.

    This means, given func, which takes normal arguments, return a function
    that takes maybe deferred arguments and passes them resolved to func.

    See _resolve()."""

    def func_deferrable(*args, **kwargs):
        args = tuple(_resolve(arg) for arg in args)
        kwargs = {key: _resolve(value) for key, value in kwargs.items()}
        return func(*args, **kwargs)

    return func_deferrable


def _resolve(lambda_or_value):
    """Evaluates the given value if it is deferred, or returns it directly
    otherwise."""
    if isinstance(lambda_or_value, LambdaType):
        return lambda_or_value()
    else:
        return lambda_or_value