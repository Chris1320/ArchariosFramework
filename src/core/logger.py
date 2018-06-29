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
from time import asctime

def log(TYPE=9999, MSG="Logger called.", LOGFILE="logfile.txt", SESSION_ID=123456, DEBUGGING=False):
    TYPE = int(TYPE)
    line = '=' * 50
    date = 'Time: ' + asctime()
    session = "Session ID: "

    # Legacy algorithm to log...
    # boundary = os.system('echo ' + line + " >> " + LOGFILE)
    # date = os.system("date >> " + LOGFILE)

    ### Basic types ###
    # 0 == Normal message
    # 1 == Warning message
    # 2 == Error message

    ### Extended Types ###
    # 3 == Important message
    # 4 == Serious warning message
    # 5 == Fatal error message

    if TYPE == 0:
        ICO = '[   INF   ]: '

    elif TYPE == 1:
        ICO = '[   WRN   ]: '

    elif TYPE == 2:
        ICO = '[   ERR   ]: '

    elif TYPE == 3:
        ICO = '[***INF***]: '

    elif TYPE == 4:
        ICO = '[***WRN***]: '

    elif TYPE == 5:
        ICO = '[***ERR***]: '

    else:
        ICO = '[**UNK**]: '

    # Old algorithm to log...
    """
    boundary
    date
    message = os.system('echo ' + ICO + MSG + " >> " + LOGFILE)
    boundary
    """

    # New algorithm to log...
    try:
        open(LOGFILE, 'r').read()
        open(LOGFILE, 'r').close()

    except FileNotFoundError:
        open(LOGFILE, 'w').write('')
        open(LOGFILE, 'w').close()

    with open(LOGFILE, 'a') as f:
        f.write(line + '\n')
        f.write(date + '\n')
        f.write(session + str(SESSION_ID) + '\n')
        f.write(ICO + MSG + '\n')
        f.write('\n')

    if DEBUGGING == True or DEBUGGING == True:
        print("[DEBUG]: Operation logged: " + ICO + MSG)
