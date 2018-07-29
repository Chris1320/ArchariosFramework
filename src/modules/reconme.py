#!/usr/bin/env python3

import random

from core import misc
from core import error
from core import logger
from core import exceptions

# Put all needed dependencies here!
try:
    import requests

    from core import printer
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
objects = ["ArchariosFrameworkModule"]


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
                "name": "ReconMe",
                # Module brief description
                "bdesc": "A suite of tools for information gathering.",
                # Module version
                "version": 1.0,
                # Module author
                "author": "Catayao56",
                # Module status
                "status": "Stable",
                # Date created (Please follow the format)
                "created": "Jul. 28 2018",
                # Latest update (Please follow the format)
                "last_update": "Jul. 28 2018",
                # Long description
                "ldesc": """\
<t>ReconMe :: A suite of tools for information gathering<end>

ReconMe is a tool included in Archários Framework to gather information
about a website or a network.
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
==================================================""".format(
        misc.FB, misc.CR, misc.END, self.module_info['name'],
        self.module_info['version'], self.module_info['author'],
        self.module_info['bdesc'], self.module_info['status'],
        self.module_info['created'], self.module_info['last_update'],
        self.module_info['ldesc'])
        print(result)

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
                "target": "127.0.0.1:80",
                "timeout": 120.0,
                "user_agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
                "get_site_title": False,
                "get_ip_address": True,
                "get_cms": False,
                "get_ddos_protect": False,
                "get_robots": False,
                "whois": False,
                "geoip": True,
                "grab_banners": False,
                "dns_lookup": True,
                "subnet_calc": True,
                "subdomain": False,
                "reverse_ip_lookup": False,
                "harvester": False
                }

        # Format: key + info
                # Example: "target": "The target to test."
        vhelp = {
                "target": "Target web server.",
                "timeout": "Set the timeout for every connection attempts.",
                "user_agent": "Set a custom user agent; Otherwise, don't modify.",
                "get_site_title": "Get the site title.",
                "get_ip_address": "Get the external IP address of the target.",
                "get_cms": "Get the CMS name of the website.",
                "get_ddos_protect": "Check if website is capable of DDoS protection. (e.g.: Cloudflare",
                "get_robots": "get robots.txt file from target.",
                "whois": "Gather whois information via hackertarget.com API.",
                "geoip": "Gather geolocation information via hackertarget.com API.",
                "grab_banners": "Grab banners.",
                "dns_lookup": "Perform DNS lookup using hackertarget.com API.",
                "subnet_calc": "Perform subnet calculation using hackertarget.com API.",
                "subdomain": "Search for subdomains.",
                "reverse_ip_lookup": "Perform a reverse IP lookup using yougetsignal.com API.",
                "harvester": "`Harvest` more information from trusted sources."
                }

        return values, vhelp

    def run(self, values):
        """
        def run():
            Run the module.
        """

        # Step 1: Check if http:// or https:// is not present in values['target'].
        if 'http://' not in values['target'] and 'https://' not in values['target']:
            print("No schema supplied, using http:// instead...")
            values['target'] = 'http://' + values['target']

        # Step 2: Check if there is stable connection between user and target.
        try:
            print("[i] Checking conection between you and {0}...".format(values['target']))
            requests.get(values['target'], timeout=values['timeout'])

        except(ConnectionResetError, ConnectionError,
                requests.ConnectionError):
            printer.Printer().print_with_status(error.ErrorClass().ERROR0006(), 2)
            print("[?] Maybe {0} is not a web server?".format(values['target']))
            return 1

        except Exception as err:
            printer.Printer().print_with_status(str(err), 2)
            return 2

        # Step 3: Get site title
        if values['get_site_title'] is True:
            print("[i] Getting site title...")
            try:
                request_title = requests.get(values['target'],
                        headers={'headers': values['user_agent']},
                        timeout=values['timeout'])
                al = request_title.text
                result_site_title = al[al.find('<title>') + 7 : al.find('</title>')]

            except Exception as err:
                printer.Printer().print_with_status("Oh crap! We lost connection to `{0}`!".format(values['target']), 2)
                return 3

        else:
            print("[i] get_site_title is false, now skipping...")
            result_site_title = ""

        # Step 4: Get IP Address
        if values['get_ip_address'] is True:
            print("[i] Getting External IP Address of target...")
            result_ip_address = gethost.byname(values['target'].partition(
                '://')[2].partition('/')[0])

        else:
            print("[i] get_ip_address is false, now skipping...")
            result_ip_address = ""

        # Step __: Print the results.
        print(misc.FB + misc.CC + \
                "Results for `{0}`:".format(values['target']) + misc.END)
        print()
        print(misc.CG + "Site Title:" + misc.END, result_site_title)
        print(misc.CG + "IP Address:" + misc.END, result_ip_address)
        print()
        return 0
