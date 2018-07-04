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

import socket
import sys
import os

def current():
    # return the current hostname
    try:
        hostname = socket.gethostname()

    except Exception as error:
        return error

    else:
        return hostname

def byname(domain):
    # map a hostname to its IP number
    try:
        ip = socket.gethostbyname(domain)
        return ip

    except Exception as error:
        return error

    else:
        return ip

def byaddr(ip):
    # map an IP number or hostname to DNS info
    try:
        host = socket.gethostbyaddr(ip)

    except Exception as error:
        return error

    else:
        return host
