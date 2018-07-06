#!/usr/bin/env python

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

# Import directives
try:
    # Import system libraries.
    import os
    import sys
    import traceback

    # Import core libraries
    from core import ansi
    from core import misc
    from core import tests
    from core import cowsay
    from core import logger
    from core import matrix
    from core import gethost
    from core import asciigraphs
    from core import touchingsky
    from core import random_quotes
    from core import html_downloader

except ImportError:
    # Prints if error is encountered while importing modules.
    print("Import Error!")
    print()
    print("==================== TRACEBACK ====================")
    traceback.print_exc()
    print("===================================================")
    sys.exit(1)


class ArchariosFramework:
    """
    class ArchariosFramework():
        The main class containing main methods.
    """

    def __init__(self):
        """
        def __init__():
            Initialization method for ArchariosFramework() class.
        """

        # Program Information
        self.name = "Archarios Framework"
        self.version = "0.0.0.1"
        self.description = "The Novice's Ethical Hacking Framework"

        # Environment Information
        self.filename = misc.ProgramFunctions().get_program_filename(sys.argv[0])

        # Network Information
        self.hostname = gethost.current()

    def help(self, rtype='default'):
        """
        def help():
            Help method of ArchariosFramework() class.

            :param rtype: Return help menu in <rtype> format.
            :type str: `default`, `list`

            :returns: <type>
            :rtype: `str`, `list`
        """

        help_lines = [
                "",
                "{0} v{1} :: {2}".format(self.name, self.version,
                    self.description),
                "",
                "USAGE: {0} [SWITCHES]".format(self.filename)
                ]

        if rtype.lower() == "default":
            result = ""
            for line in help_lines:
                result += line

            return result


# If running independently, run main() function.
if __name__ == '__main__':
    af = ArchariosFramework()
    _iterator = 1  # Skip the filename.
    while _iterator < len(sys.argv):
        arg = sys.argv[_iterator]
        if arg.lower() in ('-h', '--help', '-?', '/h', '/help', '/?'):
            print(af.help())
            sys.exit(0)

        elif arg.lower() in ('-t', '--test'):
            tests.TestingClass().main()

        else:
            print('Unknown argument `{0}`'.format(arg))
            print()
            print(af.help())
            sys.exit(1)

        _iterator += 1
