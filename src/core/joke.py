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

from random import *

def joke():
    joke1 = "I like telling UDP jokes because I don't care if you don't get them."
    joke2 = "CAPS LOCK - Preventing Login Since 1980."
    joke3 = "In a world without fences and walls, who needs Gates and Windows?"
    joke4 = "If at first you don\'t succeed; call it version 1.0."
    joke5 = "Programmers are tools for converting caffeine into code."
    joke6 = "Hacking is like s**. You get in, you get out, and hope that you didn\'t leave something that can be traced back to you."
    joke7 = "!false - its funny because its true"
    joke8 = "<joke>Joke Here</joke>"
    joke9 = "Hide & Seek champion (Hackers vs. FBI championship) -- Since 1958"
    headers = [joke1, joke2, joke3, joke4, joke5, joke6, joke7, joke8, joke9]
    result =  headers[randint(0,8)]
    return result
