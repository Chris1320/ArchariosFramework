#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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
    import time
    import atexit
    import random
    import signal
    import readline
    import importlib
    import traceback
    import subprocess
    import multitasking

    # Import third-party library to host web-interface.
    from flask import request as flask_request
    from flask import Flask, render_template
    from flask import session, redirect, url_for
    from flask import escape, make_response
    # from flask import abort as flask_abort    For fatal errors
    from flask_admin import Admin
    from flask_limiter import Limiter
    from flask_limiter.util import get_remote_address
    from flask_wtf.csrf import CSRFProtect, CSRFError

    # Import core libraries
    from core import ansi
    from core import misc
    from core import error
    from core import tests
    from core import cowsay
    from core import logger
    from core import gethost
    from core import printer
    from core import exceptions
    from core import asciigraphs
    from core import random_phrases
    from core import html_downloader

except ImportError as i:
    # Prints if error is encountered while importing modules.
    print("Error: " + str(i))
    print("")
    print("==================== TRACEBACK ====================")
    traceback.print_exc()
    print("===================================================")
    sys.exit(1)

else:
    # Changes the print function into printer.
    # print = printer.Printer().printt
    pass

# ++++++++++++++++++++ WEB INTERFACE ++++++++++++++++++++ #

# Initialize flask framework for web interface.
web_app = Flask(__name__)
web_app.secret_key = random._urandom(2048)  # Generate a random key.
web_limiter = Limiter(
               web_app,
               key_func=get_remote_address,
               default_limits=["1 per second"],
           )
web_csrf = CSRFProtect()
web_csrf.init_app(web_app)

# Error Handlers #


@web_app.errorhandler(CSRFError)
def web_csrferror(*args):
    return render_template('error.html', title=__name__,
            desc=args[0].description), 400


@web_app.errorhandler(400)
def web_misunderstood(*args):
    return render_template('error.html', title=__name__, desc="Whaaat?!? I can't \
 understand the request your browser (or proxy) has sent."), 400


@web_app.errorhandler(404)
def web_not_found(*args):
    return render_template('error.html', title=__name__, desc='The URL you requested \
was not found. Please check the URL.'), 404


@web_app.errorhandler(403)
def web_forbidden(*args):
    return render_template('error.html', title=__name__, desc="Sorry! You're not \
allowed to enter."), 403


@web_app.errorhandler(410)
def web_gone(*args):
    return render_template('error.html', title=__name__, desc="Oops! The page here \
has been gone!"), 410


@web_app.errorhandler(429)
def web_too_many_requests(*args):
    return render_template('error.html', title=__name__, desc="Beyond the limits... \
This page lets you request {0}. Please wait until you are good to go!".format(
    str(args[0]).replace('429 Too Many Requests: ', '')))


@web_app.errorhandler(500)
def web_internal_server(*args):
    return render_template('error.html', title=__name__, desc="It's my fault! \
Something's happening in the servers..."), 500

# Routes #


@web_app.route("/", methods=['GET', 'POST'])
@web_limiter.limit('1 per second')
def web_interface():
    return render_template("index.html", title=ArchariosFramework().name,
            description=ArchariosFramework().description)

@web_app.route("/status", methods=['GET', 'POST'])
@web_limiter.limit('1 per second')
def web_server_status():
    return render_template("server_status.html",
            title=ArchariosFramework().name,
            name=ArchariosFramework().name,
            version=ArchariosFramework().version,
            codename=ArchariosFramework().codename,
            description=ArchariosFramework().description,
            config_file=ArchariosFramework().config_file,
            debugging=ArchariosFramework().debug,
            userlevel=ArchariosFramework().userlevel)

# ++++++++++++++++++++ WEB INTERFACE ++++++++++++++++++++ #


