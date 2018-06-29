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

# Import Python and Core modules to run properly
try:
    if __name__ == '__main__':
        print()
        print("[i] Importing System modules...")

    import os # General Purpose
    import sys # General Purpose
    import traceback # Debugging and Traceback information
    from getpass import getpass # Input Hiding
    import hashlib # Hashing
    import time # Time API
    import subprocess # Subprocessing API
    import importlib # Framework Module importing API
    import signal # Signal API
    import random # As the name implies, its for randomization.
    import atexit # Define multiple exit functions upon normal program termination.
    import readline # Allows us to reuse recent commands.

    if __name__ == '__main__':
        print("[i] Importing Core modules...")

    from core import ansi # Like misc, but focused on UI.
    from core import error # Error Code Definitions
    from core import exceptions # Exceptions Definitions
    from core import misc # Miscellaneous Functions/Variables/Classes
    from core import multitasking # Multitasking API
    from core import update # Updating API
    from core import version # Versioning Information
    from core import suggest # Suggestion Search Engine
    from core import logger # Logging API
    from core import gethost # A little module for hostnames and IP Addresses.
    from core import asciigraphs # A little module for graphs.
    from core import joke # Corny Jokes
    from core import quote # Quotes
    from core import list_module # Module Listing API
    from core import list_services # Service Listing API
    from core import tests # For testing SSF

    if __name__ == '__main__':
        print("[i] Importing API module...")

    import API # Framework API

    if __name__ == '__main__':
        print()
        print("[i] Finished Importing modules...\n")
        if '-t' not in sys.argv and '--test' not in sys.argv:
            misc.programFunctions().pause(False)

        else:
            print("[i] Now testing SSF...")
            time.sleep(5)

except ImportError:
    # This function is called if a module was missing.
    cr = '\033[31m'
    cw = '\033[0m'
    print(cr + "ERROR 0008: A module is missing!\nPlease re-install/re-download Shadow Suite Framework to continue... Please make sure that required modules are installed and running properly!" + cw)
    print("==================== TRACEBACK ====================")
    try:
        traceback.print_exc()

    except:
        print()
        print("(CANNOT PRINT TRACEBACK INFORMATION)")
        print()

    print("===================================================")
    proper_exit(8)

global global_variables # To be used by all functions defined here...
global recent_exceptions
global active_services

def main():
    # Check python version first before main() function execution.
    req_py_version = (3, 6, 0) # Required python version integer, in a tuple.
    cur_py_version = sys.version_info # Get user python version.
    str_py_version = str(sys.version_info) # Converting tuple to string explicitly, and a bad practice.
    str_py_version = str_py_version.replace('sys.version_info(', '') # Removing unnecessary characters.
    str_py_version = str_py_version.replace(')', '')
    logger.log(3, 'User has python version ' + str_py_version +'.', 'logfile.txt')
    req_py_version_str = "v"
    for ver_nums in req_py_version: # Creating string that contains the python version.
        req_py_version_str = req_py_version_str + str(ver_nums) + '.'

    if cur_py_version < req_py_version: # Check if user's python version is lower than the required version of python.
        PythonVersionError_msg = error.errorCodes().ERROR0011(req_py_version_str) # Gets and Formats the error string.
        print(PythonVersionError_msg)
        logger.log(0, PythonVersionError_msg, 'logfile.txt')
        proper_exit(11) # Proper exit

    else:
        pass

    if misc.programFunctions().is_windows():
        pass

    else:
        # Set the title of the current terminal.
        print(ansi.set_title("Shadow Suite Framework v" + version.VNUMBER))
        logger.log(0, "Title set for current terminal...", 'logfile.txt')

    # Generate a new session ID.
    SESSION_ID = misc.programFunctions().generate_session_id()
    logger.log(3, "Generated Session ID: " + str(SESSION_ID))

    # Placeholders for the global_variables dictionary.
    current_user = "user"
    USERNAME = None
    USERPASS = None
    ROOTNAME = None
    ROOTPASS = None

    MODULE_PATH = "modules/"
    SERVICES_PATH = "services/"
    OUTPUT_PATH = "output/"
    BINARY_PATH = "/usr/bin/"

    USERLEVEL = 2

    # Check for arguments, if any.
    NO_WARN = False
    DEBUGGING = False
    argv = sys.argv
    sys.argv = sys.argv
    for args in sys.argv:
        arg = args.lower()

        try:
            if '-d' == arg or '--debug' == arg:
                DEBUGGING = True # Enables debugging mode when '-d' or '--debug' switch is present.

            if '-h' == arg or '--help' == arg: # Show this help menu and properly exit.
                misc.programFunctions().clrscrn()
                print(sys.argv[0] + "\t--\t" + version.BOTH)
                print()
                print("Basic Usage:")
                print(sys.argv[0] + " [-h/--help] || [SWITCHES]")
                print()
                print("-h           --help         Show this help menu.")
                print()
                print("Troubleshooting Switches:")
                print("-t           --test             Test itself to know if something is wrong.")
                print("-d           --debug            Run Shadow Suite in debug mode; Shows logging information.")
                print(misc.FE + \
                      "-f           --failsafe         Run Shadow Suite in failsafe mode" + \
                      misc.END)
                print()
                print("Compatibility Switches:")
                print("-w           --no-warn          Disable last session exit fail warning.")
                print(misc.FE + \
                      "-n           --no-color         Disable fancy colors. Automatically applied on Windows Systems." + \
                      misc.END)
                print()
                print("Customization Switches:")
                print("-c [FILE]    --config=[FILE]    Define a custom configuration file.")
                print()
                proper_exit(0)

            if '-w' == arg or '--no-warn' == arg:
                NO_WARN = True # Disable 'last session exit fail' warning message.

            if '-t' == arg or '--test' == arg:
                tests.main()
                proper_exit(0)

        except IndexError:
            pass # IndexError may be raised when no arguments are passed. So except block is here.

    # Parse configuration file
    logger.log(3, 'Parsing configuration file...', 'logfile.txt', SESSION_ID)
    config_file = "data/config.dat" # The default configuration file.
    try:
        iterator_config = 0
        # Iterates through the arguments passed. I think there's a more clean way to
        # achive the same result, but i don't know it yet. Sorry, reader :(
        while iterator_config < len(sys.argv):
            if '-c' in sys.argv[iterator_config]:
                iterator_config += 1
                config_file = sys.argv[iterator_config]
                config_file = "data/" + config_file
                if os.path.exists(config_file):
                    del iterator_config
                    break

                else:
                    print(error.errorCodes().ERROR0012) # If custom configuration file is invalid.
                    proper_exit(12) # But still, don't forget to exit properly.

            else:
                iterator_config += 1

    except IndexError:
        config_file = "data/config.dat"
        del iterator_config

    try:
        iterator_config = 0
        # Just like above, but with a slight modification. I figured this code block
        # within an hour, so trust me-- seriously, trust me --I'M A N00B.
        while iterator_config < len(sys.argv):
            if '--config=' in sys.argv[iterator_config]:
                config_filf = sys.argv[iterator_config]
                config_filf = config_filf.split("=")
                config_file = config_filf[1]
                config_file = "data/" + config_file
                if os.path.exists(config_file):
                    del iterator_config
                    break

                else:
                    print(error.errorCodes().ERROR0012)
                    proper_exit(12)

            else:
                iterator_config += 1

    except IndexError:
        config_file = "data/config.dat"
        del iterator_config

    # Reading the configuration file...
    logger.log(3, 'Using ' + config_file + " configuration file; Now reading data...", 'logfile.txt', SESSION_ID)
    try:
        config_data = open(config_file, 'r').readlines()
        open(config_file, 'r').close()
        # print(config_data) # DEV0005: For debugging purposes only#####
        new_config_data = []
        for data in config_data:
            if data.startswith("#"):
                continue

            elif "username=" in data.lower():
                USERNAME = data.replace('username=', '')
                USERNAME = USERNAME.replace('"', '')
                USERNAME = no_escape_chars(USERNAME)

            elif "userpass=" in data.lower():
                USERPASS = data.replace('userpass=', '')
                USERPASS = USERPASS.replace('"', '')
                USERPASS = no_escape_chars(USERPASS)

            elif "rootname=" in data.lower():
                ROOTNAME = data.replace('rootname=', '')
                ROOTNAME = ROOTNAME.replace('"', '')
                ROOTNAME = no_escape_chars(ROOTNAME)

            elif "rootpass=" in data.lower():
                ROOTPASS = data.replace('rootpass=', '')
                ROOTPASS = ROOTPASS.replace('"', '')
                ROOTPASS = no_escape_chars(ROOTPASS)

            elif "module_path=" in data.lower():
                MODULE_PATH = data.replace('module_path="', '')
                MODULE_PATH = MODULE_PATH.replace('"', '')
                MODULE_PATH = no_escape_chars(MODULE_PATH)

            elif "services_path=" in data.lower():
                SERVICES_PATH = data.replace('services_path=', '')
                SERVICES_PATH = SERVICES_PATH.replace('"', '')
                SERVICES_PATH = no_escape_chars(SERVICES_PATH)

            elif "output_path=" in data.lower():
                OUTPUT_PATH = data.replace('output_path=', '')
                OUTPUT_PATH = OUTPUT_PATH.replace('"', '')
                OUTPUT_PATH = no_escape_chars(OUTPUT_PATH)

            elif "binary_path=" in data.lower():
                BINARY_PATH = data.replace('binary_path=', '')
                BINARY_PATH = BINARY_PATH.replace('"', '')
                BINARY_PATH = no_escape_chars(BINARY_PATH)

            elif "notes_maxlines=" in data.lower():
                NOTES_MAXLINES = data.replace('notes_maxlines=', '')
                NOTES_MAXLINES = no_escape_chars(NOTES_MAXLINES)
                try:
                    NOTES_MAXLINES = int(NOTES_MAXLINES)

                except Exception as exc_err:
                    print(error.errorCodes().ERROR0020(exc_err))
                    proper_exit(20)

            else:
                continue

        # DEV0005: For debugging purposes only
        """
        print(config_data)
        print(USERNAME)
        print(USERPASS)
        print(ROOTNAME)
        print(ROOTPASS)
        print(MODULE_PATH)
        print(SERVICES_PATH)
        print(OUTPUT_PATH)
        print(BINARY_PATH)
        misc.programFunctions().pause()
        """
        logger.log(3, "Someone is trying to use Shadow Suite...", 'logfile.txt', SESSION_ID)
        if USERNAME == None or USERNAME == "":
            pass

        else:
            if USERPASS == None or USERPASS == "":
                pass

            else:
                attempts = 0
                while True:
                    try:
                        misc.programFunctions().clrscrn()
                        print()
                        print(misc.CG + misc.FB + misc.LOGO + misc.CW + misc.FR)
                        print()
                        print(misc.CC + misc.FB + "Failed Attempts: " + misc.CR + str(attempts) + misc.CW + misc.FR)
                        print()
                        print(misc.FB + "[i]" + misc.FR + "Please login to continue...\n")
                        login_user = input("Username: ")
                        current_user = login_user
                        ploginuser = login_user
                        login_user = misc.programFunctions().hash(login_user, 'sha256')
                        login_pass = getpass()
                        login_pass = misc.programFunctions().hash(login_pass, 'sha256')
                        #print(login_user) # DEV0005
                        #print(login_pass) # DEV0005
                        #print() # DEV0005
                        #print(USERNAME) # DEV0005
                        #print(USERPASS) # DEV0005
                        if login_user == USERNAME and login_pass == USERPASS:
                            print(misc.FB + "[i]" + misc.FR + " You are now logged in!")
                            logger.log(3, ploginuser + " logged in successfully on " + time.asctime() + " with " + str(attempts) + " failed attempts.", 'logfile.txt', SESSION_ID)
                            misc.programFunctions().pause()
                            break

                        else:
                            print(error.errorCodes().ERROR0013)
                            logger.log(4, ploginuser + " failed to log in on " + time.asctime() + " with " + str(attempts) + " failed attempts.", 'logfile.txt', SESSION_ID)
                            misc.programFunctions().pause()
                            if attempts < 3:
                                attempts += 1
                                continue

                            else:
                                print(error.errorCodes().ERROR0014 + " Now quitting...")
                                proper_exit(13)

                    except(KeyboardInterrupt, EOFError):
                        print(error.errorCodes().ERROR0002)
                        proper_exit(2)

    except IndexError:
        print(error.errorCodes().ERROR0012)
        proper_exit(12)

    except FileNotFoundError:
        print(error.errorCodes().ERROR0015 + " (default configuration file)")
        proper_exit(15)

    # Checks if last session failed to exit properly
    if NO_WARN == False:
        try:
            open('.last_session_exit_fail.log', 'r').read() # Try to read the file
            open('.last_session_exit_fail.log', 'r').close() # Close the file
            print(error.warningCodes().WARNING0004)
            instance_warn = str(input(misc.CY + misc.FB + misc.FI + "Do you still want to run anyway? (y/n) > " + misc.FR + misc.CW))
            instance_warn = instance_warn.lower()
            if instance_warn == 'y':
                misc.programFunctions().clrscrn()

            else:
                proper_exit(0)

        except FileNotFoundError:
            open('.last_session_exit_fail.log', 'w').write('')
            open('.last_session_exit_fail.log', 'w').close() # Close the file
            misc.programFunctions().clrscrn()

    else:
        misc.programFunctions().clrscrn()

    logger.log(0, "Creating global_variables dictionary...", 'logfile.txt', SESSION_ID)
    # More variables and constants
    PLATFORM = misc.programFunctions().get_platform() # Get PLATFORM
    #print(MODULE_PATH) # DEV0005: For debugging purposes only
    INSTALLED_MODULES = list_module.count(MODULE_PATH) # Count installed modules.
    #print(INSTALLED_MODULES) # DEV0005: For debugging purposes only
    global global_variables
    global_variables = {
            'config_file': config_file, # String; PATH to config file.

            'USERNAME': USERNAME, # String; Hashed form of global_variables['current_user'].
            'USERPASS': USERPASS, # String.
            'ROOTNAME': ROOTNAME, # String.
            'ROOTPASS': ROOTPASS, # String.

            'MODULE_PATH': MODULE_PATH, # String; PATH to modules directory.
            'SERVICES_PATH': SERVICES_PATH, # String; PATH to services directory.
            'OUTPUT_PATH': OUTPUT_PATH, # String; PATH to output directory.
            'BINARY_PATH': BINARY_PATH, # String; PATH to system binaries.

            'NOTES_MAXLINES': NOTES_MAXLINES, # Int; Max lines of notes to show.

            'USERLEVEL': USERLEVEL, # INT; 0 for system-level root, 1 for application-level root, and 2 for normal user.
            'INSTALLED_MODULES': INSTALLED_MODULES, # List; Number of modules installed and their status.

            'current_user': current_user, # String; Plaintext form of global_variables['USERNAME'].

            'PLATFORM': PLATFORM, # String.
            'SESSION_ID': SESSION_ID, # Int (6 digits).

            'DEBUGGING': DEBUGGING # Boolean.
            }

    logger.log(0, "Deleting unnecessary variables...", 'logfile.txt', global_variables['SESSION_ID'])

    del config_file

    del USERNAME
    del USERPASS
    del ROOTNAME
    del ROOTPASS

    del MODULE_PATH
    del SERVICES_PATH
    del OUTPUT_PATH
    del BINARY_PATH

    del NOTES_MAXLINES

    del USERLEVEL
    del current_user
    del SESSION_ID
    del DEBUGGING

    del PLATFORM
    del INSTALLED_MODULES

    logger.log(0, "Checking if SSF is already used...", 'logfile.txt', global_variables['SESSION_ID'])
    if global_variables['config_file'] == 'data/config.dat':
        try:
           open('data/.installed.dat', 'r').read()
           open('data/.installed.dat', 'r').close()
           logger.log(0, "SSF already used... Skipping First-run wizard.", 'logfile.txt', global_variables['SESSION_ID'])

        except(FileNotFoundError):
            logger.log(0, "Running First-run wizard...", 'logfile.txt', global_variables['SESSION_ID'])
            if misc.programFunctions().is_windows():
                pass

            else:
                print(ansi.set_title("Shadow Suite Framework: First-Run Wizard"))

            first_run_wizard()

    else:
        logger.log(0, 'User is using a custom config, so there\'s no need for running First-run Wizard.', 'logfile.txt', global_variables['SESSION_ID'])

    Terminal()

