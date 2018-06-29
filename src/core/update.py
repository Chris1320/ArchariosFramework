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
from core import misc
from core import error
from core import fullupdate
import subprocess

def full_update(global_variables, DEBUGGING):
    HEAD_COL = '[' + misc.FB + misc.FI + misc.CB + 'i' + misc.END + '] ' + \
            misc.FB + misc.FI + misc.CB
            
    HEAD_END = misc.END

    print(HEAD_COL + "Performing a full update." + HEAD_END)
    prog_update(global_variables, DEBUGGING)
    deps_update(global_variables)
    print(misc.END + HEAD_COL + "Full update finished running..." + HEAD_END)
    
    """
    process = "4"

    print(misc.FB + misc.FI + misc.CB + "Performing a full update..." + misc.FR + misc.CW)
    print(misc.CB + "Installing dependency files... (1/" + process + ")\n" + misc.CW)
    if sys.platform == 'windows' or sys.platform == 'nt':
        print("[i] Can't install binaries on Windows. Please install them manually.")

    else:
        subprocess.call(["bash", "instdeps.bash"]) # DEV0001: Need a new algorithm!

    print(misc.CB + "Updating Shadow Suite... (2/" + process + ")\n" + misc.CW)
    fullupdate.update(global_variables, DEBUGGING)

    print(misc.CB + "Installing python modules... (3/" + process + ")\n" + misc.CW)
    subprocess.call("pip", "install", "-r", "python_requirements") # DEV001: Also needs a new algorithm! I'm sure people are sick using this! >:(

    print(misc.CB + "Installing perl modules... (4/" + process + ")\n" + misc.CW)
    os.system("cpan threads Thread Net WWW Getopt Socket IO Strict Warnings Config Term XML String DotDotPwn threads::shared Thread::Queue WWW::Mechanize") # DEV0001: Also this!

    print(misc.FB + misc.FI + misc.CB + "Performing a full update... Done!" + misc.FR + misc.CW)
    """

