from colorama import init, Fore, Back, Style
init()

class Printer:
    '''Prints error and success messages.

    This class can be subclassed by the user for customization.'''

    check_mark = '\u2705'
    cross_mark = '\u274C'

    def __init__(self):
        self.success = self.check_mark + ' Expected {inspectable}({arguments}) to {check}, correctly got {actual}.'
        self.failure = self.cross_mark + ' Expected {inspectable}({arguments}) to {check}, got {actual} instead.'


class ColorfulPrinter(Printer):

    def __init__(self):
        self.success = '\u2705 ' + Fore.GREEN + 'Expected {inspectable}({arguments}) to {check}, correctly got {actual}.' + Style.RESET_ALL
        self.failure = '\u274C ' + Back.RED + 'Expected ' \
            + ColorfulPrinter._bold('{inspectable}') + '(' \
            + ColorfulPrinter._bold('{arguments}') + ') to ' \
            + ColorfulPrinter._bold('{check}') + ', got {actual} instead.' + Style.RESET_ALL

    @staticmethod
    def _bold(text):
        return Style.BRIGHT + text + Style.NORMAL