def Terminal():
    global global_variables
    global recent_exceptions
    global active_services
    recent_exceptions = ""
    active_services = []
    multitasking.set_max_threads(multitasking.config["CPU_CORES"] * 4)

    logger.log(0, "Reading history file...", 'logfile.txt', global_variables['SESSION_ID'])
    history_file = os.path.expanduser("data/.SSFhistory")
    history_length = 100
    if not os.path.exists(history_file):
        with open(history_file, "a") as history:
            if is_libedit():
                history.write("_HiStOrY_V2_\n\n")

        readline.read_history_file(history_file) # DEV0001: Not reading the history file.
        readline.set_history_length(history_length)
        atexit.register(readline.write_history_file, history_file)

        readline.parse_and_bind("set enable-keypad on")

        readline.set_completer(complete)
        readline.set_completer_delims(" \t\n;")
        if is_libedit():
            readline.parse_and_bind("bind ^I rl_complete")
        else:
            readline.parse_and_bind("tab: complete")

    logger.log(0, "Starting Shadow Suite Framework Shell...", 'logfile.txt', global_variables['SESSION_ID'])
    print()
    print(misc.FB + misc.CG + misc.LOGO + misc.CW + misc.FR) # Prints logo
    print()
    print(misc.FI + misc.CGR + misc.BRIEF_LICENSE + misc.CW + misc.FR) # Prints a brief information about the license.
    print()
    print(misc.CW + "Modules:\t[T] " + str(global_variables['INSTALLED_MODULES'][0]) + misc.CG + " [S] " + str(global_variables['INSTALLED_MODULES'][1]) + misc.CY + " [E] " + str(global_variables['INSTALLED_MODULES'][2]) + misc.CR + " [U] " + str(global_variables['INSTALLED_MODULES'][3]) + misc.CGR + " [NYI] " + str(global_variables['INSTALLED_MODULES'][4]) + misc.CP + " [UNK] " + str(global_variables['INSTALLED_MODULES'][5]) + misc.CR + misc.FB + "  [ERR] " + str(global_variables['INSTALLED_MODULES'][6]) + misc.FR + misc.CW)
    print()
    print(misc.FB + misc.programFunctions().random_color() + quote.quote() + misc.CW + misc.FR) # Print a random quote or tip.
    print()
    # Informs the user on what global_variables['PLATFORM'] Shadow Suite is running.
    print(misc.FB + "[i]" + misc.FR + " Running on " + misc.CC + misc.FB + global_variables['PLATFORM'] + misc.CW + misc.FR + " platform.")
    print(misc.FB + "[i]" + misc.FR + " If you need help, type 'help'...")
    print('\n')
    if __name__ != '__main__':
        # If the program is not running independently, then a message will be shown, while
        # still allowing the user to use it.
        logger.log(3, 'Shadow Suite running as module...', 'logfile.txt', global_variables['SESSION_ID'])
        print(misc.FB + "[i] " + misc.FR + misc.MODULE_MODE_INFO)

    if global_variables['DEBUGGING'] == True:
        # If the program has been executed with an argument -d or --debug, show this info
        print(misc.FB + "[i]" + misc.FR + " Debugging mode is on")
        logger.log(3, 'Debugging mode is on', 'logfile.txt', global_variables['SESSION_ID'])

    # This while loop enables the user to enter commands inside shadow suite without
    # needing to run the program everytime a command is entered.
    logger.log(0, "Terminal started...", 'logfile.txt', global_variables['SESSION_ID'])
    while True:
        try:
            # If geteuid is equal to 0, then a terminal with # will be shown.
            # Otherwise, $ will be shown.

            try:
                if misc.programFunctions().geteuid() != 0:
                    logger.log(0, 'Running as normal user.', 'logfile.txt', global_variables['SESSION_ID'])
                    menu_input = input(misc.CW + "[" + misc.CB + global_variables['current_user'] + misc.CW + "@" + misc.CB + misc.FB + misc.FI + "SSF.py" + misc.FR + misc.CW + "] $: ")

                else:
                    logger.log(0, 'Running as root.', 'logfile.txt', global_variables['SESSION_ID'])
                    menu_input = input(misc.CW + "[" + misc.CB + global_variables['current_user'] + misc.CW + "@" + misc.CB + misc.FB + misc.FI + "SSF.py" + misc.FR + misc.CW + "] #: ")

            except(KeyboardInterrupt, EOFError):
                #print(len(active_services)) # DEV0005: For debugging purposes only
                if len(active_services) != 0:
                    print(error.warningCodes().WARNING0006)
                    logger.log(1, 'CTRL+C Detected, Stopping active services...', 'logfile.txt', global_variables['SESSION_ID'])
                    kill_all_active_services()

                else:
                    logger.log(1, 'CTRL+C Detected, Stopping SSF...', 'logfile.txt', global_variables['SESSION_ID'])
                    print(error.errorCodes().ERROR0002)
                    proper_exit(2)

                continue

            #print(menu_input) # DEV0005

            if ' && ' in menu_input:
                menu_input = menu_input.split(' && ')
                #print(menu_input) # DEV0005
                iterator = 0
                for inputs in menu_input:
                    #print(inputs) # DEV0005
                    iterator += 1
                    if str(iterator).endswith('1'):
                        print(misc.FB + misc.BGR + "[i] " + str(iterator) + "st command: " + inputs + misc.END)

                    elif str(iterator).endswith('2'):
                        print(misc.FB + misc.BGR + "[i] " + str(iterator) + "nd command: " + inputs + misc.END)

                    elif str(iterator).endswith('3'):
                        print(misc.FB + misc.BGR + "[i] " + str(iterator) + "rd command: " + inputs + misc.END)

                    else:
                        print(misc.FB + misc.BGR + "[i] " + str(iterator) + "th command: " + inputs + misc.END)

                    parse_arguments(inputs)

            else:
                parse_arguments(menu_input)

        except Exception as unknown_exception:
            recent_exceptions = traceback.format_exc()
            print(misc.CR + "[i] " + error.errorCodes().ERROR0020("Exception: " + str(unknown_exception)))

