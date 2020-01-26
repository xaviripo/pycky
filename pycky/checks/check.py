from ..glb import PYCKY


class Checklist:
    """
    A checklist is the object that collects the checks to make against a
    certain case of the inspected function, as well as the inspected function
    itself, so it can be passed down the decorator pipeline.
    """

    def __init__(self, inspectable=None):
        self.inspectable = inspectable
        self.checklist = []

        # object of type Arguments to run the test with
        self.arguments = None

    def add_check(self, check):
        self.checklist.insert(0, check)

    def generate_actual(self):
        self.actual = self.inspectable(*self.arguments.args, **self.arguments.kwargs)

    def execute(self, printer):
        self.generate_actual()
        for check in self.checklist:
            (printer.success if check.execute(self.actual) else printer.failure)(
                inspected=self.inspectable,
                arguments=self.arguments,
                check=check,
                actual=self.actual,
            )

    def __call__(self, other):
        self.checklist = other.checklist
        self.inspectable = other.inspectable
        # TODO here we should actually add to global PYCKY.tests or sthng
        PYCKY.tests.append(self)
        return self.inspectable


class Check:

    def __call__(self, checklist):
        if not isinstance(checklist, Checklist):
            checklist = Checklist(checklist)
        checklist.add_check(self)
        return checklist

    def generate_expected(self):
        pass

    def execute(self, actual):
        self.generate_expected()
        return self.executor(actual, self.expected)

    def describe(self):
        return self.description.format(self.expected)


def checkify(description):
    def set_executor(executor):
        def set_expected(expected):
            check = Check()
            check.description = description
            check.executor = executor
            check.expected = expected
            return check
        return set_expected
    return set_executor