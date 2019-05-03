# -*- coding: utf-8 -*-

"""
Archarios Framework :: The Novice's Ethical Hacking Framework
Copyright(C) 2018-2019 :: Catayao56 <Catayao56@gmail.com>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

objects = ['phrases']

from random import randint


def phrases():
    phrases = [
        "A lot of hacking is playing with other people, \
you know, getting them to do strange things.",
        "When solving problems, dig at the roots instead \
of just hacking at the leaves.",
        "Most hackers are young because young people tend \
to be adaptable. As long as you remain adaptable, \
you can always be a good hacker.",
        "Hacking is fun if you're a Hacker",
        "Behind every successful Coder there an even more \
successful De-coder to understand that code",
        "Hacking just means building something quickly or \
testing the boundaries of what can be done",
        "Hackers are not crackers",
        "If you give a hacker a new toy, the first thing \
he'll do is take it apart to figure out how it works.",
        "Press any key... no, no, no, NOT THAT ONE!"
    ]
    result = phrases[randint(0, (len(phrases) - 1))]
    return result
