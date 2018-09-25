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

objects = ['TestingClass']

import os
import sys
import time
import hashlib
import traceback

from core import error
from core import printer
from core import asciigraphs
from importlib import import_module as imprt


class TestingClass:
    """
    class TestingClass():
        The testing class of Archários Framework.
    """

    def __init__(self, name):
        """
        def __init__():
            Initialization method for testing.

            :param name: Name of program to be displayed on screen.
            :type str:
        """

        self.main_module = sys.argv[0]
        self.core_modules = os.listdir('core')
        self.data_files = os.listdir('data')
        self.third_party_modules = os.listdir('modules')
        self.output_files = os.listdir('output')
        self.static_files = os.listdir('static')
        self.template_files = os.listdir('templates')

        self.file_integrity_filename = "data/integrity.lst"
        self.excluded = ['data/logfile.log', 'data/notes.txt',
                'data/history.log']
        self.name = str(name)

    def main(self):
        """
        def main():
            The main method of TestingClass() class.
        """

        test_results = 0
        self.FileIntegrityTest()
        test_results += self.test(self.main_module)
        for module in self.core_modules:
            test_result = self.test("core/" + module)
            # print(test_result, test_results)
            if test_result is not None:
                test_results += test_result
                continue

            else:
                continue

        for module in self.third_party_modules:
            test_result = self.test("modules/" + module)
            if test_result is not None:
                test_results += test_result
                continue

            else:
                continue

        self.test_non_ASCII()
        print()

        return test_results

    def test(self, module):
        self.erred = 0
        try:
            os.listdir(module)

        except(NotADirectoryError, FileNotFoundError):
            try:
                if os.path.isfile(module):
                    pass

                else:
                    return None

            except NotImplementedError:
                return None

        except NotImplementedError:
            return None

        else:
            return None

        # print(module)
        module = module.replace(os.sep, '.')
        module = module[::-1]
        # print(module)
        module = module.partition('.')[2]
        # print(module)
        module = module[::-1]
        # print(module)
        module_import = imprt(module)
        asciigraphs.ASCIIGraphs().animated_loading_screen(1,
                'Preparing to test {0} (`{1}` module)...'.format(self.name,
                    module),
                'loading', 0.10)
        iterator = 1
        try:
            module_objs = module_import.objects

        except Exception as err:
            print('\n', err)
            print()
            print("=" * 15, "TRACEBACK", "=" * 15)
            print(traceback.format_exc())
            print("=" * 15, "TRACEBACK", "=" * 15)
            self.erred += 1
            try:
                with open('data/tracebacks.log', 'a') as fopen:
                    fopen.write(traceback.format_exc() + '\n')
                    fopen.write(('=' * 50) + '\n')

            except(FileNotFoundError, IOError, EOFError):
                print("Cannot write to data/tracebacks.log!")

        else:
            for objct in module_objs:
                try:
                    asciigraphs.ASCIIGraphs().progress_bar_manual("Testing \
{0}...".format(module), iterator, len(module_objs), 40)
                    eval("module_import." + objct)
                    iterator += 1
                    time.sleep(0.25)

                except Exception as err:
                    print('\n', err)
                    print()
                    print("=" * 15, "TRACEBACK", "=" * 15)
                    print(traceback.format_exc())
                    print("=" * 15, "TRACEBACK", "=" * 15)
                    self.erred += 1
                    try:
                        with open('data/tracebacks.log', 'a') as fopen:
                            fopen.write(traceback.format_exc() + '\n')
                            fopen.write(('=' * 50) + '\n')

                    except(FileNotFoundError, IOError, EOFError):
                        print("Cannot write to data/tracebacks.log!")

        print()
        return self.erred

    def test_non_ASCII(self):
        asciigraphs.ASCIIGraphs().animated_loading_screen(1,
                "Testing non-ASCII characters...", 'loading', 0.10)
        print()
        try:
            for char in ('é', 'ú', 'í', 'ó', 'π', 'á', 'đ', '₣', '£', 'ž', 'ç',
                'ñ', 'μ'):
                    printer.Printer().print_and_flush('\r' + char)
                    time.sleep(1)

        except(UnicodeDecodeError):
            print(error.ErrorClass().ERROR0008())
            return 1

        else:
            asciigraphs.ASCIIGraphs().animated_loading_screen(1,
                "Another bunch of non-ASCII characters... Emojis!", 'loading', 0.10)
            print()
            try:
                for emoji in ('☺', '😀', '😁', '😂', '😅', '😇', '😉', '😯', '😐',
                    '😑', '😕', '😠', '😬', '😢'):
                        printer.Printer().print_and_flush('\r' + emoji)
                        time.sleep(1)

            except(UnicodeDecodeError):
                print(error.ErrorClass().ERROR0008())
                return 1

            else:
                return 0

    def FileIntegrityTest(self, gen_no_test=False):
        """
        def FileIntegrityTest():
            Perform a file integrity test.

            :param gen_no_test: True, if you want to generate list but no test.
            :type bool:
        """

        # Check if integrity list exists.
        if not os.path.exists(self.file_integrity_filename) and not os.path.isfile(self.file_integrity_filename):
            printer.Printer().print_with_status(
                    "Generating Data Integrity List...", 0)
            with open(self.file_integrity_filename, 'w') as fwrite:
                   fwrite.write('')
            self.GenerateFileIntegrityList(self.main_module)
            for fil in self.core_modules:
                fil = 'core/' + fil
                if os.path.isfile(fil):
                    self.GenerateFileIntegrityList(fil)

            for fil in self.data_files:
                fil = 'data/' + fil
                if os.path.isfile(fil):
                    self.GenerateFileIntegrityList(fil)

            for fil in self.third_party_modules:
                fil = 'modules/' + fil
                if os.path.isfile(fil):
                    self.GenerateFileIntegrityList(fil)

            for fil in self.output_files:
                fil = 'output/' + fil
                if os.path.isfile(fil):
                    self.GenerateFileIntegrityList(fil)

            for fil in self.static_files:
                fil = 'static/' + fil
                if os.path.isfile(fil):
                    self.GenerateFileIntegrityList(fil)

            for fil in self.template_files:
                fil = 'templates/' + fil
                if os.path.isfile(fil):
                    self.GenerateFileIntegrityList(fil)

            printer.Printer().print_with_status(
                    "Data Integrity List generated!", 0)
            return "True string"  # Return a "special boolean" Whahaha

        # Check if user just wants to generate list.
        if gen_no_test is True:
            return True

        try:
            with open(self.file_integrity_filename, 'r') as fread:
                integrity_list = fread.readlines()

        except(FileNotFoundError, IOError, EOFError,
                PermissionError, UnicodeDecodeError):
            printer.Printer().print_with_status("Cannot read {0}!".format(
                    self.file_integrity_list), 2)
            return False

        else:
            good = 0
            erred = 0
            mismatch = 0
            mismatched = {}

            for pair in integrity_list:
                time.sleep(0.10)
                pair = pair.split('\n')
                pair = pair[0].partition(' :: ')
                new_hash = self.hash_file(pair[0])
                if pair[2].upper() == str(new_hash.upper()):
                    printer.Printer().print_with_status(
                    "The hash of {0} matched the \
checksum.".format(pair[0]), 0)
                    good += 1

                elif new_hash == 1:
                    printer.Printer().print_with_status(
                    "An error occured while calculating \
checksum for {0}.".format(pair[0]), 2)
                    erred += 1

                else:
                    printer.Printer().print_with_status(
                    "The hash of {0} doesn't match the \
checksum!".format(pair[0]), 1)
                    mismatch += 1
                    mismatched[pair[0]] = [pair[2].upper(), new_hash.upper()]

            if mismatch != 0 or erred != 0:
                print()
                printer.Printer().print_with_status("Errors found!", 1)
                print()
                for missed in mismatched:
                    print("Filename: {0} | Old Hash: {1} | New Hash: {2}".format(
                        missed, mismatched[missed][0], mismatched[missed][1]))
                    print()

                while True:
                    try:
                        ask_user = input("Do you want to continue? (y/n) > ")
                        if ask_user.lower() == 'y':
                            return True

                        elif ask_user.lower() == 'n':
                            return False

                        else:
                            continue

                    except(TypeError, ValueError, EOFError, KeyboardInterrupt):
                        continue

            else:
                print()
                printer.Printer().print_with_status(
                        "No errors found!", 0)
                return True

    def GenerateFileIntegrityList(self, fil):
        """
        def GenerateFileIntegrityList():
            Generate a File Integrity List.
        """

        if fil in self.excluded:
            return 0

        hashed = self.hash_file(fil)
        try:
            with open(self.file_integrity_filename, 'a') as fwrite:
                fwrite.write("{0} :: {1}\n".format(
                    fil, hashed))

        except(FileNotFoundError, IOError, EOFError,
                   PermissionError, UnicodeDecodeError):
            printer.Printer().print_with_status("Cannot write to {0}!".format(
                   self.file_integrity_list), 2)
            return 1

        else:
            return 0

    def hash_file(self, filename):
        """
        def hash_file():
            Return the hash of a file.
        """

        try:
            try:
                with open(filename, 'r') as fopen:
                    data = fopen.read()

            except(UnicodeDecodeError):
                with open(filename, 'rb') as fopen:
                    data = fopen.read()

        except(FileNotFoundError, IOError, EOFError,
                PermissionError, UnicodeDecodeError):
            printer.Printer().print_with_status("Cannot read {0}!".format(
                filename), 2)
            return 1

        else:
            # This is the only hash function used ;)
            return hashlib.sha256(data.encode()).hexdigest()
