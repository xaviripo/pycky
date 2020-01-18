# This class only exists so that we can append arbitrary attributes to the
# global PYCKY object (e.g. PYCKY.cases).
class Empty:
    pass

# This global variable contains metadata and tests to be run later on.
PYCKY = Empty()

# Contains all the tests to be run.
PYCKY.tests = []

# Whether the code is being run for testing or not.
# As of right now this is only True when running the pycky binary, but in the
# future an option from running "live" tests when executing the code itself
# might be added.
PYCKY.testing = False