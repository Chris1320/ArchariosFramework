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

objects = []

import os
import sys

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
                data =  fopen.read()

        except(FileNotFoundError, IOError, EOFError,
                PermissionError, IsADirectoryError):
            return exceptions.ConfigFileIOError("Error reading the configuration file!")

        else:
            data = misc.ProgramFunctions().base64_decode(data)
            return data

    def _save_config_file(self):
        """
        def _save_config_file():
            Save the config file.
        """

        try:
