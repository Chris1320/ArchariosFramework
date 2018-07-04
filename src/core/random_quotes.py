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

from random import *
def quote():
    joke1 = "A lot of hacking is playing with other people, you know, getting them to do strange things."
    joke2 = "When solving problems, dig at the roots instead of just hacking at the leaves."
    joke3 = "Most hackers are young because young people tend to be adaptable. As long as you remain adaptable, you can always be a good hacker."
    joke4 = "Hacking is fun if you're a Hacker"
    joke5 = "Behind every successful Coder there an even more successful De-coder to understand that code"
    joke6 = "Hacking just means building something quickly or testing the boundaries of what can be done"
    joke7 = "Hackers are not crackers"
    joke8 = "If you give a hacker a new toy, the first thing he'll do is take it apart to figure out how it works."
    joke9 = "Press any key... no, no, no, NOT THAT ONE!"
    headers = [joke1, joke2, joke3, joke4, joke5, joke6, joke7, joke8, joke9]
    result = headers[randint(0,8)]
    return result
