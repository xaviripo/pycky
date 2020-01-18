from importlib import import_module

import click

import pycky

@click.command()
@click.argument('files', nargs=-1)
def main(files):

    # As we will run the imported code from Pycky, we'll be testing it.
    # See /pycky/glb/__init__.py for more info.
    pycky.glb.PYCKY.testing = True

    # First import each given file as a module. This will define the decorated
    # functions and thus "run" their decorators. These will load the tests into
    # the PYCKY global inside the pycky.glb package.
    for file in files:
        import_module(file)

    # Now, try to run all the tests.
    for test in pycky.glb.PYCKY.tests:
        test()
