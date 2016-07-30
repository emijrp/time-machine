#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (C) 2016 emijrp <emijrp@gmail.com>
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
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import datetime

def travelToDate(date):
    print("Time travelling to %s" % (date))
    #start time machine code
    
    #end time machie code

def main():
    date = raw_input("When do you want to go? (Format: YYYY-MM-DD hh:mm:ss): ")
    date = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
    travelToDate(date)
    print("Your are in %s now" % (date))

if __name__ == '__main__':
    main()
