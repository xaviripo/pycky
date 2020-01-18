from itertools import chain

class Arguments():
    """Contains both args and kwargs that can be used in a function call."""

    def __init__(self, args, kwargs):
        self.args = args
        self.kwargs = kwargs

    def __repr__(self):
        """Returns a comma-separated string with the args and kwargs given."""
        return ", ".join(chain(
            (repr(arg) for arg in self.args),
            ("{}={}".format(key, repr(value)) for key, value in self.kwargs.items())
        ))

    def apply(self, func):
        """Applies the arguments to the given function"""
        return func(*self.args, **self.kwargs)