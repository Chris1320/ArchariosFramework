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

def list(service_path):
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
        fr = '\033[0m'                         #  regular (Services)
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

    print(cg + fb + fi + "===Shadow Suite Services and Frameworks===\n\n" + cb + fr)
    print(cw + fb + "[i] The stability of the tools is color-coded:" + cw)
    print(cg + "\tStable" + cw)
    print(cy + "\tExperimental" + cw)
    print(cr + "\tUnstable" + cw)
    print(cgr + "\tNot Yet Implemented (NYI)" + cw)
    print(cp + "\tUnknown Status" + cw)
    print(cr + fb + "\tService with Error" + cw + fr)
    print("\n\n")

    services = os.listdir(service_path)
    service_iterator = 0
    # 0 == Stable
    # 1 == Experimental
    # 2 == Unstable
    # 3 == Not yet implemented/working
    for service in services:
        #print(services) # DEV0005: For debugging purposes only
        #print(service) # DEV0005: For debugging purposes only
        service = service_path + service
        if service.lower().endswith('.py') and misc.programFunctions().isfile(service):
            iservice = service.replace('.py', '').replace('/', '.')
            #print(iservice) # DEV0005
            #"""
            try:
                ms = importlib.import_module(iservice)

            except ModuleNotFoundError:
                pass

            except:
                pass
            #"""

            try:
                service_iterator += 1
                service = service.replace('.py', '')
                status = ms.service_status
                if status == 0:
                    print("[" + str(service_iterator) +"] " + cg + service.replace(service_path, '') + " :: " + ms.info['desc'] + cw)
                    print()

                elif status == 1:
                    print("[" + str(service_iterator) +"] " + cy + service.replace(service_path, '') + " :: " + ms.info['desc'] + cw)
                    print()

                elif status == 2:
                    print("[" + str(service_iterator) +"] " + cr + service.replace(service_path, '') + " :: " + ms.info['desc'] + cw)
                    print()

                elif status == 3:
                    print("[" + str(service_iterator) +"] " + cgr + service.replace(service_path, '') + " :: " + ms.info['desc'] + cw)
                    print()

                else:
                    print("[" + str(service_iterator) +"] " + cp + service.replace(service_path, '') + " :: " + ms.info['desc'] + cw)
                    print()

            except(ImportError, UnboundLocalError, AttributeError):
                traceback.print_exc() # DEV0005
                print("[" + str(service_iterator) +"] " + cr + fb + service.replace(service_path, '') + " :: (ERROR WHILE FETCHING INFO)" + cw + fr)
                print()

        else:
            continue

        try:
            del ms

        except:
            pass

        #print(matched_services) # DEV0005: For debugging purposes only

def count(service_path):
    services = os.listdir(service_path)
    service_count = [0, 0, 0, 0, 0, 0, 0]
    #                ^  ^  ^  ^  ^  ^  ^
    #                0  1  2  3  4  5  6
    #
    # 0=All, 1=Stable, 2=Experimental, 3=Unstable, 4=NYI/W, 5=UNK, 6=Service with err
    #print(services) # DEV0005: For debugging purposes only
    for service in services:
        #print(service) # DEV0005: For debugging purposes only
        iservice_path = service_path.replace('/', '.')
        iservice = service.replace('.py', '')
        try:
            ms = importlib.import_service(iservice_path + iservice)
        
        except(ImportError, ModuleNotFoundError):
        #except AttributeError:
            pass

        except:
            pass
        
        try:
            #print(service) # DEV0005: For debugging purposes only
            #print(service.lower().endswith('.py') and misc.programFunctions().isfile(service_path + service)) # DEV0005: For debugging purposes only
            if service.lower().endswith('.py') and misc.programFunctions().isfile(service_path + service):
                service_count[0] += 1
                service = service.replace('.py', '').replace('.Py', '').replace('.pY', '').replace('.PY', '')
                status = ms.service_status
                if status == 0:
                    service_count[1] += 1
                
                elif status == 1:
                    service_count[2] += 1
                
                elif status == 2:
                    service_count[3] += 1
                
                elif status == 3:
                    service_count[4] += 1
                
                else:
                    service_count[5] += 1
                
            else:
                continue
            
        except:
            service_count[6] += 1
            
        try:
            del ms
        
        except:
            pass

    return service_count
