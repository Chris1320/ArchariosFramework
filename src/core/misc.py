#!/usr/bin/env python3
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

objects = ['CR', 'CG', 'CY', 'CB', 'CGR', 'CP', 'CC', 'CLM', 'CLB',
        'CLG', 'CLY', 'CLR', 'CLC', 'CLGR', 'BW', 'BR', 'BG', 'BY',
        'BB', 'BM', 'BC', 'BGR', 'BLGR', 'BLR', 'BLG', 'BLY', 'BLB',
        'BLM', 'BLC', 'BLW', 'FB', 'FI', 'FU', 'FE', 'END',
        'ProgramFunctions']

import os
import sys

import random
import datetime
import hashlib
import subprocess

from core import exceptions

if sys.platform == 'linux' or sys.platform == 'darwin':
    # Colors with meanings
    CR = '\033[31m'        # red
    CG = '\033[32m'        # green
    CY = '\033[33m'        # yellow
    CB = '\033[34m'        # blue
    CGR = '\033[90m'       # gray

    # Misc colors
    CP = '\033[35m'        # purple
    CC = '\033[36m'        # cyan

    # Extended colors
    CLM = '\033[95m'       # light magenta
    CLB = '\033[94m'       # light blue
    CLG = '\033[92m'       # light green
    CLY = '\033[93m'       # light yellow
    CLR = '\033[91m'       # light red
    CLC = '\033[96m'       # light cyan
    CLGR = '\033[37m'      # light gray

    # Background Colors without meanings :p
    BW = '\033[7m'         # white
    BR = '\033[41m'        # red
    BG = '\033[42m'        # green
    BY = '\033[43m'        # yellow
    BB = '\033[44m'        # blue
    BM = '\033[45m'        # magenta
    BC = '\033[46m'        # cyan
    BGR = '\033[100m'      # gray

    BLGR = '\033[2m'       # light gray
    BLR = '\033[101m'      # light red
    BLG = '\033[102m'      # light green
    BLY = '\033[103m'      # light yellow
    BLB = '\033[104m'      # light blue
    BLM = '\033[105m'      # light magenta
    BLC = '\033[106m'      # light cyan
    BLW = '\033[107m'      # light white?!?

    # Font types
    FB = '\033[1m'         # bold
    FI = '\033[3m'         # italic
    FU = '\033[4m'         # underline
    FE = '\033[9m'         # erased

    END = '\033[0m'        # reset to default...

else:
    # No color support on windows operating systems.
    CR = ''
    CG = ''
    CY = ''
    CB = ''
    CGR = ''

    CP = ''
    CC = ''
    CK = ''

    CLM = ''
    CLB = ''
    CLG = ''
    CLY = ''
    CLR = ''
    CLC = ''
    CLGR = ''

    BW = ''
    BR = ''
    BG = ''
    BY = ''
    BB = ''
    BM = ''
    BC = ''
    BGR = ''

    BLGR = ''
    BLR = ''
    BLG = ''
    BLY = ''
    BLB = ''
    BLM = ''
    BLC = ''
    BLW = ''

    FB = ''
    FI = ''
    FU = ''
    FE = ''

    END = ''


