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

objects = ['ErrorClass']

import importlib

class ErrorClass:
    """
    class ErrorClass():
        Class containing error methods.

        This class provides a more friendly way to tell the
        user that something wrong happened than the exceptions
        module.
    """

    def __init__(self, show_traceback=False):
        """
        def __init__():
            Initialization method of ErrorClass() class.
        """

        self.show_traceback = show_traceback
        self.misc = importlib.import_module('core.misc')

    def ERROR0001(self, config_path):
        """
        def ERROR0001():
            Call this if <config_path> was not found.
        """

        return "Configuration file `{0}` wasn't found!".format(config_path)

    def ERROR0002(self):
        """
        def ERROR0002():
            Call this if CTRL+C is entered.
        """

        return "Keyboard Interrupt (CTRL+C | ^C) Detected."

    def ERROR0003(self, command):
        """
        def ERROR0003():
            Call this if <command> is an unknown or invalid input.
        """

        misc = self.misc

        return "{0}Unknown or invalid input recieved{2}: {3}{0}{1}{2}".format(
                misc.CR, command, misc.END, misc.FB
                )
