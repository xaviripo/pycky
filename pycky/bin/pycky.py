from importlib import import_module, reload

import click

import pycky

@click.command()
@click.argument('scopes', nargs=-1)
@click.option('-p', '--printer',
    default='basic',
    show_default=True,
    help='Printer used to output the results of the tests.')
@click.option('-f', '--follow-imports',
    default=False,
    show_default=True,
    is_flag=True,
    help='Whether to also run tests of imported files.')
def main(scopes, printer, follow_imports):
    """Runs the tests on the given SCOPES.

    SCOPES is a space-separated list of elements with one of the following
    formats:

    MODULE

    MODULE:INSPECTABLE

    MODULE is a dot-separated location of a Python module, without the .py
    extension, following the same format as an import statement. When just
    MODULE is given, all the tests found in the module will be run.

    INSPECTABLE is the name of a function with associated tests in MODULE.
    When an inspectable is given, only its tests are run."""

    PYCKY = pycky.glb.PYCKY

    PYCKY.testing = True

    PYCKY.modules = _process_scopes(scopes)

    PYCKY.printer = _process_printer(printer)

    PYCKY.follow_imports = follow_imports

    _obtain_tests()

    # Now, try to run all the tests.
    for checklist in PYCKY.tests:
        module_name = checklist.inspectable.__module__
        inspected_name = checklist.inspectable.__name__

        # Should this module be tested?
        test_this_module = PYCKY.follow_imports or module_name in PYCKY.modules

        # Should this inspectable be tested?
        test_this_inspectable = '*' in PYCKY.modules[module_name] or \
            inspected_name in PYCKY.modules[module_name]

        if test_this_module and test_this_inspectable:
            checklist.execute(PYCKY.printer)

def _process_scopes(scopes):
    """Given a list of scopes, returns a dictionary associating to each scope
    a list of inspectables or a wildcard element '*'."""

    modules = {}

    for scope in scopes:

        if ':' in scope: # This is an inspectable or list thereof
            module, inspectable = scope.split(':')
        else:
            module = scope
            inspectable = '*'

        if module not in modules:
            modules[module] = set()
        modules[module].add(inspectable)

    return modules

def _process_printer(printer):
    """Given the passed string, obtain a printer instance"""

    if ':' in printer:
        module_name, printer_class = printer.split(':')
        module = import_module(module_name)
    else:
        module = pycky.printers
        printer_class = printer

    return getattr(module, printer_class)()


def _obtain_tests():
    """Imports the modules to extract the tests from in an isolated manner."""

    PYCKY = pycky.glb.PYCKY

    # First import each given file as a module. This will define the decorated
    # functions and thus "run" their decorators. These will load the tests into
    # the PYCKY global inside the pycky.glb package.
    for module in PYCKY.modules:
        import_module(module)