#!/usr/bin/env python3

import random

from core import misc
from core import error
from core import logger
from core import exceptions

# Put all needed dependencies here!
try:
    import whois
    import requests

    from core import printer
    from core import gethost
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

        self.module_info = {
                # Module name
                "name": "ReconMe",
                # Module brief description
                "bdesc": "A suite of tools for information gathering.",
                # Module version
                "version": 1.2,
                # Module author
                "author": "Catayao56",
                # Module status
                "status": "Stable",
                # Date created (Please follow the format)
                "created": "Jul. 28 2018",
                # Latest update (Please follow the format)
                "last_update": "Jul. 31 2018",
                # Long description
                "ldesc": """\
<t>ReconMe :: A suite of tools for information gathering<end>

ReconMe is a tool included in Archários Framework to gather information
about a website or a network.

<h>Features:<end>
    - Custom timeout for every connection.
    - We provided a <n>FREE<end> <b>API key<end> to be used. <n>Please don't abuse it<end>.
    - Custom user agent string.
    - Get the site title.
    - Get the IP address of the web server.
    - Get the CMS information.
    - Try to resolve IP from subdomains if IP is hidden by CloudFlare.
    - Get robots.txt file from target.
    - Gather whois information of the target.
    - Gather geolocation information of the target.
    - Grab banners of the target.
    - Perform DNS lookup.
    - Perform subnet calculation.
    - Search for subdomains.
    - Perform a reverse IP lookup.
    - `Harvest` more information from trusted sources.

""".replace('<t>', misc.FB + misc.FU + misc.FI).replace(
                 '<end>', misc.END).replace('<u>', misc.FU).replace(
                 '<i>', misc.FI).replace('<b>', misc.FB).replace(
                 '<h>', misc.FB + misc.FI).replace('<n>',
                 misc.FB + misc.CY)
                }

        # Update history
        self.version_history = {
                    1.0: "Initial update",
                    1.1: "Added more features. Added get_cms and cloudflare_resolve switches.",
                    1.2: "Added more features. Added get_robots and whois switches."
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

        # Format: key + default_value
                # Example: "target": "192.168.0.1"
        values = {
                "target": "127.0.0.1:80",
                "timeout": 120.0,
                "api_key": "905e60805eecd6881177ac424007c2f7c\
ca786dd8892d941a8bfecbf4125e5fced3b30",
                "user_agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
                "get_site_title": False,
                "get_ip_address": True,
                "get_cms": False,
                "cloudflare_resolve": False,
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
                "api_key": "https://whatcms.org API key. We trust you, so \
please don't abuse this public API key. Change this if you have another API.",
                "user_agent": "Set a custom user agent string; Otherwise, don't modify.",
                "get_site_title": "Get the site title.",
                "get_ip_address": "Get the external IP address of the target.",
                "get_cms": "Get the CMS information of the website.",
                "cloudflare_resolve": "Try to resolve IP from subdomains.",
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

        global error

        # Step 1: Check if http:// or https:// is not present in values['target'].
        if 'http://' not in values['target'] and 'https://' not in values['target']:
            print("No schema supplied, using http:// instead...")
            values['target'] = 'http://' + values['target']

        # Step 2: Check if there is stable connection between user and target.
        try:
            print("[i] Checking connection between you and {0}...".format(values['target']))
            requests.get(values['target'], timeout=values['timeout'])

        except(ConnectionResetError, ConnectionError,
                requests.ConnectionError):
            printer.Printer().print_with_status(error.ErrorClass().ERROR0006(), 2)
            print("[?] Maybe {0} is not a web server?".format(values['target']))
            # FIXME: DEV0001: What if target is not a web server?
            # print("[i] Trying to contact via DNS...")
            # gethost.byname(values['target'].partition('://')[2].partition('/')[0])
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

                if len(result_site_title) > 500:
                    result_site_title = "[Cannot get site title]"

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

        # Step 5: Get CMS name.
        if values['get_cms'] is True:
            print("[i] Getting CMS name...")
            result_cms = requests.get('https://whatcms.org/APIEndpoint/Detect?key={0}&url={1}'.format(values['api_key'], values['target'])).text
            # What a dirty work...
            result_cms = eval(result_cms.replace('":null',
                '":None'))
            if int(result_cms['result']['code']) != 200:
                print("[i] Cannot get CMS information, server returned HTTP code {0}.".format(str(result_cms['result']['code'])))
                if int(result_cms['result']['code']) == 0:
                    print("\t[i] A server failure occured.")

                elif int(result_cms['result']['code']) == 100:
                    print("\t[i] The API key is not set.")

                elif int(result_cms['result']['code']) == 101:
                    print("\t[i] The API key is invalid.")

                elif int(result_cms['result']['code']) == 102:
                    print("\t[i] Your request is not authenticated.")

                elif int(result_cms['result']['code']) == 110:
                    print("\t[i] The URL is not set.")

                elif int(result_cms['result']['code']) == 111:
                    print("\t[i] The URL is invalid.")

                elif int(result_cms['result']['code']) == 112:
                    print("\t[i] There is a missing required parameter.")

                elif int(result_cms['result']['code']) == 113:
                    print("\t[i] There is an invalid required parameter.")

                elif int(result_cms['result']['code']) == 120:
                    print("\t[i] There are too many requests using this API key. Please create your own API key by registering to ``whatcms.org``.")

                elif int(result_cms['result']['code']) == 121:
                    print("\t[i] This API key exceeded the monthly quota. Please wait for the next month or create your own API key by registering to ``whatcms.org``.")

                elif int(result_cms['result']['code']) == 123:
                    print("\t[i] This API key violated the Terms and Conditions.")

                elif int(result_cms['result']['code']) == 201:
                    print("\t[i] Cannot determine CMS/Host.")

                elif int(result_cms['result']['code']) == 202:
                    print("\t[i] The requested URL is unavailable.")

                else:
                    pass

            result_cms_name = result_cms['result']['name']
            result_cms_version = result_cms['result']['version']
            result_cms_confidence = result_cms['result']['confidence']
            if type(result_cms['result']['cms_url']) is str:
                result_cms_url = result_cms['result']['cms_url'].replace('\\', '')

            else:
                result_cms_url = "N/A"

            if result_cms_version is None:
                result_cms_version = "Cannot determine CMS version"

        else:
            print("[i] get_cms is false, now skipping...")
            result_cms_name = ""
            result_cms_version = ""
            result_cms_confidence = "low"
            result_cms_url = ""

        # Step 6: Try to resolve IP from subdomain.
        target_site = values['target'].partition('://')[2].partition('/')[0]
        if values['cloudflare_resolve'] is True:
            print("[i] Checking if we are getting blocked by CloudFlare.")
            try:
                request_title = requests.get(values['target'],
                    headers={'headers': values['user_agent']},
                    timeout=values['timeout'])

                al = request_title.text
                check_cloudflare = al[al.find('<title>') + 7 : al.find('</title>')]
                if "used CloudFlare to restrict access</title>" in check_cloudflare:
                    print("[i] {0} is protected by CloudFlare.".format(
                        values['target']))
                    result_cloudflare_protected = True

                else:
                    print("[i] {0} is not protected by CloudFlare.".format(
                        values['target']))
                    result_cloudflare_protected = False

                print("[i] Trying to resolve IP from subdomains...")
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
                    print("[i] Getting default IP address...")
                    result_default_ip = gethost.byname(target_site)
                    print("\t[i] Default IP Address: {0}".format(result_default_ip))

                except Exception as err:
                    printer.Printer().print_with_status(str(err), 2)

                hosts_discovery_f = {}
                hosts_discovery_u = {}
                hosts_discovery_s = {}
                iterator = 0
                for sub in subdomains:
                    iterator += 1
                    asciigraphs.ASCIIGraphs().progress_bar_manual('Checking \
for subdomains...'.format(sub, sub + '.' + target_site), iterator,
                    len(subdomains), 20)
                    subhost = sub + '.' + target_site
                    try:
                        result_subhost_ip = gethost.byname(subhost)
                        errors = ['Errno', 'Error', 'error', 'errno']
                        for error in errors:
                            if error in str(result_subhost_ip):
                                hosts_discovery_f[subhost] = \
                                        str("[Hostname does not exist]") + misc.END
                                please_continue = True
                                break

                            else:
                                please_continue = False
                                continue

                        if please_continue is True:
                            please_continue = False
                            continue

                        if result_subhost_ip != result_default_ip:
                            hosts_discovery_u[subhost] = \
                                    str(result_subhost_ip) + misc.END
                            continue

                        else:
                            hosts_discovery_s[subhost] = \
                                    str(result_subhost_ip) + misc.END
                            continue

                    except Exception as err:
                        printer.Printer().print_with_status(str(err), 2)
                        continue

            except Exception as erred:
                printer.Printer().print_with_status(str(erred), 2)
                return 7

        else:
            result_cloudflare_protected = "N/A"
            result_default_ip = result_ip_address
            hosts_discovery_f = []
            hosts_discovery_u = []
            hosts_discovery_s = []

        # Step 7: Get robots.txt file.
        if values['get_robots'] is True:
            print("[i] Getting robots.txt file from {0}...".format(values['target']))
            try:
                request_robots = requests.get(values['target'] + '/robots.txt',
                        headers={'headers': values['user_agent']},
                        timeout=values['timeout'])
                robots_data = request_robots.text
                got_robots = True

            except ImportError:
                pass

        else:
            print("[i] get_robots is false, now skipping...")
            robots_data = None
            got_robots = False

        # Step 8: Get whois information.
        if values['whois'] is True:
            print("[i] Getting whois information...")
            try:
                whois_result = whois.query(target_site)

            except Exception as whoiserror:
                printer.Printer().print_with_status(str(whoiserror), 2)
                whois_result = None

        else:
            print("[i] whois is false, now skipping...")
            whois_result = None

        # Step 9: Get geolocation from IP.
        # TODO: DEV0001: Do this!
        if values['geoip'] is True:
            print("[i] Getting geolocation of {0}.".format(values['target']))

        else:
            print("[i] geoip is false, now skipping...")

        # Step __: Print the results.
        print(misc.FB + misc.CC + \
                "Results for `{0}`:".format(values['target']) + misc.END)
        print()
        print(misc.CG + "Site Title:" + misc.END, result_site_title)
        print(misc.CG + "IP Address:" + misc.END, result_ip_address)
        print(misc.CG + "CMS Name:" + misc.END, result_cms_name,
                "\t(with", result_cms_confidence, "confidence)")
        print(misc.CG + "CMS Version:" + misc.END, result_cms_version)
        print(misc.CY + "\t[i] More information about the CMS:" + \
                misc.END, result_cms_url)
        print(misc.CG + "Cloudflare Protection:" + misc.END, result_cloudflare_protected)
        print(misc.CG + "Default IP Address:" + misc.END, result_default_ip)
        for failed_host_discovery in hosts_discovery_f:
            print('\t' + misc.CR + failed_host_discovery, ':',
                    hosts_discovery_f[failed_host_discovery] + misc.END)

        for so_close_host_discovery in hosts_discovery_u:
            print('\t' + misc.CY + so_close_host_discovery, ':',
                    hosts_discovery_u[so_close_host_discovery] + misc.END)

        for success_host_discovery in hosts_discovery_s:
            print('\t' + misc.CG + success_host_discovery, ':',
                    hosts_discovery_s[success_host_discovery] + misc.END)

        print()
        if whois_result is None:
            print(misc.CR + "Whois Information: Error fetching data" + misc.END)

        else:
            print(misc.CG + "Whois Information:" + misc.END)
            print(misc.CY + "\tExpiration Date:" + misc.END,
                    whois_result.expiration_date)
            print(misc.CY + "\tLast Updated:" + misc.END, whois_result.last_updated)
            print(misc.CY + "\tRegistrar:" + misc.END, whois_result.registrar)
            print(misc.CY + "\tName:" + misc.END, whois_result.name)
            print(misc.CY + "\tCreation Date:" + misc.END, whois_result.creation_date)

        print()
        if got_robots is True:
            try:
                if misc.ProgramFunctions().path_exists('output/{0}_robots.txt'.format(target_site)):
                    filename = target_site + '-1'

                else:
                    filename = target_site

                with open('output/{0}_robots.txt'.format(filename), 'w') as fopen:
                    fopen.write("# Produced by ReconMe, a module from \
Archarios Framework\n\n" + robots_data)

            except(IOError):
                print(misc.CR + "There was a problem writing to the robots.txt file." + \
                        misc.END)
                return 9

            else:
                print(misc.CG + "Robots.txt file saved to `output/{0}_robots.txt`\
.".format(filename))

        else:
            pass

        # TODO: DEV0001: Do this!
        # print(misc.CG + "Geolocation:" + misc.END)
        # print(misc.CY + "Longitude:" + misc.END)
        print()
        return 0
