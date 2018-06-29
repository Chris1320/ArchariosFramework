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

import sys

if sys.platform == 'linux' or sys.platform == 'darwin':
    # Colors with meanings
    CW   = '\033[0m'       # white           (normal)
    CR   = '\033[31m'      # red             (errors)
    CG   = '\033[32m'      # green           (main color)
    CY   = '\033[33m'      # yellow          (warnings)
    CB   = '\033[34m'      # blue            (highlights)
    CGR  = '\033[90m'      # gray            (questions)

    # Misc colors
    CP   = '\033[35m'      # purple
    CC   = '\033[36m'      # cyan
    CK   = ''              #'\003[8m'       # black DEV0001: NYW

    # Extended colors
    CLM  = '\033[95m'      # light magenta
    CLB  = '\033[94m'      # light blue
    CLG  = '\033[92m'      # light green
    CLY  = '\033[93m'      # light yellow
    CLR  = '\033[91m'      # light red
    CLC  = '\033[96m'      # light cyan
    CLGR = '\033[37m'      # light gray

    # Background Colors without meanings :p
    BW   = '\033[7m'       # white
    BR   = '\033[41m'      # red
    BG   = '\033[42m'      # green
    BY   = '\033[43m'      # yellow
    BB   = '\033[44m'      # blue
    BM   = '\033[45m'      # magenta
    BC   = '\033[46m'      # cyan
    BGR  = '\033[100m'     # gray

    BLGR = '\033[2m'       # light gray
    BLR  = '\033[101m'     # light red
    BLG  = '\033[102m'     # light green
    BLY  = '\033[103m'     # light yellow
    BLB  = '\033[104m'     # light blue
    BLM  = '\033[105m'     # light magenta
    BLC  = '\033[106m'     # light cyan
    BLW  = '\033[107m'     # light white?!?

    # Font types
    FR   = '\033[0m'       # regular
    FB   = '\033[1m'       # bold
    FI   = '\033[3m'       # italic
    FU   = '\033[4m'       # underline
    FE   = '\033[9m'       # erased

    END  = '\033[0m'       # I know... CW, FR and this are the same... I didn't realize it earlier...

else:
    # No color support on windows operating systems.
    CW = ''
    CR = ''
    CG = ''
    CY = ''
    CB = ''
    CGR = ''

    CP = ''
    CC = ''
    CK   = ''

    CLM  = ''
    CLB = ''
    CLG  = ''
    CLY = ''
    CLR = ''
    CLC  = ''
    CLGR = ''

    BW   = ''
    BR   = ''
    BG   = ''
    BY   = ''
    BB   = ''
    BM   = ''
    BC   = ''
    BGR  = ''

    BLGR = ''
    BLR  = ''
    BLG  = ''
    BLY  = ''
    BLB  = ''
    BLM  = ''
    BLC  = ''
    BLW  = ''

    FR = ''
    FB = ''
    FI = ''
    FU = ''
    FE = ''

    END = ''
