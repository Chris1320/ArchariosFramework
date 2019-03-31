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

objects = ["ConfigHandler()", "ConfigHandler().get", "ConfigHandler().verify"]

import os
import sys

import time

from core import misc
from core import error
from core import exceptions

class ConfigHandler:
    """
    class ConfigHandler():
        The class containing methods to use the configuration file.
    """

    def __init__(self, config_path="data/config.dat"):
        """
        def __init__():
            The initialization method for ConfigHandler() class.
        """
        
        self.config_path = config_path

    def _open_config_file(self):
        """
        def _open_config_path():
            Open the config file.
        """

        try:
            with open(self.config_path, 'r') as fopen:
                data = fopen.read()

        except(FileNotFoundError, IOError, EOFError,
                PermissionError, IsADirectoryError):
            return exceptions.ConfigFileIOError("Error reading the configuration file!")

        else:
            # print(data)  # DEV0005
            data = misc.ProgramFunctions().base64_decode(data)
            return str(data.decode())

    def _save_config_file(self, config_data):
        """
        def _save_config_file():
            Save the config file.
        """

        try:
            with open(self.config_path, 'w') as fopen:
                data = fopen.write('')
                
        except(FileNotFoundError, IOError, EOFError,
               PermissionError, IsADirectoryError):
            return exceptions.ConfigFileIOError("Error writing to the configuration file!")
        
        else:
            try:
                with open(self.config_path, 'w') as fopen:
                    data = fopen.write(str(misc.ProgramFunctions().base64_encode(config_data)).decode())
                
            except(FileNotFoundError, IOError, EOFError,
                   PermissionError, IsADirectoryError):
                return exceptions.ConfigFileIOError("Error writing to the configuration file!")
            
            else:
                return 0
            
    def get(self, data=None):
        """
        def get():
            Get data from config file.
        """
        
        contents = self._open_config_file()
        if data is None:
            return contents.split('\n')
        
        else:
            # print(contents)  # DEV0005
            contents = contents.split('\n')
            for content in contents:
                if content.startswith('#'):
                    continue
                
                elif content.startswith(data + '='):
                    return content.replace('\n', '').partition('=')[2]
                
                else:
                    continue

                
    def set(self, variable=None, value=None):
        """
        def set():
            Set a new value for `variable`.
        """
        
        if variable is None or value is None:
            printer.Printer().print_with_status(error.ErrorClass().ERROR0011(), 2)
            return 11
        
        else:
            try:
                variable = str(variable)
                value = str(value)
                
            except(TypeError, ValueError):
                printer.Printer().print_with_status(error.ErrorClass().ERROR0011(), 2)
                return 11
        
            else:
                contents = self._open_config_file()
                new_config = []
                for content in contents:
                    if content.startswith('#'):
                        new_config.append(content)
                    
                    elif content.startswith(variable + '='):
                        new_config.append(variable + '=' + value + '\n')
                        
                    else:
                        new_config.append(content)
                        
                try:
                    self._save_config_file()
                    
                except Exception as error:
                    print(error)
                    return 1
                    
                else:
                    return 0
                
    def verify(self):
        """
        def verify():
            Verify configuration file.
        """
        
        contents = self._open_config_file()
        # print(contents)  # DEV0005
        if type(contents) is not str:
            return [2,]
        
        contents = contents.split('\n')
        
        warnings = []
        errors = []
        
        line = 0
        
        for content in contents:
            line += 1
            # print(content)  # DEV0005
            # time.sleep(1)  # DEV0005
            if '=' not in content and not content.startswith('#') and content != '':
                errors.append("Invalid statement `{0}` (line {1})".format(content, str(line)))

            if content.startswith("#") or content == '':
                continue
            
            elif content.startswith("exclude_list="):
                continue
            
            elif content.startswith("text_editor="):
                continue

            elif content.startswith("file_explorer="):
                continue

            elif content.startswith("username="):
                continue

            elif content.startswith("password="):
                continue

            elif content.startswith("rootuser="):
                continue

            elif content.startswith("rootpass="):
                continue
            
            else:
                if "Invalid statement `{0}` (line {1})".format(content, str(line)) not in errors:
                    warnings.append("Unknown statement `{0}` (line {1})".format(content, str(line)))
                    continue
                
        if len(errors) == 0 and len(warnings) == 0:
            code = 0
            
        else:
            code = 1
                        
        return [code, errors, warnings]