def deps_update(global_variables):
    binaries = ['curl', 'git', 'less', 'nmap', 'perl', 'php', 'php-dev', 'python', 'python3', 'python2', 'python-dev', 'python3-dev', 'python2-dev', 'ruby', 'ruby-dev', 'tar', 'vim', 'wget', 'zip', 'hydra']

    python3 = ['requests', 'optparse', 'urlparse', 'getopt', 'xml', 'argparse', 'beautifulsoup4', 'cryptography', 'future', 'idna', 'netaddr', 'numpy', 'paramiko', 'pyasn1', 'pycrypto', 'python-dateutil', 'python-nmap', 'shodan', 'SQLAlchemy', 'urllib', 'urllib3', 'urllib2']

    python2 = ['attrs', 'Automat', 'beautifulsoup4', 'bs4', 'idna', 'incremental', 'mechanize', 'nltk', 'pexpect', 'python-dateutil', 'requests', 'SQLAlchemy', 'urllib3', 'urllib', 'urllib2']

    perl = ['threads', 'Thread', 'Net', 'WWW', 'Getopt', 'Socket', 'IO', 'Strict', 'Warnings', 'Config', 'Term', 'XML', 'String']

    """
    Why there are 6 python binaries?

        We have 6 because python has 2 versions: Python2 and Python3.
        And the Development files: Python2-Dev and Python3-Dev.
        Termux has different python3 name, it is named 'python' only.
        As of now, we cannot identify if System is an emulator or
        a real linux system. So, this is another messy code...
    """

    H1 = '[' + misc.FB + misc.FI + misc.CB + 'i' + misc.END + '] ' + \
            misc.FB + misc.FI + misc.CB
    H2 = '[' + misc.CB + "+" + misc.END + '] ' + misc.CB
    H3 = '[' + misc.CR + '-' + misc.END + '] ' + misc.CR
    H4 = '[' + misc.CGR + '?' + misc.END + '] ' + misc.CGR

    print(H1 + "Installing OS-Specific binaries..." + misc.END)
    if misc.programFunctions().is_windows():
        print(H3 + "Shadow Suite Framework cannot install binaries on Windows Systems *YET*. Please install them manually:" + misc.END)
        return None

    else:
        apt_present = os.system("which apt")
        yum_present = os.system("which yum")
        pkg_present = os.system("which pkg")
        if apt_present == 0:
            mgr = 'apt'
            arg = 'install'

        elif yum_present == 0:
            mgr = 'yum'
            arg = ['install']

        elif pkg_present == 0:
            mgr = 'pkg'
            arg = 'install'

        else:
            print(H3 + "It seems you have no package manager or we just cannot detect it..." + misc.END)
            while True:
                try:
                    manual_mgr = input(H4 + "Do you want to manually enter your package manager's name? (y/n): " + misc.END)
                    if manual_mgr.lower() == 'y':
                        mgr = input("Enter the name of your package manager: " + misc.END)
                        arg = ['install']
                        break

                    elif manual_mgr.lower() == 'n':
                        print(H3 + "No package managers known by SSF are available, now aborting update..." + misc.END)
                        return None

                    else:
                        continue

                except Exception as e:
                    print(H3 + str(e) + misc.END)
                    continue

        erred_binary = []
        for binary in binaries:
            lst = [mgr]
            lst.append(arg)
            if mgr == 'apt' or mgr == 'pkg':
                lst.append('--upgrade')

            lst.append(binary)
            #print(lst)
            try:
                code = subprocess.call(lst)

            except Exception as binerr:
                print(H3 + str(binerr) + misc.END)
                return None

            if code != 0:
                erred_binary.append(binary)

            else:
                continue

    tries = 0
    while True:
        pip_present = os.system("which pip")
        pip3_present = os.system("which pip3")
        if pip3_present == 0:
            pip = 'pip3'
            break

        elif pip_present == 0:
            pip = 'pip'
            break

        else:
            if tries == 3:
                print(H3 + "Maximum retries reached! Please try again later." + misc.END)
                return None

            try:
                os.system(sys.argv[0] + " -m pip install --upgrade pip")

            except Exception as piperr:
                print(H3 + str(piperr) + misc.END)
                return None

            tries += 1
            continue

    erred_python3 = []
    for packages in python3:
        try:
            code = subprocess.call([pip, 'install', '--upgrade', packages])

        except Exception as pipinsterr:
            print(H3 + str(pipinsterr) + misc.END)
            return None

        if code != 0:
            erred_python3.append(packages)

        else:
            continue

    tries = 0
    while True:
        pip2_present = os.system("which pip2")
        pip_present = os.system("which pip")
        if pip2_present == 0:
            pip = 'pip2'
            break

        elif pip_present == 0:
            pip = 'pip'
            break

        else:
            if tries == 3:
                print(H3 + "Maximum retries reached! Please try again later." + misc.END)
                return None
            
            try:
                os.system(sys.argv[0] + " -m install --upgrade pip")

            except Exception as pipinsterr:
                print(H3 + str(pipinsterr) + misc.END)
                return None

            tries += 1
            continue

    erred_python2 = []
    for packages in python2:
        try:
            code = subprocess.call([pip, 'install', '--upgrade', packages])

        except Exception as pipinsterr:
            print(H3 + str(pipinsterr) + misc.END)
            return None

        if code != 0:
            erred_python2.append(packages)

        else:
            continue

    erred_perl = []
    for modules in perl:
        try:
            code = subprocess.call(['cpan', modules])

        except Exception as cpanerr:
            print(H3 + str(cpanerr) + misc.END)
            return None

        if code != 0:
            erred_perl.append(modules)

        else:
            continue

    if len(erred_binary) != 0 or len(erred_python3) != 0 or len(erred_python2) != 0:
        print(H3 + "Some binaries/modules cannot be installed:" + misc.END)
        print()
        print("===BINARIES===")
        for bins in erred_binary:
            print("[*] " + bins)

        print()
        print("===PYTHON 3===")
        for pies in erred_python3:
            print("[*] " + pies)

        print()
        print("===PYTHON 2===")
        for pies in erred_python2:
            print("[*] " + pies)

        print()
        print("===PERL===")
        for modules in erred_perl:
            print("[*] " + modules)

        print()
        print(H2 + "Please manually install the required binaries/modules." + misc.END)
        print()
        misc.programFunctions().pause()
        return None

    """
    process = "3"

    print(misc.CB + "Installing dependency files... (1/" + process + ")\n" + misc.CW)
    if sys.platform == 'windows' or sys.platform == 'nt':
        print("[i] Can't install binaries on Windows. Please install them manually.")
    
    else:
        subprocess.call(["bash", "instdeps.bash"])

    print(misc.CB + "Installing python modules... (2/" + process + ")\n" + misc.CW)
    os.system("pip install -r python_requirements")

    print(misc.CB + "Installing perl modules... (3/" + process + ")\n" + misc.CW)
    os.system("cpan threads Thread Net WWW Getopt Socket IO Strict Warnings Config Term XML String DotDotPwn threads::shared Thread::Queue WWW::Mechanize")
    print(misc.FB + misc.FI + misc.CB + "Performing a dependency update... Done!" + misc.FR + misc.CW)
    """

def prog_update(global_variables, DEBUGGING):
    fullupdate.update(global_variables, DEBUGGING)
