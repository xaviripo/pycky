from .basic import *

equals = CheckEquals.decorator()
isGreaterThan = CheckIsGreaterThan.decorator()
isLessThan = CheckIsLessThan.decorator()

__all__ = [
    "equals",
    "isGreaterThan",
    "isLessThan",
]