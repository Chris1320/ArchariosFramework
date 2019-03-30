#!/usr/bin/env python3
#coding=utf-8

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

import os
import sys
from time import sleep as timeout
from subprocess import getstatusoutput as gso


class testEnvLinux:

    def __init__(self, newenv=True):
        self.newenv = newenv
        self.job_no = 0
        self.result = [0, '']
        self.retcode = 0
        self.justContinue = False
        self.report = []
        self.rootdir = ''
        self.CG = ''
        self.CY = ''
        self.CR = ''
        self.CGR = ''
        self.END = ''

        self.py36 = 'test-env-3.6'

    def main(self, *args):
        self.createEnvironment()
        stages = []
        for arg in args:
            stages.append(arg)

        iterate = 0
        for stage in stages:
            iterate += 1
            print(self.CGR, "[i] Running stage #" + str(iterate), self.END)
            for command in stage:
                if not self.justContinue:
                    self.run(command)

                else:
                    self.report.append((-1, 'Skipped by CI Emulator.'))

            self.justContinue = False
            continue

        rc = self.get_results()
        if not self.newenv:
            if gso('git stash pop')[0] == 0:
                sys.exit(rc)

            else:
                print(self.CR, "[i] Cannot pop previous stash! Please\
 manually type 'git stash pop' to get back\
 to work.", self.END)
                sys.exit(rc + 1)

        else:
            sys.exit(rc)

    def run(self, command):
        self.job_no += 1
        print(self.CG, "$ " + command, self.END)
        if command.startswith('cd '):
            os.chdir(command.partition('cd ')[2])

        else:
            self.result = (os.system(command), '')

        print()
        if self.result[0] != 0:
            print(self.CR, "Job #{} failed! Exited with code\
 #{}".format(str(self.job_no),
                        str(self.result[0])), self.END)
            self.retcode = 1
            self.justContinue = True

        else:
            self.retcode = 0

        self.report.append(self.result)
        timeout(1)
        return self.retcode

    def createEnvironment(self, create_new_environment=True):
        if self.newenv:
            if not os.path.exists(self.py36):
                print(self.CGR, "[i] Creating Environment...", self.END)
                os.mkdir(self.py36)

            else:
                print(self.CGR, "[i] Reusing Previous\
 Environment...", self.END)
                print(self.CGR, "[i] Remove {} or run with \
`--recreate` switch to recreate virtual environment...".format(self.py36))

            os.chdir(self.py36)

        else:
            print(self.CY, "[i] Not testing on a\
 virtual environment!", self.END)
            if gso('git stash push')[0] == 0:
                pass

            else:
                print(self.CR, "[i] Cannot stash\
 current changes! Please manually")
                print("stash or commit your current\
 changes to continue.", self.END)
                sys.exit(6)

        self.rootdir = os.getcwd()
        print(self.CGR, "[i] Environment set!\
 Now starting to test...", self.END)
        timeout(1)

    def get_results(self):
        print('\n\n')
        print(self.CGR, '=' * 25, "Results:", '=' * 25, self.END)
        iterator = 0
        for result in self.report:
            iterator += 1
            if result[0] == 0:
                retcode = 0
                print(self.CG, "Job #{} exited\
 with code ".format(
                            str(iterator)) +
                        str(result[0]) + "!", self.END)
                print()
                print("="*50)
                """
                print(result[1])
                print("="*50)
                """
                print()

            else:
                retcode = 1
                print(self.CR, "Job #{} exited with\
 code ".format(str(iterator)) + str(result[0]) + "!", self.END)
                print()
                print("="*50)
                """
                print(result[1])
                print("="*50)
                """
                print()

        self.success_percentage = 0
        no_of_jobs = len(self.report)
        one = 100 / no_of_jobs
        for result in self.report:
            if result[0] == 0:
                self.success_percentage += one

            else:
                pass

        if self.success_percentage < 0 or self.success_percentage > 100:
            print(self.CGR + "Error calculating test success rate!")

        else:
            print(self.CGR + "Test Result: {0}% success (over 100%)".format(
                self.success_percentage) + self.END)
        print()
        return(retcode)


def run():
    print()
    for arg in sys.argv:
        if arg.lower() == '--recreate':
            gso('rmdir /s ' + testEnvLinux().py36)
            gso('dir /b')
            recreates = "[Recreate Virtual Environment]"

        else:
            recreates = ""

        if arg.lower() == '--no_virtualenv':
            newenv = False
            newenvs = "[No Virtual Environment]"

        else:
            newenv = True
            newenvs = ""

    if newenv:
        # Write pipeline here if you will use virtual environment.
        setup = ['dir', 'xcopy ..\src .\Archarios /O /X /E /H /K /Y', 'dir', 'cd Archarios', 'echo %cd%']
        test = ['python archariosframework.py --test']
        cleanup = ['cd ..', 'rmdir Archarios /s']

    else:
        # Write pipeline here if you will NOT use virtual environment.
        setup = ['dir', 'cd src', 'echo %cd%']
        test = ['python archariosframework.py --test']
        cleanup = []

    print("{0} Activated switches: {1} {2}".format(sys.argv[0],
        newenvs, recreates))
    testEnvLinux(newenv).main(setup, test, cleanup)


if __name__ == '__main__':
    if os.name == 'nt':
        run()

    else:
        run()
