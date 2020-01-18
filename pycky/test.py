class Test:
    """Represents a case with the associated set of checks, plus metadata used
    in order to filter which tests to run."""

    def __init__(self, execute, inspectable):

        # The test itself. Must be runnable.
        self.execute = execute

        # The function this test tests.
        self.inspectable = inspectable

    def __call__(self):
        return self.execute()