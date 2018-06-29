#!/usr/bin/env python3
#
# Shadow Suite Framework :: Ethical Hacking Toolkit and Framework
# Copyright (C) 2017-2018  Shadow Team <Public.ShadowTeam@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

# -*- coding: utf-8 -*-

import os
import sys

import random
import datetime
import hashlib
import subprocess

########## FOR SSF ONLY ##########
from core import version
from core import logger
from core import multitasking
from core import error

if sys.platform == 'linux' or sys.platform == 'darwin':
    # Colors with meanings
    CW   = '\033[0m'       # white           (normal)
    CR   = '\033[31m'      # red             (errors)
    CG   = '\033[32m'      # green           (main color)
    CY   = '\033[33m'      # yellow          (warnings)
    CB   = '\033[34m'      # blue            (highlights)
    CGR  = '\033[90m'      # gray            (questions)

    # Misc colors
    CP   = '\033[35m'      # purple
    CC   = '\033[36m'      # cyan
    CK   = ''              #'\003[8m'       # black DEV0001: NYW

    # Extended colors
    CLM  = '\033[95m'      # light magenta
    CLB  = '\033[94m'      # light blue
    CLG  = '\033[92m'      # light green
    CLY  = '\033[93m'      # light yellow
    CLR  = '\033[91m'      # light red
    CLC  = '\033[96m'      # light cyan
    CLGR = '\033[37m'      # light gray

    # Background Colors without meanings :p
    BW   = '\033[7m'       # white
    BR   = '\033[41m'      # red
    BG   = '\033[42m'      # green
    BY   = '\033[43m'      # yellow
    BB   = '\033[44m'      # blue
    BM   = '\033[45m'      # magenta
    BC   = '\033[46m'      # cyan
    BGR  = '\033[100m'     # gray

    BLGR = '\033[2m'       # light gray
    BLR  = '\033[101m'     # light red
    BLG  = '\033[102m'     # light green
    BLY  = '\033[103m'     # light yellow
    BLB  = '\033[104m'     # light blue
    BLM  = '\033[105m'     # light magenta
    BLC  = '\033[106m'     # light cyan
    BLW  = '\033[107m'     # light white?!?

    # Font types
    FR   = '\033[0m'       # regular
    FB   = '\033[1m'       # bold
    FI   = '\033[3m'       # italic
    FU   = '\033[4m'       # underline
    FE   = '\033[9m'       # erased

    END  = '\033[0m'       # I know... CW, FR and this are the same... I didn't realize it earlier...

else:
    # No color support on windows operating systems.
    CW = ''
    CR = ''
    CG = ''
    CY = ''
    CB = ''
    CGR = ''

    CP = ''
    CC = ''
    CK   = ''

    CLM  = ''
    CLB = ''
    CLG  = ''
    CLY = ''
    CLR = ''
    CLC  = ''
    CLGR = ''

    BW   = ''
    BR   = ''
    BG   = ''
    BY   = ''
    BB   = ''
    BM   = ''
    BC   = ''
    BGR  = ''

    BLGR = ''
    BLR  = ''
    BLG  = ''
    BLY  = ''
    BLB  = ''
    BLM  = ''
    BLC  = ''
    BLW  = ''

    FR = ''
    FB = ''
    FI = ''
    FU = ''
    FE = ''

    END = ''

########## FOR SSF ONLY ##########
# Shadow Suite's logo and a brief description.
LOGO = r"""
 ____  _               _                 ____        _ _
/ ___|| |__   __ _  __| | _____      __ / ___| _   _(_) |_ ___
\___ \| '_ \ / _` |/ _` |/ _ \ \ /\ / / \___ \| | | | | __/ _ \
 ___) | | | | (_| | (_| | (_) \ V  V /   ___) | |_| | | ||  __/
|____/|_| |_|\__,_|\__,_|\___/ \_/\_/   |____/ \__,_|_|\__\___|
                      Framework

           Ethical Hacking Toolkit + Framework
""" + "\n\t    v" + version.BOTH + "\n\n             Copyright(C) 2017-{} by Shadow Team".format(datetime.datetime.now().year)

########## FOR SSF ONLY ##########
# brief description of the license.
BRIEF_LICENSE = r"""
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it
under certain conditions; type 'show license' for details."""

########## FOR SSF ONLY ##########
# ShadowSuite is running as module.
MODULE_MODE_INFO = CY + "Running as module..." + CW

