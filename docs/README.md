# Documentation

## Cases

A **case** is a set of arguments to supply to the tested function.
To define a case, use the `case` decorator from `pycky.cases` and pass the arguments (both ordered and keyword) as you would pass them to the tested function.

For instance, if you want to test a function `f('value', 3, key=True)`, you can write:

```python
@case('value', 3, key=True)
```

## Checks and checklists

A **check** is something to assert about the evaluated function.

Pycky introduces a few standard checks in the `pycky.checks` package.
For example, in order to assert that `add(2, 2)` is equal to `4`, you can import the `equals` check from `pycky.checks` and write the following case and check:

```python
@case(2, 2)
@equals(4)
def add(...):
    ...
```

Several checks can be made on a single case.
For instance, you can use the `isGreaterThan` and `isLessThan` checks from `pycky.checks`:

```python
@case(2.0, 2.0)
@isGreaterThan(3.999)
@isLessThan(4.001)
def add(...):
    ...
```

The set of checks applied to a given case are known as that case's **checklist**.

You can read more about checks and checklists [here](checks/README.md).


## Modifiers

Cases and checks can admit generic changes through **modifiers**.

For instance, suppose that the arguments you supply to a given test are very expensive or slow to compute.
Presumably, you don't want them to be computed every time the Python file is executed, because you won't be running the tests every time you import a function from that file.
To achieve this, you can wrap the expensive parameters in a lambda with no arguments, e.g. `lambda: slow()` instead of `slow()`.
For Pycky to be aware of you doing this, though, you need to use the `defer` modifier on the check or case in question:

```python
from pycky.modifiers.defer import defer

@case(10)
@defer(equals(lambda: 1*2*3*4*5*6*7*8*9*10))
def factorial(n):
    return n*factorial(n-1) if n > 1 else 1
```

You can read more about modifiers [here](modifiers/README.md).


## Printers

Pycky's default behavior when running tests is to print to terminal the result of each test.
You might want to print in a different style, generate a report, or even use Pycky's results to trigger something else.
In order to do that, you can use **printers**.
The name can be a bit misleading, because they not only print, but actually can do almost anything you can write in Python.

You can read more about printers [here](printers/README.md).


## Command-line interface

Pycky will install a global command-line interface (CLI) binary called `pycky`.
In order to test a module, call `pycky` on your terminal followed by the modules or functions to test.

The syntax to specify a module or test is the same as the one used by [Setuptools](https://setuptools.readthedocs.io/en/latest/userguide/entry_point.html).
Modules are specified by a dot-separated Python module path, such as the ones used by the `import` statement.
A function inside a given module can be specified optionally by following the module path with a colon (`:`) and then the function name.

For example, if you want to test a file `~/path/to/file.py`, you can run, from the `~` directory:

```sh
pycky path.to.file
```

If, instead, you want to test the function `function` inside `file.py`, you can do:

```sh
pycky path.to.file:function
```

You can include multiple modules and functions, separating them by spaces.
For example, if you want to test files `file1.py` and `file2.py` in `~/path/to`, you can run:

```sh
pycky path.to.file1 path.to.file2
```

To know more about Pycky's CLI, run `pycky --help`.

<!-- ## Inner workings

TODO


### The decorator pipeline

TODO how the inspectable is passed down from decorator to decorator, and the role of checklists and modifiers in this.


### The `PYCKY` global

TODO -->
