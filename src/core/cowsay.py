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

# A python implementation of cowsay <http://www.nog.net/~tony/warez/cowsay.shtml>
# Copyright 2011 Jesse Chan-Norris <jcn@pith.org>
# Licensed under the GNU LGPL version 3.0

import sys
import textwrap

def cowsay(str, length=40):
	return build_bubble(str, length) + build_cow()

def build_cow():
	return """
         \   ^__^
          \  (oo)\_______
             (__)\       )\/\\
                 ||----w |
                 ||     ||
    """

def build_bubble(str, length=40):
	bubble = []

	lines = normalize_text(str, length)

	bordersize = len(lines[0])

	bubble.append("  " + "_" * bordersize)

	for index, line in enumerate(lines):
		border = get_border(lines, index)

		bubble.append("%s %s %s" % (border[0], line, border[1]))

	bubble.append("  " + "-" * bordersize)

	return "\n".join(bubble)

def normalize_text(str, length):
	lines  = textwrap.wrap(str, length)
	maxlen = len(max(lines, key=len))
	return [ line.ljust(maxlen) for line in lines ]

def get_border(lines, index):
	if len(lines) < 2:
		return [ "<", ">" ]

	elif index == 0:
		return [ "/", "\\" ]

	elif index == len(lines) - 1:
		return [ "\\", "/" ]

	else:
		return [ "|", "|" ]


	print(cowsay(sys.argv[1]))
