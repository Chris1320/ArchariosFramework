#!/usr/bin/env python3
#coding=utf-8

import random

from core import misc
from core import error
from core import logger
from core import exceptions

# Put all needed dependencies here!
try:
    from core import gethost
    from core import printer
    from core import asciigraphs

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
                "name": "WhatsYourName",
                # Module brief description
                "bdesc": "Get host by a number of ways.",
                # Module version
                "version": 1.0,
                # Module author
                "author": "Catayao56",
                # Module status
                "status": "Stable",
                # Date created (Please follow the format)
                "created": "Aug. 01 2018",
                # Latest update (Please follow the format)
                "last_update": "Aug. 01 2018",
                # Long description
                "ldesc": """\
<t>WhatsYourName -- Get host by a number of ways.<end>

WhatsYourName gets the host by a number of ways. The methods are listed below:

    + Get host's IP from DNS. (`default` method)
    + Get IP address from subdomains. (`subdomain` method.)
    + Get IP address from whois registrars. (`whois` method.) (<n>Work In Progress<end>)

If you know any methods, feel free to create a merge request or contact me on
e-mail of facebook to do it.

-Catayao56
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
            ver_hist += '\n{0}: {1}'.format(version, self.version_history[version])

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
                "target": "localhost",
                "method": "default"
                }

        # Format: key + info
                # Example: "target": "The target to test."
        vhelp = {
                "target": "Target host. Must be a domain name.",
                "method": "Method to use. `show help` for more info."
                }

        return values, vhelp

    def run(self, values):
        """
        def run():
            Run the module.
        """

        if '://' in values['target']:
            values['target'] = values['target'].partition('://')[2]
            values['target'] = values['target'].partition('/')[0]

        if values['method'].lower() == 'default':
            try:
                ip = gethost.byname(values['target'])
                error = ['Errno', 'Error', 'Err', 'errno', 'error', 'err',
                        'ERRNO', 'ERROR', 'ERR']
                for err in error:
                    if err in ip:
                        printer.Printer().print_with_status(
                                "An error occured: " + str(ip), 2)
                        return 2

                    else:
                        continue

                print(misc.CG + misc.FB + "IP Address of `{0}` is `{1}`.".format(values['target'], ip))
                return 0

            except(KeyboardInterrupt, EOFError):
                print(error.ErrorCodes().ERROR0002())
                return 1

        elif values['method'].lower() == 'subdomain':
            try:
                subdomains = ('www', 'mail', 'mail2', 'webmail',
                        'email', 'direct-connect-mail', 'direct',
                        'direct-connect', 'cpanel', 'phpmyadmin',
                        'ftp', 'forum', 'blog', 'm', 'dev',
                        'record', 'ssl', 'dns', 'help', 'ns',
                        'ns1', 'ns2', 'ns3', 'ns4', 'irc', 'server',
                        'status', 'portal', 'beta', 'admin',
                        'alpha', 'imap', 'smtp', 'test', 'mx', 'mx0',
                        'remote', 'mx1', 'mailserver', 'server', 'mx2',
                        'mail1', 'redbusprimarydns', 'redbussecondarydns',
                        'vpn', 'mx7', 'secure', 'shop', 'cloud', 'mx01',
                        'api', 'dns1', 'dns2', 'host', 'app', 'support',
                        'ww1', 'mailin1', 'mailin2', 'pop', 'bbs', 'web',
                        'r.1', 'r.2', 'r.3', 'owa')

                result_default_ip = gethost.byname(values['target'])
                print("\t[i] Default IP Address: {0}".format(result_default_ip))

            except Exception as err:
                printer.Printer().print_with_status(str(err), 2)
                return 3

            try:
                hosts_discovery = {}
                iterator = 0
                for sub in subdomains:
                    iterator += 1
                    asciigraphs.ASCIIGraphs().progress_bar_manual('Checking \
for subdomains...', iterator, len(subdomains), 20)
                    subhost = sub + '.' + values['target']
                    try:
                        result_subhost_ip = gethost.byname(subhost)
                        errors = ['Errno', 'Error', 'error', 'errno']
                        for error in errors:
                            if error in str(result_subhost_ip):
                                please_continue = True
                                break

                            else:
                                please_continue = False
                                continue

                        if please_continue is True:
                            please_continue = False
                            continue

                        if result_subhost_ip != result_default_ip:
                            hosts_discovery[subhost] = \
                                    misc.CG + str(result_subhost_ip) + misc.END

                        else:
                            hosts_discovery[subhost] = \
                                    misc.CY + str(result_subhost_ip) + misc.END

                    except Exception as err:
                        printer.Printer().print_with_status(str(err), 2)
                        continue

                print("{0}Results{1}:".format(misc.FB + misc.CR, misc.END))
                for result in hosts_discovery:
                    print("\t{0}: {1}".format(result, hosts_discovery[result]))

                return 0

            except Exception as erred:
                printer.Printer().print_with_status(str(erred), 2)
                return 4
