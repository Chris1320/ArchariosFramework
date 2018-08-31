#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import random

from core import misc
from core import error
from core import logger
from core import printer
from core import exceptions

# Put all needed dependencies here!
try:
    from core import gethost

except BaseException as err:
    print("While importing dependency modules, an error occured: {0}".format(str(err)))
    importerror = True

else:
    importerror = False

"""
Template for creating a module for Archários Framework.
"""

# Put all objects here that needs to be tested.
objects = ["ArchariosFrameworkModule", "ArchariosFrameworkModule.__init__",
        "ArchariosFrameworkModule.prepare", "ArchariosFrameworkModule.run"]


class ArchariosFrameworkModule:
    """
    class ArchariosFrameworkModule():
        Main class of Archários Framework modules.
    """

    def __init__(self, *args, **kwargs):
        if importerror is not False:
            return 8

        else:
            pass

        # Module Information

        # NOTE: DEV0004: Modify THIS DICTIONARY ONLY!
        self.module_info = {
                # Module name
                "name": "Subdomain Scanner",
                # Module brief description
                "bdesc": "Searches for subdomains of a specified website.",
                # Module version
                "version": 1.1,
                # Module author
                "author": "Catayao56",
                # Module status
                "status": "Stable",
                # Date created (Please follow the format)
                "created": "Aug. 02 2018",
                # Latest update (Please follow the format)
                "last_update": "Aug. 02 2018",
                # Long description
                "ldesc": """\
<t>Subdomain Scanner<end>

This module searches for subdomains of a specified website and then you can
do more reconnaissance on the selected subdomain.

<n>User Guide/Manual<end>

Enter the target you want to scan. <b>Put an asterisk<end> (*) on the part
where we will search. For example, to find subdomains for <u>asimple.com<end>,
enter <u>*.asimple.com<end>. You may also use two or more asterisks, like
<u>*.*.asimple.com<end>.
""".replace('<t>', misc.FB + misc.FU + misc.FI).replace(
                 '<end>', misc.END).replace('<u>', misc.FU).replace(
                 '<i>', misc.FI).replace('<b>', misc.FB).replace(
                 '<h>', misc.FB + misc.FI).replace('<n>',
                 misc.FB + misc.CY)
                }

        # NOTE: DEV0004: Modify THIS DICTIONARY ONLY!
        # Update history
        self.version_history = {
                    1.0: "Initial update",
                    1.1: "Feature update: DNS Resolution mode"
                    }

        self._parse_module_info()
        # Get sufficient information from framework.
        self.debug = kwargs.get('debug', False)
        self.logger = kwargs.get('logger', None)
        """
        self.logger = logger.LoggingObject(
                name=self.module_info['name'],
                session_id=random.randint(100000, 999999),
                logfile='data/{0}.log'.format(self.module_info['name'])
                )
        self.logger.set_logging_level('NOTSET')
        if self.debug is True:
            self.logger.enable_logging()
        """

        self.fname = kwargs.get('fname', 'Archários Framework')
        self.fversion = kwargs.get('fversion', None)
        self.fcodename = kwargs.get('fcodename', None)
        self.fdescription = kwargs.get('fbanner', None)
        self.fbanner = kwargs.get('fbanner', None)
        self.userlevel = kwargs.get('userlevel', 3)

    def _parse_module_info(self):
        """
        def _parse_module_info():
            Parse module information for getting attention of user not
            following the guidelines.
        """

        # NOTE: DEV0004: Don't modify this method!

        mo_in = self.module_info

        # Check for variable types.

        if type(mo_in['name']) is not str:
            raise TypeError("Module name must be a string!")

        if type(mo_in['bdesc']) is not str:
            raise TypeError("Module's brief description must be a string!")

        if type(mo_in['version']) is not float and \
                type(mo_in['version']) is not int:
                    raise TypeError("Version must be int or float!")

        if type(mo_in['author']) is not str:
            raise TypeError("`author` variable must be str!")

        if type(mo_in['created']) is not str:
            raise TypeError("`created` variable must be a str!")

        if type(mo_in['last_update']) is not str:
            raise TypeError("`last_update` variable must be a str!")

        if type(mo_in['ldesc']) is not str:
            raise TypeError("`ldesc` variable must be a str!")

        if type(self.version_history) is not dict:
            raise TypeError("`version_history` variable must be a dict!")

        if type(mo_in['status']) is not str:
            raise TypeError("`status` variable must be a str!")

        # Check for value contents.

        if len(mo_in['name']) > 20 or len(mo_in['name']) < 1:
            raise ValueError("Module name must be 1-20 characters!")

        if len(mo_in['bdesc']) > 100 or len(mo_in['bdesc']) < 1:
            raise ValueError("Module's brief description must be 1-100 characters!")

        if mo_in['version'] < 0.1:
            raise ValueError("Version must be 0.1 and/or above in form of int or float!")

        if len(mo_in['author']) < 1 or len(mo_in['author']) > 50:
            raise ValueError("`author` variable must be 1-50 characters!")

	# Will be a mess for sure...
        try:
            created = mo_in['created'].split(' ')
            if created[0].replace('.', '') not in ('Jan', 'Feb', 'Mar',
                    'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct',
                    'Nov', 'Dec'):
                raise ValueError("Please don't modify `created` variable!")

            try:
                created[1] = int(created[1])

            except(TypeError, ValueError):
                raise ValueError("Please don't modify `created` variable!")

            try:
                created[2] = int(created[2])

            except(TypeError, ValueError):
                raise ValueError("Please don't modify `created` variable!")

        except IndexError:
            raise ValueError("Please don't modify `created` variable!")

        # Messy code ended... Well, not really :p
        try:
            last_updated = mo_in['last_update'].split(' ')
            if last_updated[0].replace('.', '') not in ('Jan', 'Feb', 'Mar',
                    'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sept', 'Oct',
                    'Nov', 'Dec'):
                raise ValueError("Please don't modify `created` variable!")

            try:
                last_updated[1] = int(last_updated[1])

            except(TypeError, ValueError):
                raise ValueError("Please don't modify `created` variable!")

            try:
                last_updated[2] = int(last_updated[2])

            except(TypeError, ValueError):
                raise ValueError("Please don't modify `created` variable!")

        except(IndexError):
            raise ValueError("Please don't modify `created` variable!")

        if len(mo_in['ldesc']) < 15:
            raise ValueError("Module's long description must be 15+ characters!")

        for key in self.version_history:
            if type(key) in (str, float):
                pass

            else:
                raise ValueError("version_history contents must be pairs of int/float and string!")

            if type(self.version_history[key]) is str:
                pass

            else:
                raise ValueError("version_history contents must be pairs of int/float and string!")

        if mo_in['status'].lower() not in ('stable', 'experimental',
                'unstable'):
            raise ValueError("`status` variable must have the value `stable`, `experimental`, or `unstable` only!")

    def show_module_info(self):
        """
        def show_module_info():
            Print module info.
        """

        # NOTE: DEV0004: Don't modify this method!

        result = """
==================================================
{0}{1}Name{2}: {3}
{0}{1}Version{2}: {4}
{0}{1}Author{2}: {5}
{0}{1}Brief Description{2}: {6}

{0}{1}Current Status{2}: {7}
{0}{1}Created On{2}: {8}
{0}{1}Last_Update{2}: {9}

{0}{1}Description{2}:

{10}
""".format(
        misc.FB, misc.CR, misc.END, self.module_info['name'],
        self.module_info['version'], self.module_info['author'],
        self.module_info['bdesc'], self.module_info['status'],
        self.module_info['created'], self.module_info['last_update'],
        self.module_info['ldesc'])

        ver_hist = """
{0}{1}Version History{2}:
""".format(misc.FB, misc.CR, misc.END)
        for version in self.version_history:
            ver_hist += "\n\t{0}: {1}".format(version, self.version_history[version])

        print(result)
        print(ver_hist)
        print('\n==================================================')

    def prepare(self):
        """
        def prepare():
            Return options required for run() method.
        """

        # NOTE: DEV0004: This is the method you will work on!
        # NOTE: DEV0004: Modify those dictionaries only!

        # Format: key + default_value
                # Example: "target": "192.168.0.1"
        values = {
                "target": "",
                "mode": 0,
                "wordlist": "{0}/data/subdomains.lst".format(os.getcwd())
                }

        # Format: key + info
                # Example: "target": "The target to test."
        vhelp = {
                "target": "Base website without the subdomain. (e.g.: *.google.com)",
                "mode": "Mode to use; 0 = default (DNS Resolution), 1 = Web Request",
                "wordlist": "Wordlist's absolute path."
                }

        return values, vhelp

    def run(self, values):
        """
        def run():
            Run the module.
        """

        if values['target'] == "":
            print("Please enter a website to scan!")
            return 1

        else:
            if values['mode'] == 0:
                pass

            elif values['mode'] == 1:
                self.request_mode(values)

            else:
                printer.Printer().print_with_status("Unknown discovery mode!", 2)
                return 3

            # Test for connection.
            test = gethost.byname(values['target'].replace(
                '.*.', '').replace(
                    '.*', '').replace(
                        '*.', '').replace(
                            '*', ''))

            if self.check_result(test) == "Passed":
                pass

            else:
                printer.Printer().print_with_status(error.ErrorClass().ERROR0006(), 2)

            # Open the wordlist.
            try:
                with open(values['wordlist'], 'r') as fopen:
                    subdomains = fopen.readlines()

            except(IOError, FileNotFoundError, EOFError, PermissionError):
                print("Cannot open `{0}`! Please make sure that the file exists\
and you arr permitted to read the file.")
                return 1

            else:
                # Set the wordlist.
                i = 0
                result = []
                while i < len(subdomains):

                    if subdomains[i].endswith('\n'):
                        subdomains[i] = subdomains[i][::-1]
                        subdomains[i] = subdomains[i].partition('\n')[2]
                        subdomains[i] = subdomains[i][::-1]

                    try:
                        printer.Printer().print_with_status(
                                "Testing {0}....".format(values[
                                    'target'].replace(
                                        '*', subdomains[i])), 0)

                        result.append(gethost.byname(values[
                            'target'].replace('*', subdomains[i])))

                    except(KeyboardInterrupt, EOFError):
                        return 2

                    finally:
                        i += 1

                # Print results
                i = 0
                bgcolor = misc.CGR
                while i < len(subdomains):
                    try:
                        sub2print = subdomains[i]
                        res2print = result[i]
                        if self.check_result(res2print) == "Passed":
                            print("{2}{0} :: {1}{3}".format(values['target'
                                ].replace('*', sub2print), res2print, bgcolor,
                                misc.END))

                        else:
                            pass

                    except(KeyboardInterrupt, EOFError):
                        pass

                    finally:
                        i += 1
                        if bgcolor == misc.END:
                            bgcolor = misc.CGR

                        else:
                            bgcolor = misc.END

                print()
                while True:
                    try:
                        ask_user = input("Do you want to \
send the result to a file? (y/n) > ")

                    except(KeyboardInterrupt, EOFError):
                        continue

                    else:
                        if ask_user.lower() == 'y':
                            try:
                                outfile = input("Output filename: ")

                            except(KeyboardInterrupt, EOFError):
                                pass

                            else:
                                try:
                                    with open("output/{0}".format(outfile), 'w') as f:
                                        f.write('')

                                    with open("output/{0}".format(outfile), 'a') as f:
                                        i = 0
                                        while i < len(subdomains):
                                            try:
                                                f.write('{0} :: {1}\
\n'.format(values['target'].replace('*', subdomains[i]), result[i]))

                                            except(IOError, FileNotFoundError, EOFError, UnicodeDecodeError):
                                                pass

                                            finally:
                                                i += 1

                                except(IOError, FileNotFoundError, EOFError, UnicodeDecodeError):
                                    printer.Printer().print_with_status("Cannot write to file!", 2)

                                else:
                                    printer.Printer().print_with_status("Result written to file!", 0)
                                    return 0

                        else:
                            return 0

    def check_result(self, gethost_result):
        """
        def check_result():
            The gethost module catches all exceptions.
            So this method check if the result returned by the module
            is an error or an expected result.
        """

        errors = ['Errno', 'Error', 'Err', 'errno', 'error', 'err']

        # Test no. 1
        if type(gethost_result) is "gaierror":
            return "Failed"

        # Test no. 2
        for error in errors:
            if error in str(gethost_result):
                return "Failed"

            else:
                continue

        return "Passed"

    def request_mode(self, values):
        """
        def request_mode():
            Web request mode instead of DNS resolution.
        """

        pass
