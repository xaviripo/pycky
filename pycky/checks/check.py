from ..modifiers.deferrable import deferrable
from ..glb import PYCKY
from ..arguments import Arguments


class Checklist:
    """
    A checklist is the object that collects the checks to make against a
    certain case of the inspected function, as well as the inspected function
    itself, so it can be passed down the decorator pipeline.
    """

    def __init__(self, inspectable):
        """
        :param inspected: the function to test
        """
        self.inspectable = inspectable
        self.checklist = []

        # object of type Arguments to run the test with
        self.arguments = None

    def add_check(self, check):
        """Adds a new check to the checklist to make against a certain case.

        The check is added at the beginning of the checklist so that tests are
        run in the order they are written, given that decorators are applied
        inside-out instead of top-bottom.
        """
        self.checklist.insert(0, check)

    def __call__(self, printer):
        actual = self.arguments.apply(self.inspectable)
        for check in self.checklist:
            (printer.success if check.do(actual) else printer.failure)(
                inspected=self.inspectable,
                arguments=self.arguments,
                check=check,
                actual=actual,
            )

class Check:

    def __init__(self):
        self.description = None
        self.action = None
        self.expected = None

    def __call__(self, checklist_or_inspectable):
        if isinstance(checklist_or_inspectable, Checklist):
            checklist = checklist_or_inspectable
        else: # It's an inspectable
            checklist = Checklist(checklist_or_inspectable)
        checklist.add_check(self)
        return checklist

    def do(self, actual):
        return self.action(actual, self.expected)

    def describe(self):
        return self.description.format(self.expected)

    @staticmethod
    def checkify(description):
        def decorator(func):
            @deferrable
            def get_check(expected):
                check = Check()
                check.description = description
                check.action = func
                check.expected = expected
                return check
            return get_check
        return decorator