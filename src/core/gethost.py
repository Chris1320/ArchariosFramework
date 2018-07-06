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

objects = ['current', 'byname', 'byaddr']

import socket


def current():
    """
    def current():
        return the current hostname
    """

    try:
        hostname = socket.gethostname()

    except Exception as error:
        return error

    else:
        return hostname


def byname(domain):
    """
    def byname():
        map a hostname to its IP number

        :param domain: Domain to map.
        :type str:

        :returns: ip or error exception
        :return type: str <specific>Exception
    """

    try:
        ip = socket.gethostbyname(domain)
        return ip

    except Exception as error:
        return error

    else:
        return ip


def byaddr(ip):
    """
    def byaddr():
        map an IP number or hostname to DNS info

        :param ip: IP to map.
        :type str:

        :returns: ip or Exception
        :return type: str or <specific>Exception
    """

    try:
        host = socket.gethostbyaddr(ip)

    except Exception as error:
        return error

    else:
        return host
