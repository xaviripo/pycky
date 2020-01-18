from importlib import import_module

import click

import pycky

from pycky.printers import BasicPrinter

@click.command()
@click.argument('modules', nargs=-1)
@click.option('-p', '--printer',
    default='BasicPrinter',
    show_default=True,
    help='Printer used to output the results of the tests.')
@click.option('-f', '--follow-imports',
    default=False,
    show_default=True,
    is_flag=True,
    help='Whether to also run tests of imported files.')
def main(modules, printer, follow_imports):

    PYCKY = pycky.glb.PYCKY

    # As we will run the imported code from Pycky, we'll be testing it.
    # See /pycky/glb/__init__.py for more info.
    PYCKY.testing = True

    PYCKY.modules = modules

    printers = import_module('pycky.printers')
    PYCKY.printer = getattr(printers, printer)()

    PYCKY.follow_imports = follow_imports

    # First import each given file as a module. This will define the decorated
    # functions and thus "run" their decorators. These will load the tests into
    # the PYCKY global inside the pycky.glb package.
    for module in modules:
        import_module(module)

    # Now, try to run all the tests.
    for test in PYCKY.tests:
        test()
