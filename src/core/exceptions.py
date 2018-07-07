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

objects = ['InvalidParameterError', 'UnknownHashTypeError',
        'UnknownUserLevelError', 'InvalidCommandError']

class InvalidParameterError(Exception):
    """
    class InvalidParameterError():
        An exception class.
    """

    pass

class UnknownHashTypeError(Exception):
    """
    class UnknownHashTypeError():
        An exception class.
    """

    pass

class UnknownUserLevelError(Exception):
    """
    class UnknownUserLevelError():
        An exception class.
    """

    pass

class InvalidCommandError(Exception):
    """
    class InvalidCommandError():
        An exception class.
    """

    pass

class NameTooLongError(Exception):
    """
    class NameTooLong():
        An exception class.
    """

    pass
