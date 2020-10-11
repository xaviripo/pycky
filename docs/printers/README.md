# Printers

## Built-in printers

TODO list of printers


## Creating your own printers

To create a printer, just extend the `Printer` abstract base class from `pycky.printers.printer`.
This class has only two methods: `success` and `failure`.
Both methods take the same arguments:

- `inspected`: the function to test.
- `arguments`: a comma-separated list of the actual parameters passed to the tested function.
- `check`: the description of the check with the actual parameters already interpolated.
- `actual`: the value returned by the tested function.

`success` will be run for each successful check, and `failure` for each failed one.

Let's see an example.

```python
from pycky.printers.printer import Printer

class CustomPrinter(Printer):

    def success(self, inspected, arguments, check, actual):
        print("{}({}) passed the test".format(inspected.__name__, arguments))

    def failure(self, inspected, arguments, check, actual):
        print("{}({}) failed the test".format(inspected.__name__, arguments))
```

In order to use your custom printer, call Pycky with the `--printer` followed by the path to the printer class.
For instance, if you define the `CustomPrinter` class above in a `printer.py` file, in order to test a file `example.py`, you can do:

```sh
pycky --printer printer:CustomPrinter example
```

To know more about Pycky's options, run `pycky --help`.
