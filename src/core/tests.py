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

objects = ['TestingClass']

import os
import time
import traceback

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

        self.core_modules = os.listdir('core')

        self.name = str(name)
        self.faulty_modules = {}

    def main(self):
        """
        def main():
            The main method of TestingClass() class.
        """

        test_results = 0
        for module in self.core_modules:
            test_result = self.test("core/" + module)
            # print(test_result, test_results)
            if test_result is not None:
                test_results += test_result
                continue

            else:
                continue

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
