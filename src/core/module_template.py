#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Archarios Framework :: The Novice's Ethical Hacking Framework
Copyright(C) 2018-2019 :: Catayao56 <Catayao56@gmail.com>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import random

from core import misc
from core import error
from core import logger
from core import exceptions

# Put all needed dependencies here!
try:
    # import something_here
    pass

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
        # Module Information

        # NOTE: DEV0004: Modify THIS DICTIONARY ONLY!
        self.module_info = {
                # Module name
                "name": "<MODULE_NAME>",
                # Module brief description
                "bdesc": "<BRIEF_DESCRIPTION>",
                # Module version
                "version": 1.0,
                # Module author
                "author": "<MODULE_AUTHOR>",
                # Module status
                "status": "Stable",
                # Date created (Please follow the format)
                "created": "<DATE_CREATED>",
                # Latest update (Please follow the format)
                "last_update": "<DATE_CREATED>",
                # Long description
                "ldesc": """\
<t>This module is meantly built for Archários Framework.<end>

This module can be a template for contributors if they
want to create their own module.

When creating a new module, <u>please read CONTRIBUTING.md<end>
for guidelines on creating a module, and
<u>CODE_OF_CONDUCT.md<end> for rules regarding to a
harassment-free experience.

<h>Formatting tutorial<end>:
    <n>NOTE<end>: <u>This applies to long descriptions (ldesc variable).<end>

    To highlight the title, use the `< t >` expression
    (without the spaces between `<` and `t`, `t` and `>`.)

    Example:
             <t>This is a title.<end>

    To highlight a subtitle, use the `< h >` expression
    (without the spaces between `<` and `h`, `h` and `>`.)

    Example:
             <h>This is a subtitle.<end>

    To format strings, use the following:
        `< u >` to underline text,
        `< i >` to italicize text, and
        `< b >` to bold text.

        (without the spaces!)

    Example:
             <u>Underlined<end>
             <i>Italicized<end>
             <b>Bold<end>

    To place a note, use the `< n >` expression
    (without the spaces between `<` and `n`, `n` and `>`.)

    Example:
             <n>This is a Note. Follow the guidelines when creating a module!<end>

    Remember to put `< end >` expression after the characters you
    want to be modified.

    Example:
             <t>This is a title,<end> and this is not.
             <h>This is a subtitle,<end> and this is not.
             <u>This is underlined,<end> and this is not.
             <i>This is italic,<end> and this is not.
             <b>This is bold,<end> and this is not.
             <n>This is a note,<end> and this is not.

             <t>F<end> <h>A<end> <u>N<end> <i>C<end> <b>Y<end> <n>!<end>

<h>Module Template Version History<end>
    1.0: Initial Release.
    1.1: Added version history on show_module_info() method.

             """.replace('<t>', misc.FB + misc.FU + misc.FI).replace(
                 '<end>', misc.END).replace('<u>', misc.FU).replace(
                 '<i>', misc.FI).replace('<b>', misc.FB).replace(
                 '<h>', misc.FB + misc.FI).replace('<n>',
                 misc.FB + misc.CY)
                }

        # NOTE: DEV0004: Modify THIS DICTIONARY ONLY!
        # Update history
        self.version_history = {
                    1.0: "Initial update"
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
        self.from_API = kwargs.get('API', False)

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

        if self.from_API is False:
            print(result)
            print(ver_hist)
            print('\n==================================================')

        else:
            return(result + '\n' + ver_hist +
                    '\n\n==================================================')

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
                # This can be none, it is allowed.
                }

        # Format: key + info
                # Example: "target": "The target to test."
        vhelp = {
                # This can be none, it is allowed.
                }

        return values, vhelp

    def run(self, values):
        """
        def run():
            Run the module.

            If call is from API, return tuple ``(0, "transcipt")``.
            tuple[0] is return code, and tuple[1] is transcript of result.
        """

        # NOTE: DEV0004: This is the method you will work on!

        if self.from_API is True:
            return((0, "Hello, world!"))

        else:
            print("Hello, world!")
            return 0
