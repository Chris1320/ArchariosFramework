#coding=utf-8

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

    def ERROR0004(self, proc_type='command', name='Archários Framework'):
        """
        def ERROR0004():
            Call this if user attempts to run a command that needs root-level
            permission/s.

            :param proc_type: Origin of the error.
            :type str: `command` or `module`

            :param name: Name of the program.
            :type str:
        """

        return """Sorry, the {0} you are trying to perform needs root \
privileges. Please try the following:
\t~ Please run {1} as root (For Linux)
\t~ Please Run {1} as Administrator (For Windows)
\t~ Make sure your smartphone is rooted and {1} has been granted superuser \
privileges by the su binary. (For Android)""".format(proc_type, name)

    def ERROR0005(self, proc_type='command'):
        """
        def ERROR0005():
            Call this if command doesn't yet support API.

            :param proc_type: Origin of the error.
            :type str: `command` or `module`
        """

        return """Sorry! This {0} does not have any API support as of now.
Please contact the developer or create a merge request that has the fix for
your problem. Thank you""".format(proc_type)

    def ERROR0006(self):
        """
        def ERROR0006():
            Call this if there is a problem with the internet connection.
        """

        return "There is a problem connecting to the internet!"

    def ERROR0007(self):
        """
        def ERROR0007():
            Call this if module's run() method doesn't return an integer.
        """

        return """Module doesn't return an integer!
If you are the developer, please put a return token at the end of all
possible exit points of the code. If not, please contact the developer."""
