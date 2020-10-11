# Checks

## Built-in checks

TODO list of checks


## Creating your own checks

In order to create your own check, you must import the `checkify` decorator from `pycky.check`.
Then, use the `checkify` decorator on a function that defines the check's behavior.
The decorated function will become the check itself.
This function is known as the check's **executor**.

The `checkify` decorator takes a single argument, a string describing the behavior of the check.
This string can contain interpolation arguments (`{}`), which will be replaced with the actual parameters supplied to the executor at runtime.

The executor must take, at least, one argument, which is the actual result of the tested function when the case is applied to it.
Moreover, it can take any number of extra arguments, which will have to be passed when using the check on the tested function.

Let's see an example.
First, we define a check called `contains`, in order to check whether the tested function returns a list containing a given item:

```python
from pycky.check import checkify

@checkify("contain {}")
def contains(collection, item):
    return item in collection
```

Now, we can use the newly defined check, `contains`, to test a function `append`:

```python
@case([0, 1, 2], 3)
@contains(3)
def append(list, item):
    return list + [item]
```

This test will execute `append([0, 1, 2], 3)`, and assert that `contains(append([0, 1, 2], 3), 3)` is true, as defined above, i.e. `3 in append([0, 1, 2], 3)`.

The console output will be:

```
✔ example: Expected append([0, 1, 2], 3) to contain 3, correctly got [0, 1, 2, 3].
```

Observe that the "to contain 3" bit of the output is constructed from the description string `"contain {}"` passed to the `checkify` decorator when defining the check, together with the value `3` passed to the `contains` decorator when defining the test.
