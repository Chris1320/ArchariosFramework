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

# A python implementation of cowsay
# <http://www.nog.net/~tony/warez/cowsay.shtml>
# Copyright 2011 Jesse Chan-Norris <jcn@pith.org>
# Licensed under the GNU LGPL version 3.0

# NOTE: Modified by Catayao56

import textwrap

objects = ['cowsay', '_build_cow', '_build_bubble', '_normalize_text', '_get_border']

def cowsay(phrase, length=40):
    """
    def cowsay():
        Create a cow saying something.

        :param phrase: The phrase the cow will say.
        :type str:

        :param length: Maximum characters in a line.
        :type int:

        :returns: cowsay
        :return type: str
    """

    return(_build_bubble(phrase, length) + _build_cow())


def _build_cow():
    """
    def build_cow():
        Return a cow.
    """

    cow_body = """
         \   ^__^
          \  (oo)\_______
             (__)\       )\/\\
                 ||----w |
                 ||     ||
    """

    return cow_body


def _build_bubble(phrase, length=40):
    """
    def build_bubble():
        Build a bubble containing <phrase>.

        :param phrase: The phrase to be in the bubble.
        :type str:

        :param length: Length of each line in the bubble.
        :type int:

        :returns: bubble
        :return type: str
    """

    bubble = []
    lines = _normalize_text(phrase, length)
    bordersize = len(lines[0])
    bubble.append("  " + "_" * bordersize)
    for index, line in enumerate(lines):
        border = _get_border(lines, index)
        bubble.append("{0} {1} {2}".format(border[0], line, border[1]))

    bubble.append("  " + "-" * bordersize)
    return("\n".join(bubble))


def _normalize_text(phrase, length):
    """
    def normalize_text():
        Normalize <phrase>.

        :param phrase: Phrase to normalize.
        :type str:

        :param length: Number of characters on each line.
        :type int:

        :returns: normalized text
        :return type: str
    """

    lines = textwrap.wrap(phrase, length)
    maxlen = len(max(lines, key=len))
    return[line.ljust(maxlen) for line in lines]


def _get_border(lines, index):
    """
    def get_border():
        Get the border for the cow.
    """

    if len(lines) < 2:
        return["<", ">"]

    elif index == 0:
        return["/", "\\"]

    elif index == len(lines) - 1:
        return["\\", "/"]

    else:
        return["|", "|"]
