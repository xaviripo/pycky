from .check import Check

@Check.checkify("equal {}")
def equals(actual, expected):
    return actual == expected

@Check.checkify("be grater than {}")
def isGreaterThan(actual, minimum):
    return actual > minimum

@Check.checkify("be less than {}")
def isLessThan(actual, maximum):
    return actual < maximum