def parse_arguments(menu_input="help", API_global_variables={}):
    """
    API_global_variables :: (Dictionary) Needs if SSF is called from API.
    menu_input :: (String) command to pass to SSF Terminal.
    """

    global recent_exceptions
    global global_variables
    global active_services

    if API_global_variables:
        global_variables = API_global_variables

    #print(global_variables) # DEV0005

    if menu_input:
        try:
            if menu_input.lower().startswith("help"):
                logger.log(0, 'User needs help.', 'logfile.txt', global_variables['SESSION_ID'])
                print(misc.CC + misc.FB + misc.FI + "\nHELP\n" + misc.FR)
                print(misc.CW)
                print("help                          :: prints this help menu.")
                print("show [OPTION]                 :: Shows the license/info/changelog.")
                print("update [OPTION]               :: update program/dependencies/all.")
                print("config [OPTION]               :: Configure Shadow Suite settings; Export settings.")
                print("module [OPTION]               :: manage modules.")
                print("services [OPTION]             :: manage services.")
                print("suggest=[CRITERIA1,CRITERIA2] :: suggests a tool based on your critera.")
                print("notepad [OPTION]              :: built-in 'notepad'.")
                print("clear                         :: clears the screen.")
                print("run || exec [COMMAND]         :: run a command from your terminal.")
                print()
                print("netifaces                     :: ipconfig/ifconfig command.")
                print("trace [IP/HOSTNAME]           :: tracert/tracepath command.")
                print("\n")
                print("restart || reboot             :: restart Shadow Suite.")
                print("quit || exit                  :: quit Shadow Suite.")
                print()

            elif menu_input.lower().startswith("show"):
                show_o = menu_input.split(" ")
                try:
                    if show_o[1].lower() in ["license", "copying", "copyright"]:
                        logger.log(0, 'User opens license via less command...', 'logfile.txt', global_variables['SESSION_ID'])
                        if global_variables['PLATFORM'] == 'windows' or global_variables['PLATFORM'] == 'nt':
                            os.system("start extras/shadowsuitelicense")

                        else:
                            os.system("less extras/shadowsuitelicense")

                    elif show_o[1].lower() in ["info", "information", "status", "stats"]:
                        logger.log(0, 'Users looks at the info.', 'logfile.txt', global_variables['SESSION_ID'])
                        random_color1 = misc.programFunctions().random_color()
                        random_color2 = misc.programFunctions().random_color()
                        print()
                        print(misc.CC + misc.FB + "===DEBUGGING INFORMATION===" + misc.FR + misc.CW)
                        print()
                        if global_variables['DEBUGGING'] == True:
                            print(misc.CG + "Debugging: ON" + misc.CW)

                        else:
                            print(misc.CR + "Debugging: OFF" + misc.CW)

                        print()
                        print(misc.CC + misc.FB + "=== Current User Information ===" + misc.FR + misc.CW)
                        print()
                        print(misc.CY + "Current User: " + global_variables['current_user'] + misc.CW)
                        print(random_color1 + "Session ID: " + str(global_variables['SESSION_ID']) + misc.CW)
                        print()
                        print(misc.CC + misc.FB + "=== Modules Information ===" + misc.FR + misc.CW)
                        print()
                        print(misc.CW + "Total Installed Modules: " + str(global_variables['INSTALLED_MODULES'][0]) + misc.CW)
                        print(misc.CG + "Stable Modules:          " + str(global_variables['INSTALLED_MODULES'][1]) + misc.CW)
                        print(misc.CY + "Experimental Modules:    " + str(global_variables['INSTALLED_MODULES'][2]) + misc.CW)
                        print(misc.CR + "Unstable Modules:        " + str(global_variables['INSTALLED_MODULES'][3]) + misc.CW)
                        print(misc.CGR + "Not yet working:         " + str(global_variables['INSTALLED_MODULES'][4]) + misc.CW)
                        print(misc.CP + "Unknown Status:          " + str(global_variables['INSTALLED_MODULES'][5]) + misc.CW)
                        print(misc.CR + misc.FB + "Modules with Error/s:    " + str(global_variables['INSTALLED_MODULES'][6]) + misc.CW + misc.FR)
                        print()
                        print(misc.CC + misc.FB + "=== Configuration Information ===" + misc.FR + misc.CW)
                        print()
                        print(misc.CG + "Module Path: " + global_variables['MODULE_PATH'])
                        print(misc.CY + "Output Path: " + global_variables['OUTPUT_PATH'])
                        print(misc.CR + "Binary Path: " + global_variables['BINARY_PATH'])
                        print()
                        print(misc.CC + misc.FB + "=== Version Information ===" + misc.FR + misc.CW)
                        print()
                        print(misc.CG + "Version Number:   " + version.VNUMBER + misc.CW)
                        print(misc.CB + "Version Type:     " + version.VTYPE + misc.CW)
                        print(misc.CR + "Version Codename: " + version.VCODENAME + misc.CW)
                        print()
                        print(random_color2 + misc.FI + "[i] Type \'update\' for updating information." + misc.FR + misc.CW)
                        print()

                    elif show_o[1].lower() in ("system_info", "system_stats", "system_status", "sys_info", "sys_stats", "sys_status"):
                        logger.log(0, "User looks at the system info.", 'logfile.txt', global_variables['SESSION_ID'])
                        if misc.programFunctions().is_windows():
                            print()
                            os.system("systeminfo")
                            print()

                        else:
                            print()
                            os.system("bash core/neofetch.sh --config data/neofetch.config")
                            print()

                    elif show_o[1].lower() == "changelog":
                        logger.log(0, 'User opens changelog.', 'logfile.txt', global_variables['SESSION_ID'])
                        version.changelog()

                    elif show_o[1].lower() in ("recent_commands", "recent", "commands"):
                        if global_variables['ROOTNAME'] != '' and global_variables['ROOTPASS'] != '':
                            print("[i] Please log-in as root first:")
                            src_rootuser = input("Root Username: ")
                            src_rootpass = getpass("Root Password: ")
                            if misc.programFunctions().login_root(global_variables, src_rootuser, src_rootpass) == "Login Successful!":
                                print("Recent Commands:")
                                for i in range(readline.get_current_history_length()):
                                    print("- " + str(readline.get_history_item(i + 1)))

                            else:
                                print(error.errorCodes().ERROR0013)

                            del src_rootuser, src_rootpass

                        else:
                            print("Recent Commands:")
                            for i in range(readline.get_current_history_length()):
                                print("- " + str(readline.get_history_item(i + 1)))

                    elif show_o[1].lower() in ("traceback", "tracebacks"):
                        leline = misc.CC + misc.FB + misc.FI + ('=' * 25) + " Latest Exceptions " + ('=' * 25) + misc.END
                        print()
                        print(leline)
                        print()
                        print(recent_exceptions)
                        print()
                        print(leline)
                        print()
                        del leline

                    elif show_o[1].lower() == "config_files":
                        logger.log(0, "User lists available configuration files...", 'logfile.txt', global_variables['SESSION_ID'])
                        try:
                            available_config_files = os.listdir('data/')
                            acf_iterator = 0
                            for config_files in available_config_files:
                                if config_files == 'config.dat' or config_files == '.default_config.dat' or config_files == '.installed.dat' or config_files == '.SSFhistory' or config_files == '.SSFnotes' or config_files == 'neofetch.config':
                                    continue

                                else:
                                    acf_iterator += 1
                                    print("[" + str(acf_iterator) + "] " + config_files)

                            del acf_iterator

                        except NotImplementedError:
                            recent_exceptions = traceback.format_exc()
                            logger.log(0, "NotImplementedError exception raised.", 'logfile.txt', global_variables['SESSION_ID'])
                            print("[SYSTEM] functionality is unavailable")

                    else:
                        raise IndexError

                except IndexError:
                    print()
                    print("Usage: show [OPTION]")
                    print()
                    print("license  copying  copyright         -    Shows the full license via less command.")
                    print("info  information  status  stats    -    Shows the current information of Shadow Suite.")
                    print("system_info  system_stats           -    Shows the system information.")
                    print("changelog                           -    Shows the changelog via less command.")
                    print("config_files                        -    Lists the configuration files available.")
                    print("recent_commands                     -    Lists the recent commands entered.")
                    print("tracebacks                          -    Lists the most latest exception/s.")
                    print()

            elif menu_input.lower().startswith("update"):
                update_o = menu_input.split(" ")
                try:
                    if update_o[1].lower() in ["prog", "program"]:
                        print(misc.CGR + "Fetching Shadow Suite Framework from Shadow Team's repository..." + misc.CW)
                        logger.log(0, 'User performs a program update...', 'logfile.txt', global_variables['SESSION_ID'])
                        update.prog_update(global_variables, global_variables['DEBUGGING'])

                    elif update_o[1].lower() in ["deps", "dependencies", "dependency"]:
                        print(misc.CGR + "Downloading and installing dependencies..." + misc.CW)
                        logger.log(0, 'User performs a dependency update...', 'logfile.txt', global_variables['SESSION_ID'])
                        update.deps_update(global_variables)

                    elif update_o[1].lower() in ["full", "all"]:
                        print(misc.CGR + "Do you really want to perform a full update (y/n)?" + misc.CW)
                        full_updateinput = input(" > ")
                        if full_updateinput == "y" or full_updateinput == "Y":
                            logger.log(0, 'User performs a full update...', 'logfile.txt', global_variables['SESSION_ID'])
                            update.full_update(global_variables, global_variables['DEBUGGING'])

                        elif full_updateinput == "n" or full_updateinput == "N":
                            print(misc.CR + "Full update cancelled by user..." + misc.CW)

                        else:
                            print(error.errorCodes().ERROR0001)

                    else:
                        raise IndexError

                except IndexError:
                    print()
                    print("[i] Usage: update [OPTION]")
                    print()
                    print("prog  program                     -    Update Shadow Suite from GitHub.")
                    print("deps  dependencies  dependency    -    Update/install dependencies.")
                    print("full  all                         -    Update both Shadow Suite and dependencies.")
                    print()

            elif menu_input.lower().startswith("config"):
                config_o = menu_input.split(" ")
                try:
                    if config_o[1].lower() in ["username"]:
                        temp_curr_user = config_o[2]
                        config_o[2] = misc.programFunctions().hash(config_o[2], 'sha256')
                        global_variables['USERNAME'] = config_o[2]
                        if global_variables['ROOTPASS'] == None or global_variables['ROOTPASS'] == "":
                            global_variables['USERNAME'] = config_o[2]
                            global_variables['current_user'] = temp_curr_user
                            logger.log(3, 'User changed his username...', 'logfile.txt', global_variables['SESSION_ID'])
                            print("[i] Username successfully changed!")

                        else:
                            confirm_rootpass = getpass("Enter root password to continue: ")
                            confirm_rootpass = misc.programFunctions().hash(confirm_rootpass, 'sha256')
                            # print(confirm_rootpass + '\n' + global_variables['ROOTPASS']) # DEV0005: just for debugging purposes...
                            if confirm_rootpass == global_variables['ROOTPASS']:
                                global_variables['USERNAME'] = config_o[2]
                                global_variables['current_user'] = temp_curr_user
                                logger.log(3, 'User changed his username...', 'logfile.txt', global_variables['SESSION_ID'])
                                print("[i] Username successfully changed!")
                                del confirm_rootpass

                            else:
                                logger.log(4, 'User failed to change his username... Wrong root password.', 'logfile.txt', global_variables['SESSION_ID'])
                                print(error.errorCodes().ERROR0013 + " [i] This incident will be reported!")
                                del confirm_rootpass

                    elif config_o[1].lower() in ["password", "passwd"]:
                        if global_variables['USERPASS'] == "" or global_variables['USERPASS'] == None:
                            new_userpass1 = getpass("Enter new password: ")
                            new_userpass2 = getpass("Confirm new password: ")
                            if new_userpass1 == new_userpass2:
                                new_userpass1 = misc.programFunctions().hash(new_userpass1, 'sha256')
                                global_variables['USERPASS'] = new_userpass1
                                logger.log(3, 'User changed his password...', 'logfile.txt', global_variables['SESSION_ID'])
                                print("[i] Password successfully changed!")

                            else:
                                logger.log(3, 'User failed to change his password... Passwords doesn\'t match', 'logfile.txt', global_variables['SESSION_ID'])
                                print("[i] Passwords doesn't match! This incident will be reported!")

                        else:
                            old_userpass = getpass("Enter old password: ")
                            old_userpass = misc.programFunctions().hash(old_userpass, 'sha256')
                            if old_userpass == global_variables['USERPASS']:
                                new_userpass1 = getpass("Enter new password: ")
                                new_userpass2 = getpass("Confirm new password: ")
                                if new_userpass1 == new_userpass2:
                                    new_userpass1 = misc.programFunctions().hash(new_userpass1, 'sha256')
                                    global_variables['USERPASS'] = new_userpass1
                                    logger.log(3, 'User changed his password...', 'logfile.txt', global_variables['SESSION_ID'])
                                    print("[i] Password successfully changed!")

                                else:
                                    logger.log(3, 'User failed to change his username... Passwords doesn\'t match', 'logfile.txt', global_variables['SESSION_ID'])
                                    print("[i] Passwords doesn't match! This incident will be reported!")

                            else:
                                logger.log(3, 'User failed to change his password... Wrong username/password.', 'logfile.txt', global_variables['SESSION_ID'])
                                print(error.errorCodes().ERROR0013 + " [i] This incident will be reported!")

                    elif config_o[1].lower() in ["rootname"]:
                        config_o[2] = misc.programFunctions().hash(config_o[2], 'sha256')
                        if global_variables['ROOTPASS'] == None or global_variables['ROOTPASS'] == "":
                            global_variables['ROOTNAME'] = config_o[2]
                            logger.log(3, 'User changed his root username...', 'logfile.txt', global_variables['SESSION_ID'])
                            print("[i] Root username successfully changed!")

                        else:
                            confirm_rootpass = getpass("Enter root password to continue: ")
                            confirm_rootpass = misc.programFunctions().hash(confirm_rootpass, 'sha256')
                            if confirm_rootpass == global_variables['ROOTPASS']:
                                global_variables['ROOTNAME'] = config_o[2]
                                logger.log(3, 'User changed his root username...', 'logfile.txt', global_variables['SESSION_ID'])
                                print("[i] Root username successfully changed!")
                                del confirm_rootpass

                            else:
                                logger.log(3, 'User failed to change his root username... Wrong username/password.', 'logfile.txt', global_variables['SESSION_ID'])
                                print(error.errorCodes().ERROR0013 + " [i] This incident will be reported!")
                                del confirm_rootpass

                    elif config_o[1].lower() in ["rootpass"]:
                        if global_variables['ROOTPASS'] == "" or global_variables['ROOTPASS'] == None:
                            new_rootpass1 = getpass("Enter new root password: ")
                            new_rootpass2 = getpass("Confirm new root password: ")
                            if new_rootpass1 == new_rootpass2:
                                new_rootpass1 = misc.programFunctions().hash(new_rootpass1, 'sha256')
                                global_variables['ROOTPASS'] = new_rootpass1
                                logger.log(3, 'User changed his root password...', 'logfile.txt', global_variables['SESSION_ID'])
                                print("[i] Root password successfully changed!")

                            else:
                                logger.log(3, 'User failed to change his root password... Passwords doesn\'t match', 'logfile.txt', global_variables['SESSION_ID'])
                                print("[i] Root passwords doesn't match! This incident will be reported!")

                        else:
                            old_rootpass = getpass("Enter old root password: ")
                            old_rootpass = misc.programFunctions().hash(old_rootpass, 'sha256')
                            if old_rootpass == global_variables['ROOTPASS']:
                                new_rootpass1 = getpass("Enter new root password: ")
                                new_rootpass2 = getpass("Confirm new root password: ")
                                if new_rootpass1 == new_rootpass2:
                                    new_rootpass1 = misc.programFunctions().hash(new_rootpass1, 'sha256')
                                    global_variables['ROOTPASS'] = new_rootpass1
                                    logger.log(3, 'User changed his root password...', 'logfile.txt', global_variables['SESSION_ID'])
                                    print("[i] Root password successfully changed!")

                                else:
                                    logger.log(3, 'User failed to change his root password... Passwords doesn\'t match.', 'logfile.txt', global_variables['SESSION_ID'])
                                    print("[i] Root passwords doesn't match! This incident will be reported!")

                            else:
                                logger.log(3, 'User failed to change his root password... Wrong username/password', 'logfile.txt', global_variables['SESSION_ID'])
                                print(error.errorCodes().ERROR0013 + " [i] This incident will be reported!")

                    elif config_o[1].lower() in ["module_path"]:
                        if global_variables['ROOTNAME'] != '' and global_variables['ROOTPASS'] != '':
                            print("[i] Please log-in as root first:")
                            mp_rootuser = input("Root Username: ")
                            mp_rootpass = getpass("Root Password: ")
                            if misc.programFunctions().login_root(global_variables, mp_rootuser, mp_rootpass) == "Login Successful!":
                                pass

                            else:
                                print(error.errorCodes().ERROR0013)
                                return "Temporary Return"

                            del mp_rootuser, mp_rootpass

                        else:
                            pass

                        new_module_path = input("Enter the new module path: ")
                        if misc.programFunctions().path_exists(new_module_path):
                            if misc.programFunctions().isfolder(new_module_path):
                                global_variables['MODULE_PATH'] = new_module_path
                                logger.log(3, 'User changed the module path to ' + new_module_path + '...', 'logfile.txt', global_variables['SESSION_ID'])
                                print("[i] Module path set!")

                            else:
                                print(error.errorCodes().ERROR0015)

                        else:
                            print(error.errorCodes().ERROR0015)

                    elif config_o[1].lower() in ["output_path"]:
                        if global_variables['ROOTNAME'] != '' and global_variables['ROOTPASS'] != '':
                            print("[i] Please log-in as root first:")
                            op_rootuser = input("Root Username: ")
                            op_rootpass = getpass("Root Password: ")
                            if misc.programFunctions().login_root(global_variables, op_rootuser, op_rootpass) == "Login Successful!":
                                pass

                            else:
                                print(error.errorCodes().ERROR0013)
                                return "Temporary Return"

                            del op_rootuser, op_rootpass

                        else:
                            pass

                        new_output_path = input("Enter the new output path: ")
                        if misc.programFunctions().path_exists(new_output_path):
                            if misc.programFunctions().isfolder(new_output_path):
                                global_variables['OUTPUT_PATH'] = new_output_path
                                logger.log(3, 'User changed the output path to ' + new_output_path + '...', 'logfile.txt', global_variables['SESSION_ID'])
                                print("[i] Output path set!")

                            else:
                                print(error.errorCodes().ERROR0015)

                        else:
                            print(error.errorCodes().ERROR0015)

                    elif config_o[1].lower() in ["binary_path"]:
                        if global_variables['ROOTNAME'] != '' and global_variables['ROOTPASS'] != '':
                            print("[i] Please log-in as root first:")
                            bp_rootuser = input("Root Username: ")
                            bp_rootpass = getpass("Root Password: ")
                            if misc.programFunctions().login_root(global_variables, bp_rootuser, bp_rootpass) == "Login Successful!":
                                pass

                            else:
                                print(error.errorCodes().ERROR0013)
                                return "Temporary Return"

                            del bp_rootuser, bp_rootpass

                        else:
                            pass

                        new_binary_path = input("Enter the new binary path (usually /usr/bin/): ")
                        if misc.programFunctions().path_exists(new_binary_path):
                            if misc.programFunctions().isfolder(new_binary_path):
                                global_variables['BINARY_PATH'] = new_binary_path
                                logger.log(3, 'User changed the binary path to ' + new_binary_path + '...', 'logfile.txt', global_variables['SESSION_ID'])
                                print("[i] Binary path set!")

                            else:
                                print(error.errorCodes().ERROR0015)

                        else:
                            print(error.errorCodes().ERROR0015)

                    elif config_o[1].lower() in ["export", "save"]:
                        if global_variables['ROOTNAME'] != '' and global_variables['ROOTPASS'] != '':
                            print("[i] Please log-in as root first:")
                            sav_rootuser = input("Root Username: ")
                            sav_rootpass = getpass("Root Password: ")
                            if misc.programFunctions().login_root(global_variables, sav_rootuser, sav_rootpass) == "Login Successful!":
                                pass

                            else:
                                print(error.errorCodes().ERROR0013)
                                return "Temporary Return"

                            del sav_rootuser, sav_rootpass

                        else:
                            pass

                        config_dict = {
                                "username": global_variables['USERNAME'],
                                "userpass": global_variables['USERPASS'],
                                "rootname": global_variables['ROOTNAME'],
                                "rootpass": global_variables['ROOTPASS'],
                                "module_path": global_variables['MODULE_PATH'],
                                "output_path": global_variables['OUTPUT_PATH'],
                                "binary_path": global_variables['BINARY_PATH'],
                                "notes_maxlines": global_variables['NOTES_MAXLINES']
                                }
                        try:
                            open(global_variables['config_file'], 'r').read()
                            open(global_variables['config_file'], 'r').close()
                            confirm_export_overwrite = input("Do you really want to overwrite the current configuration file? (y/n) > ").lower()
                            if confirm_export_overwrite == 'y':
                                export_conf_result = API.ShadowSuite(global_variables['current_user'], global_variables['MODULE_PATH'], global_variables['OUTPUT_PATH'], global_variables['SESSION_ID'], global_variables['USERLEVEL'], global_variables['DEBUGGING']).export_conf(global_variables['config_file'], config_dict)
                                if export_conf_result == True:
                                    logger.log(3, 'Current user settings successfully saved to ' + global_variables['config_file'] + '.', 'logfile.txt', global_variables['SESSION_ID'])
                                    print("[i] Settings successfully saved to configuration file: \"" + global_variables['config_file'] + "\".")

                                else:
                                    print("[i] There was a problem exporting the settings.")

                            elif confirm_export_overwrite == 'n':
                                print("[i] Saving of settings to configuration file aborted.")

                            else:
                                print("[i] Unknown answer, assuming no.")

                        except FileNotFoundError:
                            export_conf_result = API.ShadowSuite(global_variables['current_user'], global_variables['MODULE_PATH'], global_variables['OUTPUT_PATH'], global_variables['SESSION_ID'], global_variables['USERLEVEL'], debugging).export_conf(global_variables['config_file'], config_dict)
                            if export_conf_result == True:
                                logger.log(3, 'Current user settings successfully saved to ' + global_variables['config_file'] + '.', 'logfile.txt', global_variables['SESSION_ID'])
                                print("[i] Settings successfully saved to configuration file: \"" + global_variables['config_file'] + "\".")

                            else:
                                print("[i] There was a problem exporting the settings.")

                    elif config_o[1].lower() in ['generate']:
                        if global_variables['ROOTNAME'] != '' and global_variables['ROOTPASS'] != '':
                            print("[i] Please log-in as root first:")
                            gen_rootuser = input("Root Username: ")
                            gen_rootpass = getpass("Root Password: ")
                            if misc.programFunctions().login_root(global_variables, gen_rootuser, gen_rootpass) == "Login Successful!":
                                pass

                            else:
                                print(error.errorCodes().ERROR0013)
                                return "Temporary Return"

                            del gen_rootuser, gen_rootpass

                        else:
                            pass

                        new_config = config_o[2]
                        if 'data/' not in new_config:
                            new_config = "data/" + new_config

                        if '.dat' not in new_config:
                            new_config = new_config + '.dat'

                        if misc.programFunctions().path_exists(new_config) and misc.programFunctions().isfile(new_config):
                            print("[i] Saving of settings to new configuration file aborted. File already exists.")
                            return "Temporary Return"

                        else:
                            print('[i] Exporting...')
                            config_dict = {
                                    "username": global_variables['USERNAME'],
                                    "userpass": global_variables['USERPASS'],
                                    "rootname": global_variables['ROOTNAME'],
                                    "rootpass": global_variables['ROOTPASS'],
                                    "module_path": global_variables['MODULE_PATH'],
                                    "output_path": global_variables['OUTPUT_PATH'],
                                    "binary_path": global_variables['BINARY_PATH'],
                                    "notes_maxlines": global_variables['NOTES_MAXLINES']
                                    }
                            export_conf_result = API.ShadowSuite(global_variables['current_user'], global_variables['MODULE_PATH'], global_variables['OUTPUT_PATH'], global_variables['SESSION_ID'], global_variables['USERLEVEL'], global_variables['DEBUGGING']).export_conf(new_config, config_dict)
                            if export_conf_result == True:
                                logger.log(3, 'User generated new config file named ' + new_config +'.', 'logfile.txt', global_variables['SESSION_ID'])
                                print("[i] " + new_config + " successfully generated!")

                            else:
                                print("[i] There was a problem generating the configuration file.")

                    elif config_o[1].lower() in ['remove', 'del', 'delete']:
                        if global_variables['ROOTNAME'] != '' and global_variables['ROOTPASS'] != '':
                            print("[i] Please log-in as root first:")
                            del_rootuser = input("Root Username: ")
                            del_rootpass = getpass("Root Password: ")
                            if misc.programFunctions().login_root(global_variables, del_rootuser, del_rootpass) == "Login Successful!":
                                pass

                            else:
                                print(error.errorCodes().ERROR0013)
                                return "Temporary Return"

                            del del_rootuser, del_rootpass

                        else:
                            pass

                        if '.dat' not in config_o[2]:
                            config_o[2] += '.dat'

                        if 'data/' in config_o[2]:
                            config_o[2] = config_o[2].replace('data/', '')

                        if config_o[2] == 'config.dat':
                            print(error.warningCodes().WARNING0005)
                            ask_remove_default_config = input("Do you still want to continue? (y/n) > ").lower()
                            if ask_remove_default_config == 'y':
                                os.remove('data/' + config_o[2])
                                logger.log(3, 'User removed '+ config_o[2] + ' configuration file...', 'logfile.txt', global_variables['SESSION_ID'])
                                print("[i] Configuration file removed succesfully!")

                            else:
                                pass

                            del ask_remove_default_config

                        else:
                            ask_remove_config = input("Do you really want to remove " + config_o[2] + "? (y/n) > ").lower()
                            if ask_remove_config == 'y':
                                os.remove('data/' + config_o[2])
                                logger.log(3, 'User removed ' + config_o[2] + ' configuration file...', 'logfile.txt', global_variables['SESSION_ID'])
                                print("[i] Configuration file removed successfully!")

                            else:
                                pass

                            del ask_remove_config

                    elif config_o[1].startswith("reset"):
                        if global_variables['ROOTNAME'] != '' and global_variables['ROOTPASS'] != '':
                            print("[i] Please log-in as root first:")
                            rst_rootuser = input("Root Username: ")
                            rst_rootpass = getpass("Root Password: ")
                            if misc.programFunctions().login_root(global_variables, rst_rootuser, rst_rootpass) == "Login Successful!":
                                pass

                            else:
                                print(error.errorCodes().ERROR0013)
                                return "Temporary Return"

                            del rst_rootuser, rst_rootpass

                        else:
                            pass

                        confirm_config_reset = input("Do you really want to reset default values to " + global_variables['config_file'] + "? (y/n) > ")
                        if confirm_config_reset.lower() == 'y':
                            if misc.programFunctions().is_windows():
                                os.system("del " + global_variables['config_file'])
                                os.system("xcopy data/.default_config.dat " + global_variables['config_file'])

                            else:
                                os.system("rm " + global_variables['config_file'])
                                os.system("cp data/.default_config.dat " + global_variables['config_file'])

                            print("Default values reset finished! Press enter key to restart.")
                            misc.programFunctions().pause(True)
                            misc.programFunctions().program_restart()


                        else:
                            print("Default values reset aborted.")

                    else:
                        raise IndexError

                except(IndexError, FileNotFoundError):
                    print()
                    print("[i] Usage: config [OPTION] [VALUE]")
                    print()
                    print("username [VALUE]    -    Change username.")
                    print("password | passwd   -    Change password.")
                    print("rootname [VALUE]    -    Change root username.")
                    print("rootpass            -    Change root password.")
                    print("module_path         -    Change the path where modules will be found.")
                    print("output_path         -    Change the path where module outputs will be found.")
                    print("binary_path         -    Change the path where system binaries will be found.")
                    print("export | save       -    Save changes to current configuration file.")
                    print("generate [FILENAME] -    Save changes to a new configuration file.")
                    print("remove [FILENAME]   -    Delete a configuration file.")
                    print("reset               -    Reset default values to 'data/config.dat' file.")
                    print()

            elif menu_input.startswith("module"):
                module_o = menu_input.split(" ")
                try:
                    if module_o[1] in ['show', 'list', 'lst', 'ls']:
                        list_module.list(global_variables['MODULE_PATH'])

                    elif module_o[1] in ['use', 'run', 'exec', 'execute']:
                        module_name = global_variables['MODULE_PATH'] + module_o[2]
                        try:
                            module_name = module_name.replace('/', '.')
                            logger.log(3, 'User used ' + module_name + '.', 'logfile.txt', global_variables['SESSION_ID'])
                            module = importlib.import_module(module_name)
                            try:
                                module_version = module.module_version
                                if module_version < 7.0:
                                    raise AttributeError

                                else:
                                    try:
                                        if misc.programFunctions().is_windows():
                                            pass

                                        else:
                                            print(ansi.set_title("Shadow Suite Framework: " + module_name.replace(global_variables['MODULE_PATH'], '')))

                                        module.main(global_variables)

                                    except Exception as module_error_msg:
                                        recent_exceptions = traceback.format_exc()
                                        print(misc.CR + "[i] " + str(module_error_msg))

                            except AttributeError:
                                try:
                                    if misc.programFunctions().is_windows():
                                        pass

                                    else:
                                        print(ansi.set_title("Shadow Suite Framework: " + module_name))

                                    module.main(global_variables['current_user'], global_variables['MODULE_PATH'], global_variables['OUTPUT_PATH'], global_variables['SESSION_ID'], global_variables['USERLEVEL'], global_variables['DEBUGGING'])

                                except Exception as module_error_msg:
                                    recent_exceptions = traceback.format_exc()
                                    print(misc.CR + "[i] " + str(module_error_msg))

                        except Exception as moduleerror_msg:
                            recent_exceptions = traceback.format_exc()
                            print("[i] " + str(moduleerror_msg))

                        if misc.programFunctions().is_windows():
                            pass

                        else:
                            print(ansi.set_title("Shadow Suite Framework v" + version.VNUMBER))

                    elif module_o[1] in ['info', 'information', 'search', 'query']:
                        if module_o[2] == '*':
                            modules = os.listdir(global_variables['MODULE_PATH'])
                            for module in modules:
                                module_name = global_variables['MODULE_PATH'] + module
                                if misc.programFunctions().isfile(module_name):
                                    pass

                                else:
                                    continue

                                module_name = module_name.replace('.py', '').replace('.Py', '').replace('.pY', '').replace('.PY', '')
                                try:
                                    module_name = module_name.replace('/', '.')
                                    logger.log(3, 'User looks for all modules\' information.')
                                    module = importlib.import_module(module_name)
                                    print("\n\n")
                                    module.module_info()

                                except Exception as moduleerror_msg:
                                    recent_exceptions = traceback.format_exc()
                                    print("[i] " + str(moduleerror_msg))

                                print("\n" + ('=' * 50))

                        else:
                            module_name = global_variables['MODULE_PATH'] + module_o[2]
                            try:
                                module_name = module_name.replace('/', '.')
                                logger.log(3, 'User looks for ' + module_name + ' information.', 'logfile.txt', global_variables['SESSION_ID'])
                                module = importlib.import_module(module_name)
                                print('\n\n')
                                module.module_info()

                            except Exception as moduleerror_msg:
                                recent_exceptions = traceback.format_exc()
                                print("[i] " + str(moduleerror_msg))

                    elif module_o[1] in ['reload', 'restart', 'reboot']:
                        module_name = module_o[2]
                        if module_name == '*':
                            modules = os.listdir(global_variables['MODULE_PATH'])
                            for module in modules:
                                module_name = global_variables['MODULE_PATH'] + module
                                if misc.programFunctions().isfile(module_name):
                                    pass

                                else:
                                    continue

                                module_name = module_name.replace('.py', '').replace('.Py', '').replace('.pY', '').replace('.PY', '')
                                #print(module_name) # DEV0005
                                try:
                                    module_name = module_name.replace('/', '.')
                                    logger.log(3, 'User reloads all modules.')
                                    module = importlib.reload(importlib.import_module(module_name))
                                    print(misc.CG + "[i] " + module_name + " successfully reloaded!" + misc.END)
                                    time.sleep(0.50)

                                except Exception as moduleerror_msg:
                                    recent_exceptions = traceback.format_exc()
                                    print(misc.CR + "[i] " + error.errorCodes().ERROR0020(str(moduleerror_msg)) + misc.CW)
                                    time.sleep(0.50)

                        else:
                            module_name = global_variables['MODULE_PATH'] + module_o[2]
                            try:
                                module_name = module_name.replace('/', '.')
                                logger.log(3, 'User reloads ' + module_name + ' module.', 'logfile.txt', global_variables['SESSION_ID'])
                                module = importlib.reload(importlib.import_module(module_name))
                                print(misc.CG + "[i] " + module_name + " successfully reloaded!" + misc.END)
                                time.sleep(0.50)

                            except Exception as moduleerror_msg:
                                recent_exceptions = traceback.format_exc()
                                print(misc.CR + "[i] " + error.errorCodes().ERROR0020(str(moduleerror_msg)) + misc.CW)
                                time.sleep(0.50)

                    elif module_o[1] in ['generate', 'produce', 'new']:

                        module_name = module_o[2]
                        logger.log(0, 'User generated a new module named ' + module_name, 'logfile.txt', global_variables['SESSION_ID'])
                        if misc.programFunctions().is_windows() == ('windows' or 'win' or 'nt'):
                            os.system("xcopy core/temp_module.py output/" + module_name + ".py")

                        else:
                            os.system("cp core/temp_module.py output/" + module_name + ".py")

                        if misc.programFunctions().path_exists('output/' + module_name + '.py'):
                            print("[i] " + module_name + ".py successfully generated!")

                        else:
                            print(error.errorCodes().ERROR0015 + " (Generated module not found)")

                    elif module_o[1].startswith("test") or module_o[1].startswith("runtest"):
                        if module_o[2] == '*':
                            modules = os.listdir(global_variables['MODULE_PATH'])
                            for module in modules:
                                module = global_variables['MODULE_PATH'] + module
                                if misc.programFunctions().isfile(module) == False:
                                    continue

                                else:
                                    pass

                                module_problems = []
                                print(misc.CY + "[i] Checking for problems on " + misc.CC + module + misc.CY + ' module...' + misc.CW)
                                time.sleep(0.50)
                                try:
                                    test_module = module.replace('/', '.').replace('.py', '')
                                    tester = importlib.import_module(test_module)

                                except Exception as fatalerror_msg:
                                    recent_exceptions = traceback.format_exc()
                                    print(misc.CR + misc.FB + "[i] Fatal error found:\n" + misc.CW + misc.FR)
                                    print(misc.CR + "[i] " + str(fatalerror_msg) + misc.CW)
                                    continue

                                try:
                                    module_version = tester.module_version
                                    if module_version < 7.0:
                                        raise AttributeError

                                    else:
                                        try:
                                            test1 = tester.info

                                        except Exception as test1e:
                                            module_problems.append(str(test1e))

                                        try:
                                            test2 = tester.dependencies

                                        except Exception as test2e:
                                            module_problems.append(str(test2e))

                                        try:
                                            test3 = tester.category

                                        except Exception as test3e:
                                            module_problems.append(str(test3e))

                                        try:
                                            test4 = tester.changelog

                                        except Exception as test4e:
                                            module_problems.append(str(test4e))

                                except AttributeError:
                                    print(misc.CY + "[i] Module is lower than v7.0, Switching to legacy test..." + misc.CW)
                                    time.sleep(0.50)

                                except Exception as fatalerror_msg:
                                    recent_exceptions = traceback.format_exc()
                                    print(misc.CR + misc.FB + "[i] Fatal error found:\n" + misc.CW + misc.FR)
                                    print(misc.CR + "[i] " + str(fatalerror_msg) + misc.CW)
                                    continue

                                    try:
                                        test1 = tester.info

                                    except Exception as test1e:
                                        module_problems.append(str(test1e))

                                    try:
                                       test2 = tester.dependencies

                                    except Exception as test2e:
                                        module_problems.append(str(test2e))

                                    try:
                                        test3 = tester.category

                                    except Exception as test3e:
                                       module_problems.append(str(test3e))

                                    try:
                                        test4 = tester.changelog

                                    except Exception as test4e:
                                        module_problems.append(str(test4e))

                                if module_problems != (None or "" or []):
                                    logger.log(3, test_module + ': Test finished. Problems found:')
                                    print(misc.CR + misc.FB + "\n\nTest finished. Problems found:\n\n" + misc.CW + misc.FR)
                                    for problems in module_problems:
                                        print(misc.CR + '- ' + str(problems) + '\n' + misc.CW)

                                else:
                                    logger.log(3, test_module + ': Testing finished. No problems found.', 'logfile.txt', global_variables['SESSION_ID'])
                                    print(misc.CG + misc.FB + "[i] Testing successful! No problems found." + misc.CW + misc.FR)

                                del tester
                                del module_problems

                                print()
                                print('=' * 50)
                                print()

                        else:
                            if global_variables['MODULE_PATH'] not in module_o[2]:
                                module_o[2] = global_variables['MODULE_PATH'] + module_o[2]

                            if '.py' not in module_o[2]:
                                module_o[2] += '.py'
                                module_problems = []
                                print(misc.CY + "[i] Checking for problems on " + misc.CC + module_o[2] + misc.CY + ' module...' + misc.CW)
                                time.sleep(0.50)
                                try:
                                    test_module = module_o[2].replace('/', '.').replace('.py', '')
                                    tester = importlib.import_module(test_module)

                                except Exception as fatalerror_msg:
                                    print(misc.CR + misc.FB + "[i] Fatal error found:\n" + misc.CW + misc.FR)
                                    recent_exceptions = traceback.format_exc()
                                    print(misc.CR + "[i] " + str(fatalerror_msg) + misc.CW)
                                    return "Temporary Return"

                                try:
                                    module_version = tester.module_version
                                    if module_version < 7.0:
                                        raise AttributeError

                                    else:
                                        try:
                                            test1 = tester.info

                                        except Exception as test1e:
                                            module_problems.append(str(test1e))

                                        try:
                                            test2 = tester.dependencies

                                        except Exception as test2e:
                                            module_problems.append(str(test2e))

                                        try:
                                            test3 = tester.category

                                        except Exception as test3e:
                                            module_problems.append(str(test3e))

                                        try:
                                            test4 = tester.changelog

                                        except Exception as test4e:
                                            module_problems.append(str(test4e))

                                except(AttributeError):
                                    print(misc.CY + "[i] Module is lower than v7.0, Switching to legacy test..." + misc.CW)
                                    time.sleep(0.50)

                                except Exception as fatalerror_msg:
                                    print(misc.CR + misc.FB + "[i] Fatal error found:\n" + misc.CW + misc.FR)
                                    recent_exceptions = traceback.format_exc()
                                    print(misc.CR + "[i] " + str(fatalerror_msg) + misc.CW)
                                    return "Temporary Return"

                                    try:
                                        test1 = tester.info

                                    except Exception as test1e:
                                        module_problems.append(str(test1e))

                                    try:
                                        test2 = tester.dependencies

                                    except Exception as test2e:
                                        module_problems.append(str(test2e))

                                    try:
                                        test3 = tester.category

                                    except Exception as test3e:
                                        module_problems.append(str(test3e))

                                    try:
                                        test4 = tester.changelog

                                    except Exception as test4e:
                                        module_problems.append(str(test4e))

                                if module_problems != (None or "" or []):
                                    logger.log(3, module_o[2] + ': Test finished. Problems found:')
                                    print(misc.CR + misc.FB + "\n\nTest finished. Problems found:\n\n" + misc.CW + misc.FR)
                                    for problems in module_problems:
                                        print(misc.CR + '- ' + str(problems) + '\n' + misc.CW)

                                else:
                                    logger.log(3, module_o[2] + ': Testing finished. No problems found.', 'logfile.txt', global_variables['SESSION_ID'])
                                    print(misc.CG + misc.FB + "[i] Testing successful! No problems found." + misc.CW + misc.FR)

                                del tester
                                del module_problems

                    elif module_o[1].startswith("install"):
                        if misc.programFunctions().path_exists(module_o[2]):
                            if global_variables['ROOTNAME'] != '' and global_variables['ROOTPASS'] != '':
                                print("[i] Please log-in as root first:")
                                ins_rootuser = input("Root Username: ")
                                ins_rootpass = getpass("Root Password: ")
                                if misc.programFunctions().login_root(global_variables, ins_rootuser, ins_rootpass) == "Login Successful!":
                                    pass

                                else:
                                    print(error.errorCodes().ERROR0013)
                                    return "Temporary Return"

                                del ins_rootuser, ins_rootpass

                            else:
                                pass

                            logger.log(3, 'User is trying to install ' + module_o[2] + ' package...', 'logfile.txt', global_variables['SESSION_ID'])
                            print("[i] Path found...")
                            if '.py' in module_o[2]:
                                logger.log(3, 'Parsing ' + module_o[2] + ' package...', 'logfile.txt', global_variables['SESSION_ID'])
                                print("[i] Parsing " + module_o[2] + '...')
                                try:
                                    parse_module = module_o[2].replace('/', '.').replace('.py', '')
                                    parser = importlib.import_module(parse_module)
                                    parser.module_info()

                                except Exception as parsingerror_msg:
                                    recent_exceptions = traceback.format_exc()
                                    logger.log(3, module_o[2] + ': ' + error.errorCodes().ERROR0017 + "(" + str(parsingerror_msg) + ")", 'logfile.txt', global_variables['SESSION_ID'])
                                    print("[i] " + error.errorCodes().ERROR0017)
                                    print("[i] " + str(parsingerror_msg))

                                else:
                                    logger.log(3, module_o[2] + ': Parsing successful... Now installing', 'logfile.txt', global_variables['SESSION_ID'])
                                    print("[i] Parsing successful!")
                                    print("[i] Installing " + module_o[2] + '...')
                                    if misc.programFunctions().is_windows():
                                        os.system("xcopy " + module_o[2] + " modules/")

                                    else:
                                        os.system("cp " + module_o[2] + " modules/")

                                    module_dependencies = parser.dependencies
                                    bin_manual_install = []
                                    manual_install =[]
                                    #print(module_dependencies) # DEV0005: for debugging purposes only
                                    for deps in module_dependencies:
                                        logger.log(3, 'Installing dependency: ' + deps, 'logfile.txt', global_variables['SESSION_ID'])
                                        #print(deps) # DEV0005: For debugging purposes only
                                        if 'BINARY: ' in deps:
                                            deps = deps.replace('BINARY: ', '')
                                            if misc.programFunctions().is_windows():
                                                manual_install.append('BINARY: ' + deps)

                                            else:
                                                if misc.programFunctions().path_exists(global_variables['BINARY_PATH'] + "apt"):
                                                    subprocess.Popen(args='apt install --upgrade ' + deps, shell=True, universal_newlines=True)

                                                elif misc.programFunctions().path_exists(global_variables['BINARY_PATH'] + "pkg"):
                                                    subprocess.Popen(args='pkg install --upgrade' + deps, shell=True, universal_newlines=True)

                                                elif misc.programFunctions().path_exists(global_variables['BINARY_PATH'] + "yum"):
                                                    subprocess.Popen(args='yum install ' + deps, shell=True, universal_newlines=True)

                                                else:
                                                    manual_install.append('BINARY: ' + deps)

                                        elif 'PYTHON: ' in deps:
                                            deps = deps.replace('PYTHON: ', '')
                                            misc.programFunctions().pip_install(deps)

                                        elif 'PERL: ' in deps:
                                            deps = deps.replace('PERL: ', '')
                                            subprocess.Popen(args='cpan install ' + deps, shell=True, universal_newlines=True)

                                        elif 'RUBY: ' in deps:
                                            deps = deps.replace('RUBY: ', '')
                                            os.system('gem install ' + deps)

                                        else:
                                            manual_install.append(deps)

                                    if manual_install != (None or []):
                                        print("[i] Can't install the following:\n")
                                        logger.log(3, 'Failed to install dependencies: ' + str(manual_install), 'logfile.txt', global_variables['SESSION_ID'])
                                        print(manual_install)
                                        for ideps in manual_install:
                                            print("- |" + ideps + '|')

                                        print("\nPlease install to use the module without errors...")

                            else:
                                logger.log(3, module_o[2] + ' is not a valid SSF module.', 'logfile.txt', global_variables['SESSION_ID'])
                                print("[i] " + error.errorCodes().ERROR0016)

                        else:
                            print("[i] " + error.errorCodes().ERROR0015)

                    elif module_o[1].lower() in ["uninstall"]:
                        if global_variables['MODULE_PATH'] not in module_o[2]:
                            module_name = global_variables['MODULE_PATH'] +  module_o[2]

                        else:
                            module_name = module_o[2]

                        if '.py' not in module_name:
                            module_name = module_name + '.py'

                        #print(module_name) # DEV0005: For debugging purposes only

                        if misc.programFunctions().path_exists(module_name):
                            if global_variables['ROOTNAME'] != '' and global_variables['ROOTPASS'] != '':
                                print("[i] Please log-in as root first:")
                                uns_rootuser = input("Root Username: ")
                                uns_rootpass = getpass("Root Password: ")
                                if misc.programFunctions().login_root(global_variables, uns_rootuser, uns_rootpass) == "Login Successful!":
                                    pass

                                else:
                                    print(error.errorCodes().ERROR0013)
                                    return "Temporary Return"

                                del uns_rootuser, uns_rootpass

                            else:
                                pass

                            confirm_uninstall = input("Do you really want to uninstall " + module_name + "? (y/n) > ")
                            if confirm_uninstall.lower() == ('y' or 'yes'):
                                logger.log(3, 'User is trying to uninstall ' + module_name + '...', 'logfile.txt', global_variables['SESSION_ID'])
                                print("[i] Uninstalling " + module_name + "...")
                                os.remove(module_name)
                                if misc.programFunctions().path_exists(module_name):
                                    logger.log(3, module_name + ": " + error.errorCodes().ERROR0018, 'logfile.txt', global_variables['SESSION_ID'])
                                    print("[i] " + error.errorCodes().ERROR0018)

                                else:
                                    logger.log(3, 'User successfully uninstalled ' + module_name, 'logfile.txt', global_variables['SESSION_ID'])
                                    print("[i] " + module_name + " successfully uninstalled...")

                            else:
                                print("[i] User cancelled uninstallation...")

                        else:
                            print("[i] " + error.errorCodes().ERROR0015 + ' (Module not found)')

                    else:
                        raise IndexError

                except IndexError:
                    print()
                    print("[i] Usage: module [OPTION] [ARGUMENTS]")
                    print()
                    print("show  list  lst  ls                   -  List available modules.")
                    print("use || run || exec || [MODULE]        -  Use specified module.")
                    print("info || search || query [MODULE]      -  Show information of the specified module. (\"*\" for all)")
                    print("reload || restart || reboot [MODULE]  -  Reload a specified module. (\"*\" for all)")
                    print("generate || produce || new [MODULE]   -  Generate a new module template.")
                    print("test || runtest [MODULE]              -  Test a module. (\"*\" for all)")
                    print("install [MODULE_PATH]                 -  Install a module.")
                    print("uninstall [MODULE_PATH]               -  Uninstall a module.")
                    print()

            elif menu_input.lower().startswith(("service", "services")):
                try:
                    services_o = menu_input.split(' ')
                    if services_o[1].lower().startswith(('show', 'list', 'lst', 'ls')):
                        list_services.list(global_variables['SERVICES_PATH'])
                        print(active_services) # DEV0005

                    elif services_o[1].lower().startswith(('start', 'enable')):
                        service_name = global_variables['SERVICES_PATH'] + services_o[2]
                        try:
                            service_name = service_name.replace('/', '.')
                            logger.log(3, 'User started ' + service_name + ' service.', 'logfile.txt', global_variables['SESSION_ID'])
                            service_importlib(service_name, 'start')

                        except Exception as service_err:
                            recent_exceptions = traceback.format_exc()
                            print(error.errorCodes().ERROR0020(str(service_err)))

                    elif services_o[1].lower().startswith(('stop', 'disable')):
                        service_name = global_variables['SERVICES_PATH'] + services_o[2]
                        try:
                            service_name = service_name.replace('/', '.')
                            logger.log(3, 'User started ' + service_name + ' service.', 'logfile.txt', global_variables['SESSION_ID'])
                            service_importlib(service_name, 'stop')

                        except Exception as service_err:
                            recent_exceptions = traceback.format_exc()
                            print(error.errorCodes().ERROR0020(str(service_err)))

                    elif services_o[1].lower().startswith(('info', 'search', 'query')):
                        service_name = global_variables['SERVICES_PATH'] + services_o[2]
                        try:
                            service_name = service_name.replace('/', '.')
                            logger.log(3, 'User shows info about ' + service_name + ' service.', 'logfile.txt', global_variables['SESSION_ID'])
                            service_importlib(service_name, 'info')

                        except Exception as service_err:
                            recent_exceptions = traceback.format_exc()
                            print(error.errorCodes().ERROR0020(str(service_err)))

                    elif services_o[1].lower().startswith(('reload', 'restart', 'reboot')):
                        pass

                    elif services_o[1].lower().startswith(('generate', 'produce', 'new')):
                        pass

                    elif services_o[1].lower().startswith(('test', 'runtest')):
                        pass

                    elif services_o[1].lower().startswith(('install')):
                        pass

                    elif services_o[1].lower().startswith(('uninstall')):
                        pass

                    else:
                        raise IndexError

                except IndexError:
                    print()
                    print("[i] Usage: services [OPTION] [ARGUMENTS]")
                    print()
                    print("show  list  lst  ls                   -  List available services.")
                    print("start || enable || [SERVICE]   -  Start specified service.")
                    print("stop || disable || [SERVICE]   -  Stop specified service.")
                    print("info || search || query [SERVICE]     -  Show information of the specified service. " + misc.FE + "(\"*\" for all)" + misc.END)
                    print("reload || restart || reboot [SERVICE] -  Reload a specified service. " + misc.FE + "(\"*\" for all)" + misc.END)
                    print("generate || produce || new [SERVICE]  -  Generate a new service template.")
                    print("test || runtest [SERVICE]             -  Test a service. " + misc.FE + "(\"*\" for all)" + misc.END)
                    print("install [SERVICE_PATH]                -  Install a service.")
                    print("uninstall [SERVICE_PATH]              -  Uninstall a service.")
                    print()

            elif menu_input.lower().startswith("suggest"):
                try:
                    if '=' not in menu_input:
                        raise IndexError

                    suggest_o = menu_input.split('=')
                    suggest_o[1] = suggest_o[1].lower()
                    #print(suggest_o[1]) # DEV0005: For debugging purposes only.
                    logger.log(0, 'User want a suggestion with the criteria ' + suggest_o[1] + '.', 'logfile.txt', global_variables['SESSION_ID'])
                    suggest.api(suggest_o[1], global_variables['MODULE_PATH'])

                except IndexError:
                    print()
                    print("[i] Usage: suggest=CRITERIA1,CRITERIA2,CRITERIA3,...,CRITERIA4")
                    print()

            elif menu_input.lower().startswith(('notepad', 'note', 'notes')):
                try:
                    suggest_o = menu_input.split(' ')
                    notes = 'data/.SSFnotes'
                    if suggest_o[1].lower().startswith(("add", "new")):
                        if global_variables['ROOTNAME'] != '' and global_variables['ROOTPASS'] != '':
                            print("[i] Please log-in first:")
                            npd_username = input("Username: ")
                            npd_password = getpass("Password: ")
                            if misc.programFunctions().login_user(global_variables, npd_username, npd_password) == "Login Successful!":
                                pass

                            else:
                                print(error.errorCodes().ERROR0013)
                                return "Temporary Return"

                            del npd_username, npd_password

                        else:
                            pass

                        start = 2
                        note = ""
                        for word in suggest_o:
                            if start == 0:
                                note += word + ' '

                            else:
                                start -= 1

                        with open(notes, 'a') as fopen:
                            fopen.write(note + '\n')

                        print("[i] Note added! | " + note)
                        del start, note

                    elif suggest_o[1].lower().startswith(('show', 'ls')):
                        if global_variables['ROOTNAME'] != '' and global_variables['ROOTPASS'] != '':
                            print("[i] Please log-in first:")
                            npd_username = input("Username: ")
                            npd_password = getpass("Password: ")
                            if misc.programFunctions().login_user(global_variables, npd_username, npd_password) == "Login Successful!":
                                pass

                            else:
                                print(error.errorCodes().ERROR0013)
                                return "Temporary Return"

                            del npd_username, npd_password

                        else:
                            pass

                        try:
                            open(notes, 'r').read()
                            open(notes, 'r').close()

                        except:
                            recent_exceptions = traceback.format_exc()
                            print(error.errorCodes().ERROR0019)
                            return "Temporary Return"

                        try:
                            with open(notes, 'r') as fopen:
                                notes = fopen.readlines()

                        except Exception as openerr:
                            print(misc.CR + "[i] No notes saved!")
                            return None

                        if notes == '':
                            print(misc.CR + "[i] No notes saved!")
                            return None

                        print("Notes: ")
                        MAXLINES = global_variables['NOTES_MAXLINES']
                        CURLINES = 0
                        for note in notes:
                            CURLINES += 1
                            if CURLINES <= MAXLINES:
                                note = note.replace('\n', '')
                                print('[' + str(CURLINES) + '] ' + note)

                            else:
                                print(misc.CY + "[i] Max lines reached!\n    You can override this by changing the value from the configuration file." + misc.END)
                                break

                    elif suggest_o[1].lower().startswith(('rm', 'del')):
                        if global_variables['ROOTNAME'] != '' and global_variables['ROOTPASS'] != '':
                            print("[i] Please log-in first:")
                            npd_username = input("Username: ")
                            npd_password = getpass("Password: ")
                            if misc.programFunctions().login_user(global_variables, npd_username, npd_password) == "Login Successful!":
                                pass

                            else:
                                print(error.errorCodes().ERROR0013)
                                return "Temporary Return"

                            del npd_username, npd_password

                        else:
                            pass

                        try:
                            open(notes, 'r').read()
                            open(notes, 'r').close()

                        except(IOError, EOFError, FileNotFoundError):
                            print(error.errorCodes().ERROR0019)
                            return "Temporary Return"

                        with open(notes, 'r') as fopen:
                            notes_data = fopen.readlines()

                        print("Notes: ")
                        MAXLINES = global_variables['NOTES_MAXLINES']
                        CURLINES = 1
                        while CURLINES <= len(notes_data):
                            print("[" + str(CURLINES) + "] " + notes_data[(CURLINES - 1)].replace('\n', ''))
                            CURLINES += 1

                        while True:
                            try:
                                del_line = input("Line number to remove (0 to cancel; * for all): ")
                                if del_line == '*':
                                    while True:
                                        confirm_delete = input("Are you sure to remove all notes? (y/n) > ")
                                        if confirm_delete.lower() in ('y', 'yes'):
                                            print(misc.CGR, "[i] Removing all notes...", misc.END)
                                            os.remove(notes)
                                            print(misc.CGR, "[i] Removing all notes... Done!", misc.END)
                                            return "Temporary Return"

                                        elif confirm_delete.lower() in ('n', 'no'):
                                            print("[i] No notes removed.")
                                            break

                                        else:
                                            continue

                                else:
                                    del_line = int(del_line)

                                if del_line == 0:
                                    print("[i] No notes removed.")
                                    break

                                else:
                                    if del_line < 0 and del_line >= len(notes_data):
                                        print(error.errorCodes().ERROR0001)
                                        break

                                    else:
                                        CURLINES = 0
                                        print("[i] Deleting note #" + str(del_line))
                                        print("    Please don't interrupt the process or notes may be lost...\n")
                                        try:
                                            open(notes, 'r').read()
                                            open(notes, 'r').close()

                                        except(IOError, EOFError, FileNotFoundError):
                                            print(error.errorCodes().ERROR0019)
                                            pass

                                        os.remove(notes)
                                        with open(notes, 'a') as fopen:
                                            """
                                            while CURLINES < len(notes_data):
                                                if CURLINES == (del_line - 1):
                                                    CURLINES += 1

                                                else:
                                                    fopen.write(notes_data[(CURLINES - 1)])
                                                    CURLINES += 1
                                            """
                                            for note in notes_data:
                                                CURLINES += 1
                                                if CURLINES == del_line:
                                                    continue

                                                else:
                                                    fopen.write(note)

                                        print("[i] Note successfully removed!")
                                break

                            except(ValueError, TypeError):
                                recent_exceptions = traceback.format_exc()
                                print(error.errorCodes().ERROR0001)
                                break

                    else:
                        raise IndexError

                except IndexError:
                #except ImportError: # DEV0005
                    print()
                    print("[i] Usage: notepad [OPTION] NOTE")
                    print()
                    print("add || new :: add a new note.")
                    print("show || ls :: list notes.")
                    print("rm || del  :: delete a note.")
                    print()

            elif menu_input.lower().startswith(("clear", "clr", "cls", "clrscrn")):
                misc.programFunctions().clrscrn()

            elif menu_input.lower().startswith("run") or menu_input.lower().startswith('exec'):
                try:
                    run_o = menu_input.split(' ')
                    run_o[0] = ''
                    command = ''
                    index_error = False
                    for args in run_o:
                        command += str(args) + ' '

                    #print('|', command, '|') # DEV0005: For debugging purposes only
                    if command == (None or '' or ' '):
                        raise IndexError

                    else:
                        logger.log(3, 'User run the command: "' + command + '".', 'logfile.txt', global_variables['SESSION_ID'])
                        system_call_error_code = os.system(command)
                        print(misc.CGR + "[i] process returned error code " + str(system_call_error_code) + '\n' + misc.END)

                except IndexError:
                    print()
                    print("Usage: run [COMAMND] || exec [COMMAND]")
                    print()
                    print("Example: run ls")
                    print("         exec ls")
                    print()

            elif menu_input.lower() in ["netifaces"]:
                if misc.programFunctions().is_windows():
                    success = os.system("ipconfig /all")
                    if success != 0:
                        print(error.errorCodes().ERROR0020("Process returned error code" + str(success)))

                    else:
                        pass

                else:
                    success = os.system("ifconfig -a -s")
                    if success != 0:
                        print(error.errorCodes().ERROR0020("Process returned error code " + str(success) + '.'))

                    else:
                        pass

            elif menu_input.lower().startswith("trace"):
                try:
                    trace_o = menu_input.split(' ')
                    if misc.programFunctions().is_windows():
                        os.system("tracert /b " + trace_o[1]) # DEV0001: must be tested on a windows system!

                    else:
                        os.system("traceroute -b " + trace_o[1])

                except(KeyboardInterrupt, EOFError):
                    pass

                except IndexError:
                    print()
                    print("Usage: trace [IP/HOSTNAME]")
                    print()

            elif menu_input in ["back"]:
                logger.log(2, "ERROR 0004: Back cannot be used in the main module", 'logfile.txt', global_variables['SESSION_ID'])
                print(error.errorCodes().ERROR0004)

            elif menu_input == "THIS":
                print("\n\n")
                import this # No 'Easter egg' here! Go away!!!...
                print("\n\n")

            elif menu_input.startswith("SH4D0WT34MDEVS"):
                # Again, No 'Easter egg' here!
                try:
                    shadow_o = menu_input.split(" ")
                    if shadow_o[1] == "modules":
                        for modules in sys.modules:
                            print("- " + modules)
                            time.sleep(0.001)

                    elif shadow_o[1] == "test":
                        if shadow_o[2] == "multitasking":
                            try:
                                if shadow_o[3] == "no_sleep":
                                    no_sleep = True

                                else:
                                    no_sleep = False

                            except IndexError:
                                no_sleep = False

                            @multitasking.task
                            def test_thread(i, no_sleep):
                                if no_sleep:
                                    o = 0

                                else:
                                    o = random.randint(1, 10) / 2

                                print("Task #" + str(i) + " started, sleeping for " + str(o) + "...")
                                time.sleep(o)
                                print("Task #" + str(i) + " finished...")

                            for i in range(0, 10):
                                test_thread(i, no_sleep)

                            del test_thread
                            del no_sleep

                            time.sleep(10)

                    elif shadow_o[1] == "show":
                        if shadow_o[2] == "multitasking":
                            print(multitasking)
                            for i in multitasking.config:
                                print(str(i) + ": " + str(multitasking.config[i]) + '\n')

                    else:
                        raise IndexError

                    del shadow_o

                except IndexError:
                    proper_exit(999)

            elif menu_input in ["restart", "reboot"]:
                logger.log(0, 'User restarted Shadow Suite...', 'logfile.txt', global_variables['SESSION_ID'])
                misc.programFunctions().clrscrn()
                misc.programFunctions().program_restart()

            elif menu_input in ["quit", "exit"]:
                print(misc.programFunctions().random_color() + joke.joke() + misc.END)
                print(misc.FB + misc.CLR + "Quitting Shadow Suite...\n" + misc.END)
                logger.log(0, 'User quits Shadow Suite...', 'logfile.txt', global_variables['SESSION_ID'])
                proper_exit(0)

            else:
                logger.log(2, 'ERROR 0001: Invalid Input', 'logfile.txt', global_variables['SESSION_ID'])
                print(error.errorCodes().ERROR0001)

        except KeyboardInterrupt:
            #print(len(active_services)) # DEV0005: For debugging purposes only
            if len(active_services) != 0:
                print(error.warningCodes().WARNING0006)
                logger.log(1, 'CTRL+C Detected, Stopping active services...', 'logfile.txt', global_variables['SESSION_ID'])
                kill_all_active_services()

            else:
                logger.log(1, 'CTRL+C Detected, Stopping SSF...', 'logfile.txt', global_variables['SESSION_ID'])
                print(error.errorCodes().ERROR0002)
                proper_exit(2)

        except ImportError:
            recent_exceptions = traceback.format_exc()
            # This function is called if a module was missing.
            cr = '\033[31m'
            cw = '\033[0m'
            print(cr + "ERROR 0008: A module is missing!\nPlease re-install/re-download Shadow Suite to continue..." + cw)
            print("==================== TRACEBACK ====================")
            traceback.print_exc()
            print("===================================================")
            logger.log(5, 'ImportError catched.', 'logfile.txt', global_variables['SESSION_ID'])

            proper_exit(8)

        except Exception as exceptionmessage:
            recent_exceptions = traceback.format_exc()
            print(error.warningCodes().WARNING0003)
            print("[i] " + str(exceptionmessage))
            print()
            print("==================== TRACEBACK ====================")
            traceback.print_exc()
            print("===================================================")
            print()
            quit = misc.programFunctions().error_except()
            if quit == True:
                proper_exit(0)

            elif quit == False:
                pass

            else:
                ValueError_msg = "ValueError: quit variable must be a boolean (True or False)."
                print(ValueError_msg)
                logger.log(0, ValueError_msg, 'logfile.txt', global_variables['SESSION_ID'])
                proper_exit(0)

