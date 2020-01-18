from importlib import import_module

import click

import pycky

from pycky.printers import BasicPrinter

@click.command()
@click.argument('files', nargs=-1)
@click.option('-p', '--printer',
    default='BasicPrinter',
    help='Printer for the results of the tests.')
def main(files, printer):

    PYCKY = pycky.glb.PYCKY

    # As we will run the imported code from Pycky, we'll be testing it.
    # See /pycky/glb/__init__.py for more info.
    PYCKY.testing = True

    printers = import_module('pycky.printers')
    PYCKY.printer = getattr(printers, printer)()

    # First import each given file as a module. This will define the decorated
    # functions and thus "run" their decorators. These will load the tests into
    # the PYCKY global inside the pycky.glb package.
    for file in files:
        import_module(file)

    # Now, try to run all the tests.
    for test in pycky.glb.PYCKY.tests:
        test()
