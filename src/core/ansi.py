"""
Archarios Framework :: The Novice's Ethical Hacking Framework
Copyright(C) 2018 :: Catayao56 <Catayao56@gmail.com>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

# Constants
CSI = '\033['
OSC = '\033]'
BEL = '\007'


def code_to_chars(code):
    """
    def code_to_chars():
        Convert code to characters.

        :param code: Code to convert into character.

        :returns str: Converted code.
    """

    return CSI + str(code) + 'm'


def set_title(title):
    """
    def set_title():
        Returns a code to set the terminal title.

        :param title: Returns a code to set terminal title to <title>.

        :returns str: Code (must be printed to take effect.)
    """

    return OSC + '2;' + title + BEL


def clear_screen(mode=2):
    """
    def clear_screen():
        Clears the screen.

        :param mode: Mode to use.

        :returns str: Code (must be printed to take effect.)
    """

    return CSI + str(mode) + 'J'


def clear_line(mode=2):
    """
    def clear_line():
        Clears a line in the terminal.

        :param mode: Mode to use.

        :returns str: Code (must be printed to take effect.)
    """

    return CSI + str(mode) + 'K'


class AnsiCodes(object):
    """
    class AnsiCodes():
        ANSI standard codes.
    """

    def __init__(self):
        """
        def __init__():
            The subclasses declare class attributes which are numbers.
            Upon instantiation we define instance attributes, which are the same
            as the class attributes but wrapped with the ANSI escape sequence
        """

        for name in dir(self):
            if not name.startswith('_'):
                value = getattr(self, name)
                setattr(self, name, code_to_chars(value))


class AnsiCursor(object):
    """
    class AnsiCursor():
        Controlling the cursor in the terminal.
    """

    def UP(self, n=1):
        """
        def UP():
            Move cursor up.
        """

        return CSI + str(n) + 'A'

    def DOWN(self, n=1):
        """
        def DOWN():
            Move cursor down.
        """

        return CSI + str(n) + 'B'

    def FORWARD(self, n=1):
        """
        def FORWARD():
            Move cursor forward or right.
        """

        return CSI + str(n) + 'C'

    def BACK(self, n=1):
        """
        def BACK():
            Move cursor back or left.
        """

        return CSI + str(n) + 'D'

    def POS(self, x=1, y=1):
        """
        def POS():
            Position the cursor in the given coordinates.
        """

        return CSI + str(y) + ';' + str(x) + 'H'
