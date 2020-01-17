import abc

from ..modifiers.deferrable import deferrable


class Checklist:
    """
    A checklist is the object that collects the checks to make against a
    certain case of the inspected function, as well as the inspected function
    itself, so it can be passed down the decorator pipeline.
    """

    def __init__(self, inspectable, *checklist):
        """
        :param inspected: the function to test
        :param checklist: optional list of checks to do
        """
        self.inspectable = inspectable
        self.checklist = list(checklist)

    def add_check(self, check):
        """Adds a new check to the checklist to make against a certain case.

        The check is added at the beginning of the checklist so that tests are
        run in the order they are written, given that decorators are applied
        inside-out instead of top-bottom.
        """
        self.checklist.insert(0, check)


class Check(abc.ABC):
    """A check is basically an assertion to make against a certain execution of
    the inspected function."""

    @abc.abstractmethod
    def do(self, actual):
        """Does the actual check. Should return True if the check passes, False
        otherwise."""
        pass

    @abc.abstractmethod
    def describe(self):
        """Returns a phrase describing the check.
        
        The sentence is written in infinitive (e.g. "be greater than", "equal",
        "have a length of", etc.)
        """
        pass

    @classmethod
    def decorator(cls):
        """Given a check type, makes and returns a decorator out of it."""
        @deferrable
        def decorator(*args, **kwargs):
            def inner(checklist_or_inspectable):
                if isinstance(checklist_or_inspectable, Checklist):
                    checklist = checklist_or_inspectable
                else: # It's an inspectable
                    checklist = Checklist(checklist_or_inspectable)
                checklist.add_check(cls(*args, **kwargs))
                return checklist
            return inner
        return decorator