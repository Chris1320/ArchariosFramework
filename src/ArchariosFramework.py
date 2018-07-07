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
    import atexit
    import signal
    import readline
    import traceback
    import subprocess

    # Import core libraries
    from core import ansi
    from core import misc
    from core import error
    from core import tests
    from core import cowsay
    from core import logger
    from core import matrix
    from core import gethost
    from core import printer
    from core import exceptions
    from core import asciigraphs
    from core import touchingsky
    from core import random_phrases
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

    def __init__(self, **kwargs):
        """
        def __init__():
            Initialization method for ArchariosFramework() class.
        """

        # Create and start logging object
        self.logger = logger.LoggingObject(
                name='ArchariosFramework',
                logfile='data/logfile.log'
                )
        self.logger.set_logging_level('NOTSET')

        # Program Information
        self.logger.info('Defining program information.')
        self.name = "Archários Framework"
        self.version = "0.0.0.4"
        self.codename = "Alpha"
        self.description = "The Novice's Ethical Hacking Framework"
        self.banner = r"""{0}
   _          _     {3}/\/|{0}     _            ___                                  _
  /_\  _ _ __| |_  {3}|/\/{0} __ _(_)___ ___   | __| _ __ _ _ __  _____ __ _____ _ _| |__
 / _ \| '_/ _| ' \ {3}/--\{0} | '_| / _ (_-<   | _| '_/ _` | '  \/ -_) V  V / _ \ '_| / /
/_/ \_\_| \__|_||_{3}/_/\_\{0}|_| |_\___/__/   |_||_| \__,_|_|_|_\___|\_/\_/\___/_| |_\_\
              {5}{3}{1} {4}{7}v{5}{6}{2} {8}{9}{4}
""".format(misc.CB,
        self.description,
        self.version,
        misc.CY,
        misc.END,
        misc.FB,
        misc.CC,
        misc.CGR,
        misc.CR,
        self.codename)
        self.logger.info("Program Information: {0} v{1}".format(self.name,
            self.version))

        # Parse command-line parameters..
        self.logger.info("Parsing command-line parameters/arguments.")
        kwargs_to_pop = []
        for kwarg in kwargs:
            if kwargs[kwarg] is None:
                self.logger.info("{0} is None, deleting key.".format(
                    kwarg
                    ))
                kwargs_to_pop.append(kwarg)  # Remove all keys with value None.

            else:
                continue

        self.logger.info("Keyword arguments to pop: {0}".format(
            str(kwargs_to_pop)
            ))

        for kwarg in kwargs_to_pop:
            self.logger.info("Popping {0} from kwargs.".format(str(kwarg)))
            kwargs.pop(kwarg)

        del kwargs_to_pop

        self.logger.info("Getting configuration file...")
        self.config_file = kwargs.get('config_file',
                'data/default.dat')  # Get config file.
        self.logger.info("Config file used: {0}".format(self.config_file))
        self.logger.info("Checking if debug is True...")
        if kwargs.get('debug', False) is True:  # Enable debugging.
            self.logger.info("Debug is True, showing logs...")
            self.logger.enable_logging()
            self.logger.info("Debugging started.")

        # Environment Information
        self.logger.info("Getting environment information.")
        self.filename = misc.ProgramFunctions().get_program_filename(
                sys.argv[0])
        self.logger.info("Program current filename: {0}".format(
            self.filename))
        self.is_windows = misc.ProgramFunctions().is_windows()
        self.platform = misc.ProgramFunctions().get_platform()
        self.logger.info("Is windows: {0}    Platform: {1}".format(
            str(self.is_windows), self.platform
            ))

        # Network Information
        self.logger.info("Getting network information...")
        self.hostname = gethost.current()
        self.logger.info("Current Hostname: {0}".format(self.hostname))

        # Default interactive mode environment.
        self.logger.info("Setting default interactive mode environment.")
        self.userlevel = misc.ProgramFunctions().geteuid()
        self.logger.info("Userlevel: {0}".format(str(self.userlevel)))
        if self.userlevel != 0:
            self.userlevel = 3

        else:
            pass
        self.prompt_lvl3 = '[{0}{1}{2}@{3}{4}{2}] >>> '.format(
                misc.CG, self.filename, misc.END,
                misc.CC, self.hostname
                )
        self.prompt_lvl2 = '[{0}{1}{2}@{3}{4}{2}] $: '.format(
                misc.CG, self.filename, misc.END,
                misc.CC, self.hostname
                )

        self.prompt_lvl1 = '[{0}{1}{2}@{3}{4}{2}] #: '.format(
                misc.CG, self.filename, misc.END,
                misc.CC, self.hostname
                )

        self.latest_exceptions = traceback.format_exc()

        # Setup interpreter history
        self.logger.info("Setting up interpreter history...")
        self.history_file = "data/history.log"
        self.history_length = 100
        self._set_interpreter_history()

        # Parse configuration file.
        self.logger.info("Parsing configuration file `{0}`.".format(
            self.config_file))
        self._parse_config()

        # Set terminal title.
        ansi.set_title("{0} v{1}".format(self.name, self.version))

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
                "USAGE: {0} [SWITCHES]".format(self.filename),
                "",
                "SWITCHES:",
                "    Debugging Seitches:",
                "        Switch: -t --test /t /test",
                "        Desc..: Test for errors and then exit.",
                "",
                "        Switch: -d --debug /d /debug",
                "        Desc..: Enable debugging mode; Show logs.",
                "",
                "    Miscellaneous Switches:",
                "        Switch: -h --help -? /h /help /?",
                "        Desc..: Show this help menu.",
                "",
                "NOTE: Running {0} without any arguments \
will use the default settings.".format(self.name),
                "",
                "",
                "INTERACTIVE MODE COMMANDS:",
                "",
                "help                  Show this help menu.",
                "run exec [COMMAND]    Pass <command> to the shell.",
                "restart reboot        Restart {0}.".format(self.name),
                "quit exit             Exit {0}.".format(self.name)
                ]

        self.logger.info("Return type recieved: {0}".format(rtype))
        if rtype.lower() == "default":
            result = ""
            self.logger.info("Converting list to string...")
            for line in help_lines:
                result += (line + '\n')

            return result

        elif rtype.lower() == "list":
            result = help_lines
            self.logger.info("Returning list...")
            return result

        else:
            self.latest_exceptions = traceback.format_exc()
            self.logger.error("Cannot identify what `{0}` means.".format(rtype))
            raise exceptions.InvalidParameterError("Unknown parameter passed! Must be `default` or `list`.")

    def _set_interpreter_history(self):
        """
        def _set_interpreter_history():
            Initialization of third-party libraries

            Setting interpreter history and
            setting appropriate completer function.
        """

        self.logger.info("Checking if `{0}` exists.".format(self.history_file))
        if not os.path.exists(self.history_file):
            self.logger.info("{0} doesn't exist, creating file.".format(
                self.history_file
                ))
            with open(self.history_file, "a") as history:
                if "libedit" in readline.__doc__:
                    self.logger.info("Writing to history.")
                    history.write("_HiStOrY_V2_\n\n")

        self.logger.info("Reading history file.")
        readline.read_history_file(self.history_file)
        self.logger.info("Setting history length.")
        readline.set_history_length(self.history_length)
        self.logger.info("Registering readline command at exit.")
        atexit.register(readline.write_history_file, self.history_file)

        readline.parse_and_bind("set enable-keypad on")

        self.logger.info("Setting up completion.")
        readline.set_completer(self._complete)
        readline.set_completer_delims(" \t\n;")
        if "libedit" in readline.__doc__:
            readline.parse_and_bind("bind ^I rl_complete")

        else:
            readline.parse_and_bind("tab: complete")

        return 0

    def _complete(self, text, state):
        """
        def _complete():
            Return the next possible completion for 'text'.

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
                cmd, args = self.parse_line(line)
                if cmd == "":
                    complete_function = self.default_completer

                else:
                    try:
                        complete_function = getattr(self, "complete_" + cmd)

                    except AttributeError:
                        complete_function = self.default_completer

            else:
                complete_function = self.raw_command_completer

            self.completion_matches = complete_function(text, line,
                    start_index, end_index)

        try:
            return self.completion_matches[state]

        except IndexError:
            return None

    def _parse_config(self):
        """
        def _parse_config():
            Parse configuration file.
        """

        try:
            self.logger.info("Reading {0}...".format(self.config_file))
            with open(self.config_file) as conf:
                conf_data = conf.readlines()

            for data in conf_data:
                if data.startswith('#'):
                    continue

                else:
                    continue

        except(FileNotFoundError):
            self.latest_exceptions = traceback.format_exc()
            self.logger.error("{0} was not found.".format(self.config_file))
            printer.Printer().print_with_status(str(
                error.ErrorClass().ERROR0001(self.config_file)), 2)
            self._proper_exit(1)

    def _proper_exit(self, exit_code=0):
        if exit_code == 0:
            self.logger.info("SystemExit raised with error code `{0}`.".format(
                str(exit_code)))

        else:
            self.logger.warning("SystemExit raised with error code `{0}`.".format(
                str(exit_code)))

        ansi.set_title("")
        sys.exit(exit_code)

    def console(self):
        """
        def console():
            Enter interactive mode.
        """

        self.logger.info("Starting interactive terminal...")
        print('\n' * 5)
        print(self.banner)
        print()
        print(misc.FB + misc.FI + misc.ProgramFunctions().random_color() +
                random_phrases.phrases() + misc.END)
        print()
        print("{0}[{1}i{0}] {2}Type '{3}help{2}' for more information.\
                {4}".format(misc.CGR, misc.CC, misc.CB, misc.CC, misc.END))
        print()
        self.logger.info("Starting while loop...")
        while True:
            try:
                self.logger.info("Running {0} with userlevel of {1}.".format(
                    self.name, self.userlevel
                    ))
                if self.userlevel == 3:
                    self.command = input(self.prompt_lvl3)

                elif self.userlevel == 2:
                    self.command = input(self.prompt_lvl2)

                elif self.userlevel == 1:
                    self.command = input(self.prompt_lvl1)

                else:
                    raise exceptions.UnknownUserLevelError("There is a problem obtaining the userlevel.")

                self.parse_input(self.command)

            except(KeyboardInterrupt):
                self.latest_exceptions = traceback.format_exc()
                printer.Printer().print_with_status(str(
                    error.ErrorClass().ERROR0002()), 2)
                self.logger.warning(error.ErrorClass().ERROR0002())
                self._proper_exit(2)

            except(EOFError):
                print()
                print("No options yet!")  # DEV0004
                print()

    def parse_input(self, command='help'):
        self.logger.info("Command recieved: `{0}`".format(command))
        if command.lower() in ('help', '?'):
            self.logger.info("Printing help menu.")
            print(self.help())

        elif command.lower().startswith('show'):
            command = command.lower().partition(' ')[2]
            if command in ('traceback', 'tracebacks'):
                print()
                print("{0}{1}{2}{3} Latest Exceptions {3}{4}".format(
                    misc.FB, misc.FI, misc.CC, ('=' * 25),
                    misc.END
                    ))
                print()
                print(self.latest_exceptions)
                print()
                print("{0}{1}{2}{3} Latest Exceptions {3}{4}".format(
                    misc.FB, misc.FI, misc.CC, ('=' * 25),
                    misc.END
                    ))
                print()

        elif command.lower().startswith(('run', 'exec')):
            command = command.partition(' ')[2]
            self.logger.info("Running command `{0}`...".format(
                command
                ))
            try:
                if command == '':
                    raise exceptions.InvalidCommandError("Command must not be NoneType!")

                else:
                    print()
                    # subprocess.call(command)  # DEV0004: Use subprocess
                    os.system(command)
                    print()

            except(PermissionError, OSError):
                self.latest_exceptions = traceback.format_exc()
                printer.Printer().print_with_status(str(
                    error.ErrorClass().ERROR0004('command')), 2)

            except Exception as err:
                self.latest_exceptions = traceback.format_exc()
                printer.Printer().print_with_status(str(err), 2)

        elif command.lower() in ('restart', 'reboot'):
            self.logger.info("Restarting...")
            asciigraphs.ASCIIGraphs().animated_loading_screen(5,
                    "Restarting {0}...".format(self.name),
                    'swapcase',
                    0.10
                    )
            misc.ProgramFunctions().clrscrn()
            misc.ProgramFunctions().program_restart()

        elif command.lower() in ('quit', 'exit'):
            self._proper_exit(0)

        else:
            self.latest_exceptions = traceback.format_exc()
            printer.Printer().print_with_status(str(
                error.ErrorClass().ERROR0003(command)), 2)
            self.logger.error("Unknown or invalid input recieved: {0}".format(
                command))
            print("{0} Type '{1}help{0}' for more information.{2}".format(
                misc.CR, misc.CC, misc.END
                ))


# If running independently, run main() function.
if __name__ == '__main__':
    oconfig_file = None
    odebug = None

    _iterator = 1  # Skip the filename.
    while _iterator < len(sys.argv):
        arg = sys.argv[_iterator]

        if arg.lower() in ('-h', '--help', '-?', '/h', '/help', '/?'):
            print(ArchariosFramework().banner)
            print(ArchariosFramework().help())
            ArchariosFramework()._proper_exit(0)

        elif arg.lower() in ('-t', '--test', '/t', '/test'):
            try:
                print(ArchariosFramework().banner)
                print()
                test_result = tests.TestingClass(ArchariosFramework().name).main()
                if test_result == 0:
                    print("{0}[{1}i{0}] {2}No problems found!{3}".format(
                        misc.CGR, misc.CY, misc.CG, misc.END))

                else:
                    print("{0}[{1}i{0}] {2}Problems found! Please examine \
the traceback on `data/tracebacks.log` and/or inform us about what is it\
 about.{3}".format(misc.CGR, misc.CY, misc.CR, misc.END))

                ArchariosFramework()._proper_exit(test_result)

            except(KeyboardInterrupt, EOFError, SystemExit):
                ArchariosFramework()._proper_exit(0)

        elif arg.lower() in ('-d', '--debug', '/d', '/debug'):
            odebug = True

        else:
            print(ArchariosFramework().banner)
            print()
            print('Unknown argument `{0}`'.format(arg))
            print()
            print(ArchariosFramework().help())
            ArchariosFramework()._proper_exit(1)

        _iterator += 1

    ArchariosFramework(
            config_file=oconfig_file,
            debug=odebug
            ).console()
