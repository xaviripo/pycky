# Pycky

## Introduction

Pycky is a simple unit testing framework for Python.


## Quick start

Just

```python
from pycky.cases import case
from pycky.checks import equals
```

and decorate your function like so:

```python
@case(2, 2)
@equals(4)
def add(a, b):
    a + b
```

For more in-depth examples, see [`demo.py`](https://github.com/xaviripo/pycky/blob/master/demo.py).