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
along with this program. If not, see <http://www.gnu.org/licenses/>.
"""

objects = ['Printer']

import sys

from core import misc
from core import exceptions


class Printer:
    """
    Print an object to the screen using number of methods..
    """

    def __init__(self):
        """
        def __init__():
            Initialization method of Printer() class.
        """

        pass

    def print_with_status(self, obj, status=0):
        """
        def print():
            Print <obj> with status number <status>.

            :param obj: Object to print.
            :type object:

            :param status: Status number.
            :type int:
                0 = Normal;
                1 = Warning;
                2 = Error
        """

        if status == 0:
            print('{2}[{0}+{2}]{1}'.format(misc.CG, misc.END, misc.CGR),
                    misc.CG, obj, misc.END)
            return None

        elif status == 1:
            print('{2}[{0}!{2}]{1}'.format(misc.CY, misc.END, misc.CGR),
                    misc.CY, obj, misc.END)
            return None

        elif status == 2:
            print('{2}[{0}E{2}]{1}'.format(misc.CR, misc.END, misc.CGR),
                    misc.CR, obj, misc.END)
            return None

        else:
            raise exceptions.InvalidParameterError("Unknown status mode!")

    def print_and_flush(self, obj):
        """
        def print_and_flush():
            Print <obj> and then flush.
        """

        sys.stdout.write(obj)
        sys.stdout.flush()
        return None
