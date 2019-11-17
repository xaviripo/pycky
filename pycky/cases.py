from itertools import chain

def case(*args, **kwargs):
    """Decorates a given checklist in order to run its checks."""
    def inner(checklist):
        actual = checklist.inspectable(*args, **kwargs)
        for check in checklist.checklist:
            assert check.do(actual),\
                "Expected {}({}) to {}, got {} instead.".format(
                    checklist.inspectable.__name__,
                    _repr_args_kwargs(*args, **kwargs),
                    check.describe(),
                    repr(actual),
                )
        return checklist.inspectable
    return inner

def _repr_args_kwargs(*args, **kwargs):
    """Returns a comma-separated string with the args and kwargs given."""
    return ", ".join(chain(
        (repr(arg) for arg in args),
        ("{}={}".format(key, repr(value)) for key, value in kwargs.items())
    ))