def no_escape_chars(string):
    result = string.replace('\n', '').replace('\t', '')
    return result

def default_completer(*ignored):
    return []

def complete(text, state):
    """Return the next possible completion for 'text'.

    If a command has not been entered, then complete against command list.
    Otherwise try to call complete_<command> to get list of completions.
    """
    if state == 0:
        original_line = readline.get_line_buffer()
        line = original_line.lstrip()
        stripped = len(original_line) - len(line)
        start_index = readline.get_begidx() - stripped
        end_index = readline.get_endidx() - stripped

        if start_index > 0:
            cmd, args = parse_line(line)
            if cmd == "":
                complete_function = default_completer
            else:
                try:
                    complete_function = getattr("complete_" + cmd)
                except AttributeError:
                    complete_function = default_completer
        else:
            complete_function = raw_command_completer

        completion_matches = complete_function(text, line, start_index, end_index)

    try:
        return self.completion_matches[state]

    except IndexError:
        return None

def raw_command_completer(self, text, line, start_index, end_index):
    """ Complete command w/o any argument """
    return [command for command in suggested_commands() if command.startswith(text)]

def suggested_commands():
	return commands()

def commands(*ignored):
    return [command.rsplit("_").pop() for command in dir(self) if command.startswith("command_")]

def parse_line(line):
        """ Split line into command and argument.

        :param line: line to parse
        :return: (command, argument)
        """
        command, _, arg = line.strip().partition(" ")
        return command, arg.strip()

