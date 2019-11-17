from pycky.cases import case
from pycky.checks import *


@case(2, 2)
@isGreaterThan(3)
@equals(4)
@isLessThan(5)
def addition(a, b):
    return a + b


@case(1, 2, 3)
@equals(6)

@case(*(2*x for x in range(10)))
@isGreaterThan(sum(x for x in range(10)))
@isLessThan(sum(3*x for x in range(10)))

def summation(*elems):
    return sum(elems)