class ProgramFunctions:
    """
    class ProgramFunctions():
        Class of miscellaneous methods.
    """

    def __init__(self):
        """
        def __init__():
            Initialization method of misc module.
        """

        self.COPYRIGHT = "Copyright(C) 2017-{0} by Catayao56".format(
                datetime.datetime.now().year)

    def program_restart(self):
        """
        def program_restart():
            Restart program.
        """

        python = sys.executable
        os.execl(python, python, * sys.argv)

    def clrscrn(self):
        """
        def clrscrn():
            Clears the screen.
        """

        platform = self.is_windows()
        if platform is False:
            subprocess.call('clear')

        elif platform is True:
            subprocess.call('cls')

        else:
            loop = 0
            while loop != 100:
                print()
                loop += 1

    def pause(self, silent=False):
        """
        def pause():
            Wait for the user's input.
        """

        if silent is True:
            input()

        else:
            input("Press enter to continue...")

    def error_except(self):
        """
        def error_except():
            Ask the user if he wanted to continue when an exception occurs.
        """

        loop = True
        while loop is True:
            try:
                quit = None
                ask = input(CB + FB + FI + 'Do you want to keep running? (y/n)> ' + CW + FR)
                ask = ask.lower()
                if ask == 'y':
                    loop = False
                    quit = False

                elif ask == 'n':
                    loop = False
                    quit = True

                else:
                    loop = True

            except(KeyboardInterrupt, EOFError):
                continue

        return quit

    def get_platform(self):
        """
        def get_platform():
            Get the system platform.
        """

        result = sys.platform
        return result

    def cli_color_support(self):
        """
        def cli_color_support():
            Check if the system supports command-line/terminal
            color support. This is because windows systems doesn't
            support ANSI colors using codes.
        """

        PLATFORM = self.is_windows()
        if PLATFORM is False:
            return True

        elif PLATFORM is True:
            return False

        else:
            # Just to be sure that we will not mess up everything.
            return False

    def is_windows(self):
        """
        def is_windows():
            Check if system is windows.
        """
        PLATFORM = os.name
        if PLATFORM in ('nt', 'win', 'windows'):
            return True

        else:
            return False

    def generate_session_id(self):
        """
        def generate_session_id():
            Generate a session ID for the logger module.
        """

        session = random.randint(111111, 999999)
        return session

    def hash(self, string, hashtype='md5'):
        """
        def hash():
            Hashlib module wrapper.
        """

        string = string.encode()
        hashtype = hashtype.lower()
        if hashtype == 'blake2b':
            result = hashlib.blake2b(string).hexdigest()
            result = result.upper()
            return result

        elif hashtype == 'blake2s':
            result = hashlib.blake2s(string).hexdigest()
            result = result.upper()
            return result

        elif hashtype == 'sha3_224':
            result = hashlib.sha3_224(string).hexdigest()
            result = result.upper()
            return result

        elif hashtype == 'sha3_256':
            result = hashlib.sha3_256(string).hexdigest()
            result = result.upper()
            return result

        elif hashtype == 'sha3_384':
            result = hashlib.sha3_384(string).hexdigest()
            result = result.upper()
            return result

        elif hashtype == 'sha3_512':
            result = hashlib.sha3_512(string).hexdigest()
            result = result.upper()
            return result

        elif hashtype == 'shake_128':
            result = hashlib.shake_128(string).hexdigest()
            result = result.upper()
            return result

        elif hashtype == 'shake_256':
            result = hashlib.shake_256(string).hexdigest()
            result = result.upper()
            return result

        elif hashtype == 'md5':
            result = hashlib.md5(string).hexdigest()
            result = result.upper()
            return result

        elif hashtype == 'sha1':
            result = hashlib.sha1(string).hexdigest()
            result = result.upper()
            return result

        elif hashtype == 'sha224':
            result = hashlib.sha224(string).hexdigest()
            result = result.upper()
            return result

        elif hashtype == 'sha256':
            result = hashlib.sha256(string).hexdigest()
            result = result.upper()
            return result

        elif hashtype == 'sha384':
            result = hashlib.sha384(string).hexdigest()
            result = result.upper()
            return result

        elif hashtype == 'sha512':
            result = hashlib.sha512(string).hexdigest()
            result = result.upper()
            return result

        else:
            raise exceptions.UnknownHashTypeError("An unknown hash type is entered...")

    def path_exists(self, file_path):
        """
        def path_exists():
            Return True if path exists.
        """

        return os.path.exists(file_path)

    def isfile(self, file_path):
        """
        def isfile():
            Return True if path is a file.
        """

        return os.path.isfile(file_path)

    def isfolder(self, file_path):
        """
        def isfolder():
            Return True if path is a directory.
        """

        return os.path.isdir(file_path)

    def pip_install(self, package, pyver):
        """
        def pip_install():
            Install a module using PIP.
        """

        if pyver == 3:
            subprocess.Popen(args='pip3 install ' + package,
                    shell=True, universal_newlines=True)

        elif pyver == 2:
            subprocess.Popen(args='pip2 install ' + package,
                    shell=True, universal_newlines=True)

        else:
            subprocess.Popen(args='pip install ' + package,
                    shell=True, universal_newlines=True)

    def geteuid(self):
        """
        def geteuid():
            Return the current process's effective user id.
        """

        try:
            euid = os.geteuid()

        except:
            # Might be running on windows...
            euid = 0

        return euid

    def random_color(self):
        """
        def random_color():
            Return a random color.
        """

        color_list = [CR, CG, CY, CB, CGR, CP, CC, CLM, CLB, CLG, CLY,
                CLR, CLC, CLGR]
        randomizer = random.randint(0, (len(color_list) - 1))
        return color_list[randomizer]

    def captcha_picker(self, list_of_strings=[]):
        """
        def captcha_picker():
            Return random captchas.
        """

        if list_of_strings == []:
            list_of_strings = [
                    "Type this text.",
                    "Please type this text.",
                    "Don't type this text.",
                    "Type this text now!"
                    ]

        randomizer = random.randint(0, (len(list_of_strings)-1))
        return list_of_strings[randomizer]

    def get_program_filename(self, current_path):
        """
        def get_program_filename():
            Get the program's filename.
        """

        separator = os.sep
        current_path = current_path[::-1]
        filename = current_path.partition(separator)[0]
        filename = filename[::-1]
        return filename