def service_importlib(service_name, mode='start'):
    global active_services
    try:
        if mode == 'start':
            try:
                serv_start(service_name)

            except Exception as e:
                print(error.errorCodes().ERROR0020(str(e)))

            else:
                active_services.append(service_name)

            time.sleep(5)

        elif mode == 'stop':
            # DEV0001: The program quits when iservice.stop_service() is called.
            print(misc.CGR + "[" + service_name + "] Stopping service...")
            iservice = importlib.import_module(service_name)
            iservice.stop_service()
            print(misc.CGR + "[" + service_name + "] Stopping service... Done!")

        elif mode == 'info':
            iservice = importlib.import_module(service_name)
            iservice.service_info()

        elif mode == 'reload':
            """
            print(misc.CGR + "[" + service_name + "] Reloading service...")
            iservice = importlib.reload(importlib.import_module(service_name))
            print(misc.CGR + "[" + service_name + "] Reloading service... Done!")
            time.sleep(0.50)
            """
            pass

        else:
            raise ValueError("Parameter mode must be 'start', 'stop', 'info', or 'reload'!")

    except Exception as service_err:
        print(error.errorCodes().ERROR0020(str(service_err)))

@multitasking.task
def serv_start(service_name):
    print(misc.CGR + "[" + service_name + "] Starting service...")
    iservice = importlib.import_module(service_name)
    iservice.main(global_variables)

