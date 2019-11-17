from .check import Check


class CheckEquals(Check):
    """Checks whether the case return value is equal to the given value."""

    def __init__(self, expected):
        self.expected = expected

    def do(self, actual):
        return actual == self.expected

    def describe(self):
        return "equal {}".format(repr(self.expected))


class CheckIsGreaterThan(Check):
    """Checks whether the case return value is greater than the given value."""

    def __init__(self, expected):
        self.expected = expected

    def do(self, actual):
       return actual > self.expected

    def describe(self):
        return "be greater than {}".format(repr(self.expected))


class CheckIsLessThan(Check):
    """Checks whether the case return value is less than the given value."""

    def __init__(self, expected):
        self.expected = expected

    def do(self, actual):
       return actual < self.expected

    def describe(self):
        return "be less than {}".format(repr(self.expected))