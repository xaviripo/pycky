import abc

from colorama import init, Fore, Back, Style
init() # initialize colorama

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


class BasicPrinter(Printer):

    def __init__(self):
        self._success = '\u2714 Expected {inspected}({arguments}) to {check}, correctly got {actual}.'
        self._failure = '\u2718 Expected {inspected}({arguments}) to {check}, got {actual} instead.'

    def success(self, inspected, arguments, check, actual):
        print(self._success.format(
            inspected=inspected.__name__,
            arguments=repr(arguments),
            check=check.describe(),
            actual=repr(actual)
        ))

    def failure(self, inspected, arguments, check, actual):
        print(self._failure.format(
            inspected=inspected.__name__,
            arguments=repr(arguments),
            check=check.describe(),
            actual=repr(actual)
        ))


class ColorfulPrinter(BasicPrinter):

    def __init__(self):

        self._success = Fore.GREEN \
            + '\u2714 Expected ' \
            + ColorfulPrinter._bold('{inspected}({arguments})') + ' to ' \
            + ColorfulPrinter._bold('{check}') + ', correctly got ' \
            + ColorfulPrinter._bold('{actual}') + '.' \
            + Style.RESET_ALL

        self._failure = Back.RED \
            + '\u2718 Expected ' \
            + ColorfulPrinter._bold('{inspected}({arguments})') + ' to ' \
            + ColorfulPrinter._bold('{check}') + ', got ' \
            + ColorfulPrinter._bold('{actual}') + ' instead.' \
            + Style.RESET_ALL

    @staticmethod
    def _bold(text):
        return Style.BRIGHT + text + Style.NORMAL