def proper_exit(code):
    # Step 1: Deletes the file.
    try:
        os.remove('.last_session_exit_fail.log') # Delete the file

    except:
        pass

    # Step 2: Sets title to None.
    if misc.programFunctions().is_windows():
        pass

    else:
        print(ansi.set_title(''))

    # Step 3: Logs the exit
    try:
        logger.log(4, "SystemExit raised with error code " + str(code) + ".", 'logfile.txt', global_variables['SESSION_ID'])

    except:
        logger.log(4, "SystemExit raised with error code " + str(code) + ".", 'logfile.txt')

    # Step 4: Kills all threads. Services and some modules uses and quit.
    try:
        sys.exit(code)

    except SystemExit:
        os._exit(code)

def kill_all_active_services():
    print(misc.CY, "[i] Not yet implemented! Please quit SSF to stop all services.", misc.END)

def is_libedit():
    return "libedit" in readline.__doc__

def first_run_wizard():
    while True:
        misc.programFunctions().clrscrn()
        print(misc.FB + misc.CG + misc.LOGO + misc.CW + misc.FR)
        print()
        print(misc.CG + "\t\t\tFirst-run Wizard" + misc.CW)
        print()
        print(misc.FI + misc.CGR + misc.BRIEF_LICENSE + misc.CW + misc.FR)
        print()
        print("[R] Read the full version of the license")
        print("[Q] Quit Shadow Suite Framework")
        print()
        list_of_captcha_strings = ['i agree', 'i do', 'i accept', 'i\'ll follow the rules']
        captcha_string = misc.programFunctions().captcha_picker(list_of_captcha_strings)
        print("If you accept and will follow the rules of the license, type '" + captcha_string + "'.")
        captcha_confirm = input(" > ")
        if captcha_confirm.lower() == 'r' or captcha_confirm.lower() == 'read' or 'license' in captcha_confirm.lower():
            if global_variables['PLATFORM'] == 'windows' or global_variables['PLATFORM'] == 'nt':
                os.system("start extras/shadowsuitelicense")

            else:
                os.system("less extras/shadowsuitelicense")

            logger.log(0, "User read the license.", 'logfile.txt', global_variables['SESSION_ID'])
            continue

        elif captcha_confirm.lower() == captcha_string:
            print(misc.FB + misc.CG + "[i] Thank you for downloading Shadow Suite Framework! :D " + misc.FR + misc.CW)
            logger.log(0, "User accepted the agreement!", 'logfile.txt', global_variables['SESSION_ID'])
            misc.programFunctions().pause()
            pass

        elif captcha_confirm.lower() == 'q' or captcha_confirm.lower() == 'quit':
            print(misc.FB + misc.CR + "\n[i] Thank you for downloading Shadow Suite Framework...")
            print(misc.FR + "\n\tIf you are unsatisfied about this project,\n\t\tplease contact us and\n\twe will try our best to make you satisfied :)\n" + misc.CW)
            logger.log(0, "User choosed to not accept the license and quit.", 'logfile.txt', global_variables['SESSION_ID'])
            proper_exit(0)

        else:
            continue

        misc.programFunctions().clrscrn()
        print(misc.FB + misc.CG + misc.LOGO + misc.CW + misc.FR)
        print()
        print(misc.CG + "\t\t\tFirst-run Wizard" + misc.CW)
        while True:
            askuser_fullupdate = input(misc.FB + misc.CGR + "Do you want to perform a full update? (y/n) > " + misc.CW + misc.FR)
            if askuser_fullupdate.lower() in ('yes' or 'y'):
                logger.log(0, "User performed a full update.", 'logfile.txt', global_variables['SESSION_ID'])
                update.full_update(global_variables['DEBUGGING'])
                break

            elif askuser_fullupdate.lower() in ('no' or 'n'):
                logger.log(1, "User did not performed a full update.", 'logfile.txt', global_variables['SESSION_ID'])
                break

            else:
                continue

        print("[i] Just press enter if you don't want to use password protection.")
        while True:
            askuser_username = input("[i] Username: ")
            if askuser_username == None or askuser_username == "":
                pass

            else:
                hashed_username = misc.programFunctions().hash(askuser_username, 'sha256')
                global_variables['USERNAME'] = hashed_username
                global_variables['current_user'] = askuser_username

            while True:
                askuser_userpass1 = getpass("[i] Userpass: ")
                if askuser_userpass1 == None or askuser_userpass1 == "":
                    break

                else:
                    askuser_userpass2 = getpass("[i] Confirm Userpass: ")
                    if askuser_userpass1 == askuser_userpass2:
                        global_variables['USERPASS'] = misc.programFunctions().hash(askuser_userpass1, 'sha256')
                        break

                    else:
                        continue

            askuser_rootname = input("[i] Rootname: ")
            if askuser_rootname == None or askuser_rootname == "":
                pass

            else:
                hashed_rootname = misc.programFunctions().hash(askuser_rootname, 'sha256')
                global_variables['ROOTNAME'] = hashed_rootname

            while True:
                askuser_rootpass1 = getpass("[i] Rootpass: ")
                if askuser_rootpass1 == None or askuser_rootpass1 == "":
                    pass

                else:
                    askuser_rootpass2 = getpass("[i] Confirm Rootpass: ")
                    if askuser_rootpass1 == askuser_rootpass2:
                        global_variables['ROOTPASS'] = misc.programFunctions().hash(askuser_rootpass1, 'sha256')
                        break

                    else:
                        continue

                break

            break

        while True:
            askuser_binary_path = input("Binary path (Usually '/usr/bin/'): ")
            if misc.programFunctions().path_exists(askuser_binary_path):
                if not askuser_binary_path.endswith('/'):
                    askuser_binary_path += '/'

                global_variables['BINARY_PATH'] = askuser_binary_path
                break

            else:
                print(error.errorCodes().ERROR0015)
                continue

        logger.log(0, "Updating configuration file data...", 'logfile.txt', global_variables['SESSION_ID'])
        config_dict = {
                "username": global_variables['USERNAME'],
                "userpass": global_variables['USERPASS'],
                "rootname": global_variables['ROOTNAME'],
                "rootpass": global_variables['ROOTPASS'],
                "module_path": global_variables['MODULE_PATH'],
                "services_path": global_variables['SERVICES_PATH'],
                "output_path": global_variables['OUTPUT_PATH'],
                "binary_path": global_variables['BINARY_PATH']
                }

        export_conf_result = API.ShadowSuite(global_variables['current_user'], global_variables['MODULE_PATH'], global_variables['OUTPUT_PATH'], global_variables['SESSION_ID'], global_variables['USERLEVEL'], global_variables['DEBUGGING']).export_conf(global_variables['config_file'], config_dict)

        logger.log(0, "Deleting First-run Wizard variables...", 'logfile.txt', global_variables['SESSION_ID'])
        del askuser_fullupdate
        del askuser_username
        del askuser_userpass1
        try:
            del askuser_userpass2

        except UnboundLocalError:
            pass

        del askuser_rootname
        del askuser_rootpass1
        try:
            del askuser_rootpass2

        except UnboundLocalError:
            pass

        del askuser_binary_path

        logger.log(0, "Writing to \"data/.installed.dat\" file...", 'logfile.txt', global_variables['SESSION_ID'])
        open('data/.installed.dat', 'w').write('')
        open('data/.installed.dat', 'w').close()
        misc.programFunctions().clrscrn()
        #print(config_dict) # DEV0005
        #print(global_variables) # DEV0005
        break


"""
class debug:

    def __init__(self):
        pass

    def print_log(self, error_code, log):
        pass

"""

# Starts the program
if __name__ == "__main__":
	main()
