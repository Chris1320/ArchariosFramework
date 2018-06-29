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
import traceback
from core import misc
from core import error

def list(module_path):
    COLOR_SUPPORT = misc.programFunctions().cli_color_support()
    if COLOR_SUPPORT == True:
        cw = '\033[0m'                         #  white  (normal)
        cb = '\033[34m'                        #  blue   (highlights)

        cg = '\033[32m'                        #  green  (Stable)
        cy = '\033[33m'                        #  yellow (Experimental)
        cr = '\033[31m'                        #  red    (Unstable)
        cgr = '\033[37m'                       #  gray   (Not yet Implemented)
        cp = '\033[35m'                        #  purple (Unknown status)
    
        # Font types
        fr = '\033[0m'                         #  regular (Modules)
        fb = '\033[1m'                         #  bold    (Sections)
        fi = '\033[3m'                         #  italic  (Sub-Sections)

    else:
        cw = ''
        cb = ''

        cg = ''
        cy = ''
        cr = ''
        cgr = ''
        cp = ''

        fr = ''
        fb = ''
        fr = ''

    print(cg + fb + fi + "===Shadow Suite Modules and Frameworks===\n\n" + cb + fr)
    print(cw + fb + "[i] The stability of the tools is color-coded:" + cw)
    print(cg + "\tStable" + cw)
    print(cy + "\tExperimental" + cw)
    print(cr + "\tUnstable" + cw)
    print(cgr + "\tNot Yet Implemented (NYI)" + cw)
    print(cp + "\tUnknown Status" + cw)
    print(cr + fb + "\tModule with Error" + cw + fr)
    print("\n\n")

    modules = os.listdir(module_path)
    module_iterator = 0
    # 0 == Stable
    # 1 == Experimental
    # 2 == Unstable
    # 3 == Not yet implemented/working
    for module in modules:
        #print(modules) # DEV0005: For debugging purposes only
        #print(module) # DEV0005: For debugging purposes only
        module = module_path + module
        if module.lower().endswith('.py') and misc.programFunctions().isfile(module):
            imodule = module.replace('.py', '').replace('/', '.')
            try:
                ms = importlib.import_module(imodule)

            except ModuleNotFoundError:
                pass

            except:
                pass

            try:
                module_iterator += 1
                module = module.replace('.py', '')
                status = ms.module_status
                if status == 0:
                    print("[" + str(module_iterator) +"] " + cg + module.replace(module_path, '') + " :: " + ms.info['desc'] + cw)
                    print()

                elif status == 1:
                    print("[" + str(module_iterator) +"] " + cy + module.replace(module_path, '') + " :: " + ms.info['desc'] + cw)
                    print()

                elif status == 2:
                    print("[" + str(module_iterator) +"] " + cr + module.replace(module_path, '') + " :: " + ms.info['desc'] + cw)
                    print()

                elif status == 3:
                    print("[" + str(module_iterator) +"] " + cgr + module.replace(module_path, '') + " :: " + ms.info['desc'] + cw)
                    print()

                else:
                    print("[" + str(module_iterator) +"] " + cp + module.replace(module_path, '') + " :: " + ms.info['desc'] + cw)
                    print()

            except(ImportError, UnboundLocalError, AttributeError):
                print("[" + str(module_iterator) +"] " + cr + fb + module.replace(module_path, '') + " :: (ERROR WHILE FETCHING INFO)" + cw + fr)
                print()

        else:
            continue

        try:
            del ms

        except:
            pass

        #print(matched_modules) # DEV0005: For debugging purposes only

def count(module_path):
    modules = os.listdir(module_path)
    module_count = [0, 0, 0, 0, 0, 0, 0]
    #               ^  ^  ^  ^  ^  ^  ^
    #               0  1  2  3  4  5  6
    #
    # 0=All, 1=Stable, 2=Experimental, 3=Unstable, 4=NYI/W, 5=UNK, 6=Module with err
    #print(modules) # DEV0005: For debugging purposes only
    for module in modules:
        #print(module) # DEV0005: For debugging purposes only
        imodule_path = module_path.replace('/', '.')
        imodule = module.replace('.py', '')
        try:
            ms = importlib.import_module(imodule_path + imodule)
        
        except(ImportError, ModuleNotFoundError):
        #except AttributeError:
            pass

        except:
            pass
        
        try:
            #print(module) # DEV0005: For debugging purposes only
            #print(module.lower().endswith('.py') and misc.programFunctions().isfile(module_path + module)) # DEV0005: For debugging purposes only
            if module.lower().endswith('.py') and misc.programFunctions().isfile(module_path + module):
                module_count[0] += 1
                module = module.replace('.py', '').replace('.Py', '').replace('.pY', '').replace('.PY', '')
                status = ms.module_status
                if status == 0:
                    module_count[1] += 1
                
                elif status == 1:
                    module_count[2] += 1
                
                elif status == 2:
                    module_count[3] += 1
                
                elif status == 3:
                    module_count[4] += 1
                
                else:
                    module_count[5] += 1
                
            else:
                continue
            
        except:
            module_count[6] += 1
            
        try:
            del ms
        
        except:
            pass

    return module_count
