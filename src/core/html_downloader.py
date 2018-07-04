#!/usr/bin/python3

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

import sys, urllib.request

def getHTML(target):
    try:
        if 'http' not in target:
            target = 'http://' + target

        page = urllib.request.urlopen(target)
        return page

        for line in page:
            print(str(line, encoding='utf-8'), end='')
        print("\n\n\n")

    except Exception as error:
        return error
