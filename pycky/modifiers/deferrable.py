from types import LambdaType

def deferrable(func):
    """Given a function, returns a deferred version of itself.

    This means, given func, which takes normal arguments, return a function
    that takes maybe deferred arguments and passes them resolved to func.

    See _resolve()."""

    def func_deferrable(*args, **kwargs):
        args = tuple(_resolve(arg) for arg in args)
        kwargs = {key: _resolve(value) for key, value in kwargs.items()}
        return func(*args, **kwargs)

    func.defer = func_deferrable

    return func


def _resolve(lambda_or_value):
    """Evaluates the given value if it is deferred, or returns it directly
    otherwise."""
    if isinstance(lambda_or_value, LambdaType):
        return lambda_or_value()
    else:
        return lambda_or_value