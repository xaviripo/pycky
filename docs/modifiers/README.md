# Modifiers

## Built-in modifiers

TODO list of modifiers


## Creating your own modifiers

A modifier is an instance of the `Modifier` class from `pycky.modifiers.modifier`.
This instance carries a `modifier` method.
To define the behavior on any check, decorate a function that takes the check and returns it modified with the `modifier(Check)` function, where `Check` is a class from `pycky.checks.check`.
Similarly, to define its behavior on any case, decorate a function that takes its checklist and returns it modified with the `modifier(Checklist)` function, where `Checklist` is also from `pycky.checks.check`.

Let's see an example.
Suppose we want a modifier `mod` that acts only on checks.
We can build it as such:

```python
from pycky.modifiers.modifier import Modifier
from pycky.checks.check import Check

mod = Modifier()

@mod.modifier(Check)
def mod_check(check):
    # Here we can modify the object `check` as we please, or do something else
    return check
```

If we want it to modify checklists, we can do it so:

```python
from pycky.checks.check import Checklist

@mod.modifier(Checklist)
def mod_check(checklist):
    # Here we can modify the object `checklist` as we please, or do something else
    return checklist
```


