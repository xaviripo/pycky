from colorama import init, Fore, Back, Style
init() # initialize colorama

from .printer import Printer


class BasicPrinter(Printer):

    def __init__(self):
        self._success = '\u2714 {module}: Expected {inspected}({arguments}) to {check}, correctly got {actual}.'
        self._failure = '\u2718 {module}: Expected {inspected}({arguments}) to {check}, got {actual} instead.'

    def success(self, inspected, arguments, check, actual):
        print(self._success.format(
            module=inspected.__module__,
            inspected=inspected.__name__,
            arguments=repr(arguments),
            check=check.describe(),
            actual=repr(actual)
        ))

    def failure(self, inspected, arguments, check, actual):
        print(self._failure.format(
            module=inspected.__module__,
            inspected=inspected.__name__,
            arguments=repr(arguments),
            check=check.describe(),
            actual=repr(actual)
        ))


class ColorfulPrinter(BasicPrinter):

    def __init__(self):

        self._success = Fore.GREEN + '\u2714 ' \
            + ColorfulPrinter._bold('{module}') + ': Expected ' \
            + ColorfulPrinter._bold('{inspected}({arguments})') + ' to ' \
            + ColorfulPrinter._bold('{check}') + ', correctly got ' \
            + ColorfulPrinter._bold('{actual}') + '.' \
            + Style.RESET_ALL

        self._failure = Back.RED + '\u2718 ' \
            + ColorfulPrinter._bold('{module}') + ': Expected ' \
            + ColorfulPrinter._bold('{inspected}({arguments})') + ' to ' \
            + ColorfulPrinter._bold('{check}') + ', got ' \
            + ColorfulPrinter._bold('{actual}') + ' instead.' \
            + Style.RESET_ALL

    @staticmethod
    def _bold(text):
        return Style.BRIGHT + text + Style.NORMAL


class ExceptionPrinter(Printer):
    """Raises an exception when a test fails, silent otherwise."""

    def success(self, inspected, arguments, check, actual):
        pass

    def failure(self, inspected, arguments, check, actual):
        raise Exception(
            'Expected {inspected}({arguments}) to {check}, got {actual} instead.'.format(
                inspected=inspected.__name__,
                arguments=repr(arguments),
                check=check.describe(),
                actual=repr(actual)
            )
        )