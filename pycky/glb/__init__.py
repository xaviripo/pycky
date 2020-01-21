# This class only exists so that we can append arbitrary attributes to the
# global PYCKY object (e.g. PYCKY.cases).
class Empty:
    pass

# This global variable contains metadata and tests to be run later on.
PYCKY = Empty()

# Whether we are testing or not.
PYCKY.testing = False

# Contains all the tests to be run.
PYCKY.tests = []

# List of modules passed to the Pycky script
PYCKY.modules = {}

# Object in charge of managing the output of the test runs.
PYCKY.printer = None

# Whether to run tests in the imported packages of the listed modules as well.
PYCKY.follow_imports = False