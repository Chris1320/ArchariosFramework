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
import importlib
import signal

from core import error
from core import misc
from core import version
from core import multitasking

def api(criteria, module_path):
    criteria = criteria.split(',')
    #print(criteria) # DEV0005: For debugging purposes only

    modules = os.listdir(module_path)
    matched_modules = []
    #print(modules) # DEV0005: For debugging purposes only
    module_iterator = 0
    module_path = module_path.replace('/', '.')
    for module in modules:
        if '.py' in module or '.Py' in module or '.pY' in module or '.PY' in module:
            module = module.replace('/', '.').replace('.py', '')
            try:
                ms = importlib.import_module(module_path + module)
                module_iterator += 1
                module = module.replace('.py', '')
                status = ms.category
                #print(status) # DEV0005: For debugging purposes only

            except ModuleNotFoundError:
                continue

            for category in status:
                for crit in criteria:
                    #print(category) # DEV0005: For debuging purposes only
                    if category.replace(' ', '') in crit:
                        #print(module + "    " + str(matched_modules)) # DEV0005: For debugging purposes only
                        if module in matched_modules:
                            continue

                        else:
                            matched_modules.append(module)
                            if ms.module_status == 0:
                                print(misc.CG + module + " :: " + ms.info['desc'] + misc.CW)
                                print()

                            elif ms.module_status == 1:
                                print(misc.CY + module + " :: " + ms.info['desc'] + misc.CW)
                                print()

                            elif ms.module_status == 2:
                                print(misc.CR + module + " :: " + ms.info['desc'] + misc.CW)
                                print()

                            elif ms.module_status ==3:
                                print(misc.NYI + module + " :: " + ms.info['desc'] + misc.CW)
                                print()

                            else:
                                print(misc.CP + module + " :: " + ms.info['desc'] + misc.CW)
                                print()

                            break

                    else:
                        #print(str(category) + " not in " + str(criteria)) # DEV0005: For debugging purposes only
                        continue

                else:
                    #print(module + " not a package")
                    continue
