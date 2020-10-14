from .check import checkify


@checkify("equal {}")
def equals(actual, expected):
    return actual == expected


@checkify("be greater than {}")
def isGreaterThan(actual, minimum):
    return actual > minimum


@checkify("be less than {}")
def isLessThan(actual, maximum):
    return actual < maximum