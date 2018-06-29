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


class ASCII_Graphs():

    def __init__(self):
        pass

    def percent_bar(self, percent):
        if not percent:
            raise ValueError("Needs one argument: percent(int 0-100)")

        else:
            if percent < 1 or percent > 100:
                raise ValueError("Needs one argument: percent(int 0-100)")

            else:
                if sys.platform == 'windows' or sys.platform == 'nt':
                    raise PlatformError("Windows Systems are not *yet* supported...")

                else:
                    percent = percent // 2
                    bar = '|' + ('=' * percent)
                    empty = 50 - percent
                    bar = bar + ' ' * empty + '|'
                    return bar