@multitasking.task
def web_run(port, debug):
    """
    def web_run():
        Run the server.
    """

    # TODO: DEV0004: Use a production WSGI server instead.

    if type(port) is tuple or type(port) is list:
        for prt in port:
            try:
                # web_app.run('0.0.0.0', prt, debug)
                web_app.run('0.0.0.0', prt)

            except PermissionError:
                erred = True
                continue

            else:
                erred = False
                break

        if erred is True:
            printer.Printer().print_with_status("Cannot bind to {0}:{1}!\
".format('0.0.0.0', prt), 2)
            ArchariosFramework(from_API=True)._proper_exit(256)

        del erred

    else:
        try:
            # web_app.run('0.0.0.0', prt, debug)
            web_app.run('0.0.0.0', prt)

        except PermissionError:
            printer.Printer().print_with_status("Cannot bind to {0}:{1}!\
".format('0.0.0.0', prt), 2)
            ArchariosFramework(from_API=True)._proper_exit(256)


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

        # Check if called as an API or not.
        self.from_API = bool(kwargs.get('API', False))

        # Create and start logging object
        self.logger = logger.LoggingObject(
                name='ArchariosFramework',
                logfile='data/logfile.log'
                )
        self.logger.set_logging_level('NOTSET')

        # Program Information
        self.logger.info('Defining program information.')
        # self.name = "Archários Framework"
        self.name = "Archarios Framework"
        self.version = "0.0.1.9"
        self.codename = "Beta"
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
        self.debug = kwargs.get('debug', False)
        if self.debug is True:  # Enable debugging.
            self.logger.info("Debug is True, showing logs...")
            self.logger.enable_logging()
            self.logger.info("Debugging started.")

        self.logger.info("Checking if web interface is True...")
        self.web = kwargs.get('web', False)
        if self.web is True:
            web_run((80, 8000, 8080, 5000), self.debug)

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

        self.prompt_lvl3 = "[" + misc.CG + self.filename + misc.END + '@' +\
        misc.CC + "{0}" + misc.END + "] >>> "

        self.prompt_lvl2 = "[" + misc.CG + self.filename + misc.END + '@' +\
        misc.CC + "{0}" + misc.END + "] $: "

        self.prompt_lvl1 = "[" + misc.CG + self.filename + misc.END + '@' +\
        misc.CC + "{0}" + misc.END + "] #: "

        self.latest_exceptions = traceback.format_exc()
        self.module_call = """ArchariosFrameworkModule(debug=self.debug, \
fname=self.name, fversion=self.version, fcodename=self.codename, \
fdescription=self.description, fbanner=self.banner, \
userlevel=self.userlevel, logger=self.logger, API=self.from_API)"""
        # To be used with `eval()`.

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
                "    Debugging Switches:",
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
                "        Switch: -w --web /w /web",
                # TODO: DEV0004: Remove WIP when finished developing web interface.
                "        Desc..: (WIP) Start {0}'s web interface.".format(self.name),
                "",
                "NOTE: Running {0} without any arguments \
will use the default settings.".format(self.name),
                "",
                "",
                "INTERACTIVE MODE COMMANDS:",
                "",
                "help                  Show this help menu.",
                "show [OPTION]         Show information about <option>.",
                "module [OPTION]       Manage modules. (Type `module ?` for info.)",
                "runpy [COMMAND]       Pass <command> to python shell. ({0}Use AT YOUR OWN RISK{1})".format(misc.FB + misc.CY, misc.END),
                "run exec [COMMAND]    Pass <command> to the shell.",
                "clear cls clr         Clear the current contents of the screen.",
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
            result = [0, help_lines]
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
        """
        def _proper_exit():
            Performs `cleanup` before exit.
        """

        if exit_code == 0:
            self.logger.info("SystemExit raised with error code `{0}`.".format(
                str(exit_code)))

        else:
            self.logger.warning("SystemExit raised with error code `{0}`.".format(
                str(exit_code)))

        ansi.set_title("")
        try:
            sys.exit(exit_code)

        except SystemExit:
            os._exit(exit_code)

    def _import_module(self, module, silent=False):
        """
        def _import_module():
            Import <module> using importlib.
        """

        self.logger.info("Importing {0} via importlib...".format(
            module
            ))
        try:
            module_object = importlib.import_module('modules.' + module)

        except(ImportError, ModuleNotFoundError):
            printer.Printer().print_with_status("Cannot find `{0}` module! Please make sure it is installed and properly configured.".format(module), 2)

        except Exception as err:
            self.latest_exceptions = traceback.format_exc()
            if silent is False:
                printer.Printer().print_with_status(str(err), 2)
                printer.Printer().print_with_status("Use `show tracebacks` \
for more info.", 2)
                self.logger.error("Something wrong happened while importing \
{0}! Error: `{1}`; Returning None.".format(module, str(err)))
                return None

        else:
            self.logger.info("Imported {0}! Returning object...".format(module))
            return module_object

    def _reload_module(self, module):
        """
        def _reload_module():
            Reload <module> using importlib.
        """

        self.logger.info("Reloading {0} via importlib...".format(
            module
            ))
        try:
            module_obj = self._import_module(module)
            module_object = importlib.reload(module_obj)

        except Exception as err:
            self.latest_exceptions = traceback.format_exc()
            printer.Printer().print_with_status(str(err), 2)
            printer.Printer().print_with_status("Use `show tracebacks` \
for more info.", 2)
            self.logger.info("Error while reloading {0}! Error: {1}; \
Reloading None.".format(module, str(err)))
            return None

        else:
            self.logger.info("Reloaded {0}! Returning new object...".format(module))
            return module_object

    def console(self):
        """
        def console():
            Enter interactive mode.
        """

        self.logger.info("Starting interactive terminal...")
        time.sleep(1)
        print('\n' * 5)
        print(self.banner)
        print()
        print(misc.FB + misc.FI + misc.ProgramFunctions().random_color() +
                random_phrases.phrases() + misc.END)
        print()
        print("{0}[{1}i{0}] {2}Type '{3}help{2}' for more information.\
                {4}".format(misc.CGR, misc.CC, misc.CB, misc.CC, misc.END))
        print()
        self.logger.info("Starting loop in terminal...")
        while True:
            try:
                self.logger.info("Running {0} with userlevel of {1}.".format(
                    self.name, self.userlevel
                    ))
                if self.userlevel == 3:
                    self.command = input(self.prompt_lvl3.format(self.hostname))

                elif self.userlevel == 2:
                    self.command = input(self.prompt_lvl2.format(self.hostname))

                elif self.userlevel == 1:
                    self.command = input(self.prompt_lvl1.format(self.hostname))

                else:
                    raise exceptions.UnknownUserLevelError("There is a problem obtaining the userlevel.")

                if ' && ' in self.command:
                    iterator = 0
                    self.command = self.command.split(' && ')
                    for command in self.command:
                        iterator += 1
                        print()
                        print("{0}Command {1}#{2}{3}: {4}".format(
                            misc.CG, misc.CB, str(iterator),
                            misc.END, command
                            ))
                        self.parse_input(command)
                        time.sleep(1)

                else:
                    self.parse_input(self.command)

            except(KeyboardInterrupt):
                self.latest_exceptions = traceback.format_exc()
                printer.Printer().print_with_status(str(
                    error.ErrorClass().ERROR0002()), 2)
                self.logger.warning(error.ErrorClass().ERROR0002())
                self._proper_exit(2)

            except(EOFError):
                self.logger.info("CTRL+D Detected; Showing additional options.")
                print("More Options")
                print()
                print("[01] Standby")
                print("[02] Force Shutdown")
                print()
                print("[99] Back to console")
                print()
                while True:
                    try:
                        ctrl_d_option = int(input(" >>> "))
                        if ctrl_d_option == 1:
                            try:
                                self.logger.info("Standing by...")
                                print(cowsay.cowsay("I'm sleeping, Press \
CTRL+C when you are ready.").replace('(oo)', '(==)'))
                                while True:
                                    time.sleep(60)

                            except(KeyboardInterrupt, EOFError):
                                self.logger.info("Going back to work.")
                                break

                        elif ctrl_d_option == 2:
                            self.logger.critical("Forcing to quit")
                            sys.exit(1024)

                        else:
                            printer.Printer().print_with_status(
                                    "Unknown option!", 2)
                            self.logger.info("Unknown option selected.")
                            continue

                    except(KeyboardInterrupt, EOFError, TypeError, ValueError):
                        self.logger.info("^C/^D detected, continuing loop.")
                        continue

    def parse_input(self, command='help'):
        """
        def parse_input():
            Parse user input.
        """

        self.logger.info("Command recieved: `{0}`".format(command))
        if command.lower() in ('help', '?'):
            self.logger.info("Printing help menu.")
            if self.from_API is not True:
                print(self.help())

            else:
                return self.help('list')

        elif command.lower().startswith('show'):
            command = command.lower().partition(' ')[2]
            self.logger.info("Looking for matches of `{0}`...".format(
                command
                ))
            try:
                if command in ('traceback', 'tracebacks'):
                    self.logger.info("Printing traceback information...")
                    if self.from_API is not True:
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

                    else:
                        return [0, ["{0} Latest Exceptions {0}".format(('=' * 5)),
                        "",
                        self.latest_exceptions,
                        "",
                        "{0} Latest Exceptions {0}".format(('=' * 5))]]

                elif command in ('log_data', 'log_datas'):
                    self.logger.info("Printing log data...")
                    log_data = self.logger.get_all_log_datas()
                    result = ""
                    if self.from_API is not True:
                        result += ("\n" + ("=" * 25) + "LOG DATA" + ("=" * 25) + "\n\n")

                    else:
                        result += ("\n" + ("=" * 5) + "LOG DATA" + ("=" * 5) + "\n\n")

                    for log in log_data:
                        if log[1] == "info":
                            if self.from_API is not True:
                                result += (misc.END + log[0] + '\n')

                            else:
                                result += (log[0] + '\n')

                        elif log[1] == "warning":
                            if self.from_API is not True:
                                result += (misc.CY + log[0] + '\n')

                            else:
                                result += (log[0] + '\n')

                        elif log[1] == "error":
                            if self.from_API is not True:
                                result += (misc.CR + log[0] + '\n')

                            else:
                                result += (log[0] + '\n')

                        elif log[1] == "debug":
                            if self.from_API is not True:
                                result += (misc.CGR + log[0] + '\n')

                            else:
                                result += (log[0] + '\n')

                        elif log[1] == "critical":
                            if self.from_API is not True:
                                result += (misc.FB + misc.CR + log[0] + '\n')

                            else:
                                rrsult += (log[0] + '\n')

                        else:
                            if self.from_API is not True:
                                result += (misc.FB + misc.CGR + log[0] + '\n')

                            else:
                                result += (log[0] + '\n')

                    if self.from_API is not True:
                        result += ("\n" + ("=" * 25) + "LOG DATA" + ("=" * 25) + "\n\n")

                    else:
                        result += ("\n" + ("=" * 5) + "LOG DATA" + ("=" * 5) + "\n\n")

                    if self.from_API is not True:
                        print(result)

                    else:
                        return [0, result.split('\n')]

                else:
                    self.logger.info("`{0}` is an unknown option to `show`.".format(
                        command
                        ))
                    raise IndexError

            except IndexError:
                printer.Printer().print_with_status(
                        "Unknown option: {0}".format(command), 2)
                if self.from_API is not True:
                    print("""
USAGE: show [OPTIONS]

OPTIONS:
    traceback tracebacks    Show the latest traceback information.
    log_data log_datas      Show the log data from the logger module.
""")

                else:
                    return [0, ["", "USAGE: show [OPTIONS]",
                            "", "OPTIONS:",
                            "    traceback tracebacks    Show the latest traceback information.",
                            "    log_data log_datas      Show the log data from the logger module.",
                            ""]]

        elif command.lower().startswith('module'):
            try:
                command = command.split(' ')
                self.logger.info("Looking for matches of `{0}`...".format(
                    command[1]
                    ))
                if command[1] == ('info'):
                    self.logger.info("Importing {0} module...".format(
                        command[2]
                        ))
                    module_obj = self._import_module(command[2])
                    self.logger.info("Checking if importing succeeded...")
                    if module_obj is None:
                        self.logger.error("Importing failed.")
                        return None

                    else:
                        self.logger.info("Importing succeeded; Calling \
show_module_info()...")
                        try:
                            if self.from_API is False:
                                eval("module_obj.{0}.show_module_info()".format(
                                    self.module_call
                                    ))

                            else:
                                return([0, eval("module_obj.{0}.\
show_module_info()".format(self.module_call)).split('\n')])
                                # TODO: Continue API support

                        except(SystemExit):
                            self.logger.info("SystemExit detected from module..")
                            return None

                        except Exception as exception:
                            self.latest_exceptions = traceback.format_exc()
                            self.logger.error("An error occured while using \
the module: `{0}`".format(str(exception)))
                            if self.from_API is False:
                                printer.Printer().print_with_status(
                                    str(exception), 2
                                    )
                                return 1

                            else:
                                return(1, str(exception))

                elif command[1] in ('generate', 'new'):
                    self.logger.info("Creating new custom module...")
                    if self.from_API is not True:
                        print("{0}{1}Create new custom module...{2}".format(
                            misc.FB, misc.CG, misc.END
                            ))

                        while True:
                            try:
                                gen_module_name = input("Module name: ")
                                gen_description = input("Brief Description about \
the module: ")
                                gen_author = input("Module Author's/Your Name: ")
                                self.logger.info("Module name is {0} characters; \
Description is {1} characters; And Author name is {2} characters.".format(
                                            len(gen_module_name),
                                            len(gen_description),
                                            len(gen_author)
                                            ))
                                if len(gen_module_name) > 20 or len(
                                        gen_module_name) < 1:
                                    printer.Printer().print_with_status(
                                            "Module name must be 1-20 characters!",
                                            2
                                            )
                                    continue

                                if len(gen_description) > 100 or len(
                                        gen_description) < 1:
                                    printer.Printer().print_with_status(
                                            "Module's brief description must \
be 1-100 characters!", 2
                                            )
                                    continue

                                if len(gen_author) < 1 or len(gen_author) > 50:
                                    printer.Printer().print_with_status(
                                            "`author` variable must be 1-50 \
characters!", 2
                                            )
                                    continue

                            except(KeyboardInterrupt, EOFError):
                                printer.Printer().print_with_status(
                                        "Module creation cancelled...", 1
                                        )
                                self.logger.info("Module creating cancelled.")
                                return None

                            gen_filename = gen_module_name.lower().replace(' ',
                                    '_')
                            self.logger.info("Reading core/module_template.py")
                            try:
                                with open('core/module_template.py',
                                        'r') as fopen:
                                    gen_module_data = fopen.read()

                            except(IOError, FileNotFoundError, OSError, \
                                    PermissionError):
                                self.latest_exceptions = traceback.format_exc()
                                printer.Printer().print_with_status(
                                        "Error while reading template!", 2
                                        )
                                self.logger.critical("Error while reading template!")
                                return None

                            else:
                                self.logger.info("Modifying template...")
                                gen_module_data = gen_module_data.replace(
                                        "<MODULE_NAME>",
                                        gen_module_name).replace(
                                        "<BRIEF_DESCRIPTION>", gen_description
                                        ).replace(
                                        "<MODULE_AUTHOR>", gen_author
                                        ).replace(
                                        "<DATE_CREATED>", time.strftime("%b. \
%d %Y")
                                        )

                                self.logger.info("Writing to {0}...".format(
                                            "output/" + gen_filename + ".py"
                                            ))
                                try:
                                    with open(
                                            "output/{0}.py".format(
                                            gen_filename), 'a') as fopen:
                                                fopen.write(gen_module_data)

                                    printer.Printer().print_with_status(
                                            "{0}.py module created \
successfully!".format(gen_filename))
                                    print("Now, edit your module located in \
output/{0}.py and create your amazing extension module!".format(gen_filename))
                                    self.logger.info("Module created!")

                                except(IOError, OSError, PermissionError):
                                    self.latest_exceptions = traceback.format_exc()
                                    printer.Printer().print_with_status(
                                            "Error while writing to file!", 2)
                                    self.logger.error("Error while writing \
to file!")
                                    return None

                                break

                    else:
                        return(5, error.ErrorClass().ERROR0005().split('\n'))

                elif command[1] in ("ls", "list"):
                    self.logger.info("Listing modules/ directory contents...")
                    paths = os.listdir('modules')
                    self.logger.info("Contents: " + str(paths))
                    iterator = 0
                    result = ""
                    for path in paths:
                        path = 'modules/' + path
                        if path in ('modules/__init__.py', 'modules/__pycache__'):
                            continue

                        self.logger.info("Checking if {0} is file.".format(path))
                        if misc.ProgramFunctions().isfile(path):
                            self.logger.info("{0} is a file.".format(path))
                            if path.endswith('.py'):
                                self.logger.info("{0} is a python module.".format(path))
                                try:
                                    path = path.replace(os.sep, '.')
                                    self.logger.debug(path)
                                    path = path[::-1]
                                    self.logger.debug(path)
                                    path = path.partition('.')[2]
                                    self.logger.debug(path)
                                    path = path[::-1]
                                    self.logger.debug(path)
                                    path = path.partition('.')[2]
                                    self.logger.debug(path)
                                    self.logger.info("Importing {0}...".format(path))
                                    module_obj = self._import_module(path, True)
                                    iterator += 1
                                    if module_obj is None:
                                        self.logger.info("Failed to import {0}!".format(path))
                                        result += ("[{0}] ".format(str(iterator)) + misc.FI + misc.CGR + misc.FB + path + " :: ERROR WHILE FETCHING INFO" + misc.END + '\n')

                                    else:
                                        self.logger.info("{0} imported! Now determining module status.".format(path))
                                        try:
                                            module_stats = eval("module_obj.{0}\
.module_info".format(self.module_call))
                                            if module_stats['status'].lower() == 'stable':
                                                self.logger.info("{0} is stable.".format(path))
                                                result += ("[{0}] ".format(str(iterator)) + misc.FI + misc.CG + path + " :: " + module_stats['bdesc'] + misc.END + '\n')

                                            elif module_stats['status'].lower() == 'experimental':
                                                self.logger.info("{0} is experimental.".format(path))
                                                result += ("[{0}] ".format(str(iterator)) + misc.FI + misc.CY + path + " :: " + module_stats['bdesc'] + misc.END + '\n')

                                            elif module_stats['status'].lower() == 'unstable':
                                                self.logger.info("{0} is unstable.".format(path))
                                                result += ("[{0}] ".format(str(iterator)) + misc.FI + misc.CR + path + " :: " + module_stats['bdesc'] + misc.END + '\n')

                                            else:
                                                self.logger.warning("{0} has unknown status!".format(path))
                                                result += ("[{0}] ".format(str(iterator)) + misc.FI + misc.CGR + path + " :: " + module_stats['bdesc'] + misc.END +  '\n')

                                        except Exception as err:
                                            self.logger.error("error while determining {0} status: {1}".format(path, str(err)))
                                            result += ("[{0}] ".format(str(iterator)) + misc.FI + misc.CGR + misc.FB + path + " :: ERROR WHILE FETCHING INFO: " + str(err) + misc.END + '\n')

                                except Exception as err:
                                    self.logger.error("error while determining {0} status!".format(path))
                                    result += ("[{0}] ".format(str(iterator)) + misc.FI + misc.CGR + misc.FB + path + " :: ERROR WHILE FETCHING INFO: " + str(err) + misc.END + '\n')

                        elif misc.ProgramFunctions().isfolder(path):
                            self.logger.info("{0} is a directory.".format(path))

                    if self.from_API is not True:
                        print(result)

                    else:
                        result = result.split('\n')
                        return result

                elif command[1] in ('test',):
                    self.logger.info("Testing {0} module...".format(command[2]))
                    module_obj = self._import_module(command[2])
                    self.logger.info("Checking if importing succeeded...")
                    if module_obj is None:
                        printer.Printer().print_with_status("Importing failed.", 2)
                        self.logger.error("Importing failed.")
                        return None

                    else:
                        self.logger.info("Importing succeeded; getting objects list.")
                        objects = module_obj.objects
                        i = 0
                        for obj in objects:
                            i += 1
                            asciigraphs.ASCIIGraphs().progress_bar_manual(
                                    "Testing module...", i, len(objects))

                            try:
                                eval("module_obj.{0}".format(obj))

                            except BaseException as err:
                                self.latest_exceptions = traceback.format_exc()
                                printer.Printer().print_with_status(
                                        str(err) + " (type `show tracebacks` \
for more info.)", 2)
                                time.sleep(1)
                                break

                            finally:
                                time.sleep(0.10)

                elif command[1] in ('use', 'run', 'exec'):
                    self.logger.info("Importing {0} module...".format(
                        command[2]))
                    module_obj = self._import_module(command[2])
                    self.logger.info("Checking if importing succeeded...")
                    if module_obj is None:
                        self.logger.error("Importing failed.")
                        return None

                    else:
                        self.logger.info("Importing succeeded; Calling \
prepare()...")
                        try:
                            options, ohelp = eval("module_obj.{0}\
.prepare()".format(self.module_call))

                        except(SystemExit):
                            self.logger.info("SystemExit detected from module...")
                            printer.Printer().print_with_status("SystemExit \
detected from module...", 1)
                            return None

                        except Exception as exception:
                            self.logger.info("An unknown error occured while \
using module: {0}".format(str(exception)))
                            self.latest_exceptions = traceback.format_exc()
                            printer.Printer().print_with_status(
                                    str(exception), 2)

                        while True:
                            try:
                                if self.userlevel == 3:
                                    self.module_command = input(self.prompt_lvl3.format(misc.FB + command[2]))

                                elif self.userlevel == 2:
                                    self.module_command = input(self.prompt_lvl2.format(misc.FB + command[2]))

                                elif self.userlevel == 1:
                                    self.module_command = input(self.prompt_lvl1.format(misc.FB + command[2]))

                                else:
                                    raise exceptions.UnknownUserLevelError("\
There is a problem obtaining the userlevel.")

                                self.logger.info("User entered: " +
                                    self.module_command)

                                if self.module_command.lower().startswith("help"):
                                    self.logger.info("Printing module help.")
                                    print()
                                    print("help                 Show this help \
menu.")
                                    print("set [KEY] [VALUE]    Set the value \
for <key>.")
                                    print("show [OPTION]        Show <option> \
to the screen.")
                                    print("run exec             Start module.")
                                    print("clear clr cls        Clears the screen.")
                                    print("back                 Quit module \
and go back to Archarios terminal.")
                                    print()
                                    print(misc.FB + "Available Keys:" +
                                            misc.END)
                                    for key in options:
                                        try:
                                            print(misc.FB + misc.CR + key +
                                                    misc.END + ": " + ohelp[key])

                                        except KeyError:
                                            print(misc.FB + misc.CR + key +
                                                    misc.END + ": " +
                                                    misc.CGR + "None" + misc.END)

                                    print()
                                    print(misc.FB + "Available Options:" +
                                            misc.END)
                                    print("{0}{1}info{2}       Show information \
about this module.".format(misc.FB, misc.CR, misc.END))
                                    print("{0}{1}values{2}     Show current \
values.".format(misc.FB, misc.CR, misc.END))
                                    print("{0}{1}options{2}    Show available \
options.".format(misc.FB, misc.CR, misc.END))
                                    print("{0}{1}tracebacks{2} Show latest exceptions.".format(misc.FB, misc.CR, misc.END))
                                    print()

                                elif self.module_command.lower().startswith("set"):
                                    mod_comm = self.module_command.partition(' ')[2]
                                    mod_com = mod_comm.partition(' ')
                                    self.logger.info("Partitioned command: " +
                                            str(mod_com))
                                    self.logger.info("Setting {0} to {1}.".format(mod_com[0], mod_com[2]))
                                    try:
                                        if type(options[mod_com[0]]) is bool:
                                            if mod_com[2].lower() in ('true', 'on', '1'):
                                                options[mod_com[0]] = True
                                                continue

                                            elif mod_com[2].lower() in ('false', 'off', '0'):
                                                options[mod_com[0]] = False
                                                continue

                                            else:
                                                printer.Printer().print_with_status(
                                                        "Invalid value for key! Must be True or False, On or Off, 0 or 1.", 2
                                                        )
                                                continue

                                        else:
                                            value_type = type(options[mod_com[0]])

                                    except KeyError:
                                        self.latest_exceptions = traceback.format_exc()
                                        printer.Printer().print_with_status(
                                                "Invalid key!", 2
                                                )
                                        continue

                                    try:
                                        options[mod_com[0]] = value_type(mod_com[2])

                                    except(TypeError, ValueError):
                                        self.latest_exceptions = traceback.format_exc()
                                        printer.Printer().print_with_status(
                                        "Invalid value for key!", 2)
                                        continue

                                elif self.module_command.lower().startswith("show"):
                                    try:
                                        mod_com = self.module_command.split(' ')
                                        if mod_com[1] == 'info':
                                            self.logger.info("Printing module info.")
                                            eval("module_obj.{0}\
.show_module_info()".format(self.module_call))

                                        elif mod_com[1]  == 'values':
                                            self.logger.info("Showing current values.")
                                            print(misc.FB + "Current Values:" +
                                                    misc.END)
                                            for key in options:
                                                print(misc.FB + misc.CR + str(key) +
                                                        misc.END + ": " +
                                                    str(options[key]))

                                        elif mod_com[1] == 'options':
                                            self.logger.info("Showing available keys.")
                                            print(misc.FB + "Available Keys:" +
                                                    misc.END)
                                            for key in options:
                                                try:
                                                    print(misc.FB + misc.CR + key +
                                                            misc.END + ': ' +
                                                            ohelp[key])

                                                except KeyError:
                                                    print(misc.FB + misc.CR + key +
                                                            misc.END + ": " +
                                                            misc.CGR + "None" +
                                                            misc.END)

                                        elif mod_com[1].lower(
                                                ) in ('tracebacks', 'traceback'):
                                            self.parse_input("show tracebacks")

                                        else:
                                            printer.Printer().print_with_status(
                                                    "Unknown option \
`{0}`!".format(mod_com[1]))
                                            continue

                                    except IndexError:
                                        eval("module_obj.{0}\
.show_module_info()".format(self.module_call))

                                elif self.module_command.lower(
                                    ).startswith(("run", "exec")):
                                    self.logger.info("Running module...")
                                    try:
                                        return_code = eval("module_obj.{0}.run(\
options)".format(self.module_call))
                                        try:
                                            return_code = int(return_code)

                                        except(ValueError, TypeError):
                                            print(misc.CR + \
                                                error.ErrorClass().ERROR0007() + misc.END)

                                        else:
                                            if return_code == 0:
                                                print(misc.CG + "Module successfully finished!" + misc.END)

                                            else:
                                                print(misc.CR + "Module exited with error code {0}!".format(str(return_code)) + misc.END)

                                    except BaseException as moduleExc:
                                        self.latest_exceptions = traceback.format_exc()
                                        printer.Printer(
                                                ).print_with_status(
                                                        str(moduleExc) + "\t(run \
`show tracebacks` for more info.)", 1)

                                elif self.module_command.lower().startswith(
                                    "back"):
                                    self.logger.info("Quitting module...")
                                    return None

                                elif self.module_command.lower().startswith(("clear",
                                        "cls", "clr", "clrscrn")):
                                    self.logger.info("Clearing the screen.")
                                    misc.ProgramFunctions().clrscrn()

                                else:
                                    self.logger.info("Unknown command: " +
                                            self.module_command)
                                    printer.Printer().print_with_status(
                                            "Unknown command: `{0}`!".format(
                                                self.module_command
                                                ), 2
                                            )

                            except(KeyboardInterrupt, EOFError):
                                self.logger.info("Printing additional options.")
                                print("More Options")
                                print()
                                print("[01] Standby")
                                print("[02] Force module to quit")
                                print()
                                print("[99] Back to module")
                                print()
                                while True:
                                    try:
                                        moption = int(input(" >>> "))
                                        if moption == 1:
                                            self.logger.info("Standing by...")
                                            print(cowsay.cowsay("I'm sleeping. \
Press CTRL+C when you are ready.").replace('(oo)', '(==)'))
                                            try:
                                                while True:
                                                    time.sleep(60)

                                            except(KeyboardInterrupt, EOFError):
                                                pass

                                        elif moption == 2:
                                            self.logger.critical("Forcing to \
quit module...")
                                            return None

                                        elif moption == 99:
                                            break

                                        else:
                                            self.logger.info("Unknown option: " +
                                                    str(moption))
                                            printer.Printer().print_with_status(
                                                    "Unknown option!", 2)
                                            continue

                                    except(KeyboardInterrupt, EOFError, TypeError, ValueError):
                                        break

                elif command[1] in ('reload', 'restart', 'reboot'):
                    try:
                        printer.Printer().print_with_status(
                                "Restarting {0}...".format(command[2]), 0)
                        self._reload_module(command[2])

                    except Exception as reload_error:
                        self.latest_exceptions = traceback.format_exc()
                        printer.Printer().print_with_status(str(reload_error), 2)

                else:
                    self.logger.info("No match for {0}... Showing help \
menu...".format(command[1]))
                    printer.Printer().print_with_status("Unknown option \
`{0}`!".format(command[1]), 2)
                    raise IndexError

            except IndexError:
                if self.from_API is not True:
                    print("""
USAGE: module [OPTIONS]

OPTIONS:
    ls list                  Show available modules.
    info [MODULE]            Show information of the specified module.
    test [MODULE]            Test the specified module.
    use run exec [MODULE]    Use the specified module.
    new generate             Generate a new module from template.
    reload [MODULE]          Reload the specified module.
""")

                else:
                    return[0, ["",
"USAGE: module [OPTIONS]",
"",
"OPTIONS:",
"    ls list                 Show available modules.",
"    info [MODULE]           Show information of the specified module.",
"    test [MODULE]           Test the specified module."
"    use run exec [MODULE]   Use the specified module.",
"    new generate            Generate a new module from template.",
"    reload [MODULE]         Reload the specified module.",
""]]

        elif command.lower().startswith("runpy"):
            command = command.partition(' ')[2]
            self.logger.info("Running command `{0}`...".format(
                command))
            try:
                dangers = ('sys.exit', 'os.exit', 'proper_exit')
                for danger in dangers:
                    if danger in command:
                        raise exceptions.CommandNotAllowedError("Sorry! The command you are trying to execute is not allowed by the program.")

                    else:
                        pass

                if command == '':
                    raise exceptions.InvalidCommandError("Command must not be NoneType!")

                else:
                    print()
                    print(eval(command))
                    print()

            except(PermissionError, OSError):
                self.latest_exceptions = traceback.format_exc()
                printer.Printer().print_with_status(str(
                    error.ErrorClass().ERROR0004('command')), 2)
                self.logger.error("User recieved ERROR 0004.")

            except Exception as err:
                self.latest_exceptions = traceback.format_exc()
                printer.Printer().print_with_status(str(err), 2)
                self.logger.error(str(err))

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
                    # subprocess.call(command)  # TODO: DEV0004: Use subprocess
                    os.system(command)
                    print()

            except(PermissionError, OSError):
                self.latest_exceptions = traceback.format_exc()
                printer.Printer().print_with_status(str(
                    error.ErrorClass().ERROR0004('command')), 2)
                self.logger.error("User recieved ERROR 0004.")

            except Exception as err:
                self.latest_exceptions = traceback.format_exc()
                printer.Printer().print_with_status(str(err), 2)
                self.logger.error(str(err))

        elif command.lower() in ('clear', 'cls', 'clr'):
            self.logger.info("Clearing the screen")
            misc.ProgramFunctions().clrscrn()

        elif command.lower() in ('restart', 'reboot'):
            if self.web is True:
                printer.Printer().print_with_status("Cannot restart when --web switch is enabled! Please manually restart {0}.".format(self.name), 1)
                return None

            self.logger.info("Restarting...")
            asciigraphs.ASCIIGraphs().animated_loading_screen(6,
                    "Restarting {0}...".format(self.name),
                    'swapcase',
                    0.10
                    )
            misc.ProgramFunctions().clrscrn()
            readline.write_history_file()
            misc.ProgramFunctions().program_restart()

        elif command.lower() in ('quit', 'exit'):
            self.logger.info("Gracefully exiting {0}...".format(self.name))
            print(misc.FB + misc.FI + misc.ProgramFunctions().random_color() +
                    random_phrases.phrases() + misc.END)
            self._proper_exit(0)

        elif command.lower() == "":
            return None

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
    oweb = None

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

        elif arg.lower() in ('-w', '--web',  '/w', '/web'):
            oweb = True

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
            debug=odebug,
            web=oweb
            ).console()
