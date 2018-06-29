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

def quote():
    quote01 = "A lot of hacking is playing with other people, you know, getting them to do strange things."
    quote02 = "When solving problems, dig at the roots instead of just hacking at the leaves."
    quote03 = "Most hackers are young because young people tend to be adaptable. As long as you remain adaptable, you can always be a good hacker."
    quote04 = "Hacking is fun if you're a Hacker"
    quote05 = "Behind every successful Coder there\'s an even more successful De-coder to understand that code"
    quote06 = "Hacking just means building something quickly or testing the boundaries of what can be done"
    quote07 = "Hackers are not crackers"
    quote08 = "If you give a hacker a new toy, the first thing he'll do is take it apart to figure out how it works."
    quote09 = "Press any key... no, no, no, NOT THAT ONE!"

    tip01 = "Don't forget to do reconnaissance first before doing anything serious!"
    tip02 = "Nmap is the best tool to use when you need to scan for open ports. Nwrap automates the process!"
    tip03 = "There are so many tool that is included in Shadow Suite Framework so make sure to check them out!"
    tip04 = "Learn, Try, Rage, Retry..."
    tip05 = "Atleast 4GB of RAM is recommended."
    tip06 = "Python is the best language to start from."
    tip07 = "Use SQLMap for SQL Injection attacks."
    tip08 = "Use Hash Identifier to indentify the kind of a hash."
    tip09 = "Use ShadowCrack to crack encryptions and hashes."
    tip10 = "Shadow Repository has lots of wordlists! You can also use CUPP to generate your own wordlist, included in this framework."
    tip11 = "Social Engineer Toolkit is included here in Shadow Suite Framework!"
    tip12 = "Weeman can serve a phishing page."
    tip13 = "Use Ipify to know your external IP Address."
    tip14 = "To expose your local server to the internet, use WebExpose."
    tip15 = "I recommend not to use Deception in a very serious job."
    headers = [quote01, quote02, quote03, quote04, quote05, quote06, quote07, quote08, quote09, tip01, tip02, tip03, tip04, tip05, tip06, tip07, tip08, tip09, tip10, tip11, tip12, tip13, tip14, tip15]
    result = headers[randint(0,23)]
    return result
