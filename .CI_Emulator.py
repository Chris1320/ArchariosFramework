#!/usr/bin/env python3
import os
import sys
import importlib
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
        self.CG   = '\033[32m'
        self.CY   = '\033[33m'
        self.CR   = '\033[31m'
        self.CGR  = '\033[90m'
        self.END  = '\033[0m'

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
                print(self.CR, "[i] Cannot pop previous stash! Please manually type 'git stash pop' to get back to work.", self.END)
                sys.exit(rc + 1)

        else:
            sys.exit(rc)

    """
    def run(self, command):
        self.job_no += 1
        print(self.CG, "$ " + command, self.END)
        if command.startswith('cd '):
            os.chdir(command.partition('cd ')[2])

        else:
            self.result = gso(command)

        print(self.result[1])
        print()
        if self.result[0] != 0:
            print(self.CR, "Job #{} failed! Exited with code #{}".format(str(self.job_no), str(self.result[0])), self.END)
            self.retcode = 1
            self.justContinue = True

        else:
            self.retcode = 0

        self.report.append(self.result)
        timeout(1)
        return self.retcode
    """

    def run(self, command):
        self.job_no += 1
        print(self.CG, "$ " + command, self.END)
        if command.startswith('cd '):
            os.chdir(command.partition('cd ')[2])

        else:
            self.result = (os.system(command), '')

        print()
        if self.result[0] != 0:
            print(self.CR, "Job #{} failed! Exited with code #{}".format(str(self.job_no), str(self.result[0])), self.END)
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
                gso('virtualenv --python=python3.6 ' + self.py36)

            else:
                print(self.CGR, "[i] Reusing Previous Environment...", self.END)
                print(self.CGR, "[i] Remove {} to recreate...".format(self.py36))

            os.chdir(self.py36)

        else:
            print(self.CY, "[i] Not testing on a virtual environment!", self.END)
            if gso('git stash push')[0] == 0:
                pass

            else:
                print(self.CR, "[i] Cannot stash current changes! Please manually")
                print("stash or commit your current changes to continue.", self.END)
                sys.exit(6)

        self.rootdir = os.getcwd()
        print(self.CGR, "[i] Environment set! Now starting to test...", self.END)
        timeout(1)

    def get_results(self):
        print('\n\n')
        print(self.CGR, '=' * 25, "Results:", '=' * 25, self.END)
        iterator = 0
        for result in self.report:
            iterator += 1
            if result[0] == 0:
                retcode = 0
                print(self.CG, "Job #{} exited with code ".format(str(iterator)) + str(result[0]) + "!", self.END)
                print()
                print("="*50)
                """
                print(result[1])
                print("="*50)
                """
                print()

            else:
                retcode = 1
                print(self.CR, "Job #{} exited with code ".format(str(iterator)) + str(result[0]) + "!", self.END)
                print()
                print("="*50)
                """
                print(result[1])
                print("="*50)
                """
                print()

        print()
        return(retcode)

def run():
    if 'recreate' in sys.argv:
        gso('rm -rf ' + testEnvLinux().py36)

    if 'no_virtualenv' in sys.argv:
        newenv = False

    else:
        newenv = True

    if newenv:
        # Write pipeline here if you will use virtual environment.
        setup = ['ls', 'cp -r ../src ./Archarios', 'ls', 'cd Archarios', 'pwd']
        test = ['python3 archarios_framework.py --test']
        cleanup = ['cd ..', 'rm -rf Archarios/']

    else:
        # Write pipeline here if you will NOT use virtual environment.
        setup = ['ls', 'cd src', 'pwd']
        test = ['python3 archarios_framework.py --test']
        cleanup = []

    testEnvLinux(newenv).main(setup, test, cleanup)

if __name__ == '__main__':
    if os.name == 'nt':
        pass

    else:
        run()