class programFunctions(object):

    def __init__(self):
        self.COPYRIGHT = "Copyright(C) 2017-{} by Shadow Team".format(datetime.datetime.now().year)

    def program_restart(self):
        ########## TRY BLOCK FOR SSF ONLY ##########
        try:
            open('.last_session_exit_fail.log', 'r').read() # Try to read the file
            open('.last_session_exit_fail.log', 'r').close() # Close the file
            IS_WINDOWS = self.is_windows()
            if IS_WINDOWS == False:
                os.system('rm .last_session_exit_fail.log') # Delete the file

            else:
                os.system("del .last_session_exit_fail.log") # Delete the file

        except:
            pass # If file doesn't exist, do nothing, just restart.

        python = sys.executable
        os.execl(python, python, * sys.argv)
        curdir = os.getcwd()

    def clrscrn(self):
        try:
            platform = self.is_windows()
            if platform == False:
                os.system('clear')

            elif platform == True:
                os.system('cls')

            else:
                os.system('clear')
                # DEV0001: Thinking of new generic clrscrn... Try also using ansi module.
                """
                loop = 0
                while loop != 100:
                    print()
                    loop += 1
                """

        except KeyboardInterrupt:
            print(error.errorCodes().ERROR0002)
            logger.log(2, "SystemExit raised with error code 2.", 'logfile.txt')
            sys.exit(2)

    def pause(self, silent=False,  phrase="Press enter to continue..."):
        try:
            """
            platform = sys.platform
            if platform == 'linux':
                if silent is False:
                    print('Press any key to continue...')
                    os.system('read A972681B318C92911A4020C18ACF78B6')

                else:
                    os.system('read A972681B318C92911A4020C18ACF78B6')

            elif platform == 'windows':
                if silent is False:
                    os.system('pause')

                else:
                    os.sysem('pause > nul')

            else:
                if silent is False:
                    print('Press any key to continue...')
                    os.system('read A972681B318C92911A4020C18ACF78B6')

                else:
                    os.system('read A972681B318C92911A4020C18ACF78B6')
            """

            if silent == True:
                input()

            else:
                input(phrase)

        except(KeyboardInterrupt, EOFError):
            print(error.errorCodes().ERROR0002)
            logger.log(2, "SystemExit raised with error code 2.", 'logfile.txt')
            sys.exit(2)

    def error_except(self):
        try:
            loop = True
            while loop == True:
                quit = None
                ########## LABEL FOR SSF ONLY ##########
                ask = input(CB + FB + FI + 'Do you want to keep Shadow Suite running? (y/n)> ' + CW + FR)
                ask = ask.lower()
                if ask == 'y':
                    loop = False
                    quit = False

                elif ask == 'n':
                    loop = False
                    quit = True

                else:
                    loop = True

            return quit

        except KeyboardInterrupt:
            print(error.errorCodes().ERROR0002)
            logger.log(2, "SystemExit raised with error code 2.", 'logfile.txt')
            sys.exit(2)

    def get_platform(self):
        result = sys.platform
        return result

    def cli_color_support(self):
        PLATFORM = self.is_windows()
        if PLATFORM == False:
            return True

        elif PLATFORM == True:
            return False

        else:
            # Just to be sure that we will not mess up everything.
            return False

    def is_windows(self):
        PLATFORM = self.get_platform()
        if PLATFORM == 'windows':
            return True

        else:
            return False

    def generate_session_id(self):
        session = random.randint(111111, 999999)
        return session

    def hash(self, string, hashtype='md5'):
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
            raise UnknownHashTypeError("An unknown hash type is entered...")

    ########## FOR SSF ONLY ##########
    def login_user(self, global_variables, ulogin, plogin):
        ulogin = programFunctions().hash(ulogin, 'sha256')
        plogin = programFunctions().hash(plogin, 'sha256')
        if global_variables['USERNAME'] == ulogin and global_variables['USERPASS'] == plogin:
            return "Login Successful!" # means success

        else:
            return error.errorCodes().ERROR0013 # means fail

    ########## FOR SSF ONLY ##########
    def login_root(self, global_variables, ulogin, plogin):
        ulogin = programFunctions().hash(ulogin, 'sha256')
        plogin = programFunctions().hash(plogin, 'sha256')
        if global_variables['ROOTNAME'] == ulogin and global_variables['ROOTPASS'] == plogin:
            return "Login Successful!" # means success

        else:
            return error.errorCodes().ERROR0013 # means fail

    def path_exists(self, file_path):
        return os.path.exists(file_path)

    def isfile(self, file_path):
        return os.path.isfile(file_path)

    def isfolder(self, file_path):
        return os.path.isdir(file_path)

    def pip_install(self, package):
        subprocess.Popen(args='pip install ' + package, shell=True, universal_newlines=True)
        subprocess.Popen(args='pip2 install ' + package, shell=True, universal_newlines=True)

    ########## FOR SSF ONLY ##########
    def export_conf(self, config_file, config_dict):
        logger.log(3, config_dict['username'] + " is exporting settings to " + config_file + ".")
        try:
            open(config_file, 'r').read()
            open(config_file, 'r').close()
            os.remove(config_file)
            raise FileNotFoundError

        except FileNotFoundError:
            open(config_file, 'w').write('')
            open(config_file, 'w').close()

        try:
            config_new_data = """\
# This is the default configuration file for Shadow Suite.
# Every line that starts with '#' is a comment.

username="{0}"
userpass="{1}"
rootname="{2}"
rootpass="{3}"

module_path="{4}"
output_path="{5}"
binary_path="{6}"

notes_maxlines={7}"""

            config_new_data = config_new_data.format(config_dict['username'], config_dict['userpass'], config_dict['rootname'], config_dict['rootpass'], config_dict['module_path'], config_dict['output_path'], config_dict['binary_path'], config_dict['notes_maxlines'])
            with open(config_file, 'a') as fopen:
                fopen.write(config_new_data)

            return True # means success

        except:
            return False # means failed

    def geteuid(self):
        try:
            euid = os.geteuid()

        except:
            # Might be running on windows...
            euid = 0

        return euid

    def random_color(self):
        color_list = [CW, CR, CG, CY, CB, CGR, CP, CC, CK, CLM, CLB, CLG, CLY, CLR, CLC, CLGR]
        randomizer = random.randint(0, 15)
        return color_list[randomizer]

    def captcha_picker(self, list_of_strings):
        randomizer = random.randint(0, (len(list_of_strings)-1))
        return list_of_strings[randomizer]
