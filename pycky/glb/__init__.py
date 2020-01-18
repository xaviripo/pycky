# This class only exists so that we can append arbitrary attributes to the
# global PYCKY object (e.g. PYCKY.cases).
class Empty:
    pass

# This global variable contains metadata and tests to be run later on.
PYCKY = Empty()

# Contains all the tests to be run.
PYCKY.tests = []

# List of modules passed to the Pycky script
PYCKY.modules = []

# Whether the code is being run for testing or not.
# As of right now this is only True when running the pycky binary, but in the
# future an option from running "live" tests when executing the code itself
# might be added.
PYCKY.testing = False

# Object in charge of managing the output of the test runs.
PYCKY.printer = None

# Whether to run tests in the imported packages of the listed modules as well.
PYCKY.follow_imports = False