from importlib import import_module

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

    PYCKY.modules = _process_scopes(scopes)

    PYCKY.printer = getattr(pycky.printers, printer)()

    PYCKY.follow_imports = follow_imports

    _obtain_tests()

    # Now, try to run all the tests.
    for test in PYCKY.tests:
        test()

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

def _obtain_tests():
    """Imports the modules to extract the tests from in an isolated manner."""

    PYCKY = pycky.glb.PYCKY

    # As we will run the imported code from Pycky, we'll be testing it.
    # See /pycky/glb/__init__.py for more info.
    PYCKY.testing = True

    # First import each given file as a module. This will define the decorated
    # functions and thus "run" their decorators. These will load the tests into
    # the PYCKY global inside the pycky.glb package.
    for module in PYCKY.modules:
        import_module(module)

    # Disable the testing mode, so that we don't accidentally run tests on
    # other modules we might import.
    PYCKY.testing = False