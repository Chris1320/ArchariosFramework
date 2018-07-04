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

import sys

class ASCIIGraphs():

    def __init__(self):
        pass

    def progress_bar(self, description, iteration_counter, total_items,
            progress_bar_length=20):
        """
        Print progress bar
        :param description: Description
        :type description: str

        :param iteration_counter: Incremental counter
        :type iteration_counter: int

        :param total_items: total number items
        :type total_items: int

        :param progress_bar_length: Progress bar length
        :type progress_bar_length: int

        :returns: void
        :rtype: void
        """

        percent = float(iteration_counter) / total_items
        hashes = '#' * int(round(percent * progress_bar_length))
        spaces = ' ' * (progress_bar_length - len(hashes))
        sys.stdout.write("\r{0}: [{1}] {2}%".format(description,
            hashes + spaces, int(round(percent * 100))))
        sys.stdout.flush()
        if total_items == iteration_counter:
            print("\r")
