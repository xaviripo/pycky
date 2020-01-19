import abc

class Printer(abc.ABC):
    """Prints error and success messages.

    This interface can be used by the user for customization.
    The printer not only decides the style of the message, but also the format:
    a printer can print to stdout, but it can also save the result of the tests
    to a file, or do some action as a function of the results."""


    @abc.abstractmethod
    def success(self, inspected, arguments, check, actual):
        """Action to execute upon success of a test.

        :param inspected: the function to test
        :param arguments: the arguments passed to the inspected function, as
            an Arguments instance.
        :param check: the test that succeeded
        :param actual: the actual result of the test
        """
        pass

    @abc.abstractmethod
    def failure(self, inspected, arguments, check, actual):
        """Action to execute upon failure of a test.

        :param inspected: the function to test
        :param arguments: the arguments passed to the inspected function, as
            an Arguments instance.
        :param check: the test that failed
        :param actual: the actual result of the test
        """
        pass