# Pycky

## About

**Pycky** is a unit testing framework for Python.
It is focused on being:

- **Compact**. The tests are in the same files as the code, so you can easily check and change the behavior of your functions.
- **Descriptive**. Pycky tests are as easy to read as they are to write.
- **Flexible**. Choose to run some or all tests every time you run the code (just in case!), or run all the tests in a package, for a function, a case, or a check.
- **Extensible**. Easily define reusable checks, modifiers, and printers to make writing new tests a breeze.


## Installation

You can install directly from this repository:

```sh
pip install git+https://github.com/xaviripo/pycky.git
```


## Quick start

Suppose a file `example.py` with the following function:

```python
def add(a, b):
    return a + b
```

If you want to add a test to check that `add(2, 2)` equals `4`, you can change it to:

```python
from pycky import cases, checks

@cases.case(2, 2)
@checks.equals(4)
def add(a, b):
    return a + b
```

By running `pycky example` in the terminal, you get:

```
✔ example: Expected add(2, 2) to equal 4, correctly got 4.
```

The `case` decorator defines the arguments to pass to the tested function (in this case `add`), and the `equals` decorator supplies the expected output.


## Documentation

You can find the complete documentation for Pycky [here](docs/README.md).
