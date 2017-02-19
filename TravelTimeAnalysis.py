#!/usr/bin/env python
#
# Copyright (C) 2016-2017 Roel Baardman
#
# This file is part of findmynewhome.
# Findmynewhome is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Findmynewhome is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with findmynewhome.  If not, see <http://www.gnu.org/licenses/>.


import sys
import numpy
import collections

times = collections.OrderedDict()
distances = collections.OrderedDict()
for line in sys.stdin:
	elements = line.split(",")
	timestamp 	= int(elements[0])
	year 		= int(elements[1])
	month		= elements[2]
	day		= elements[3]
	hour		= int(elements[4])
	minute		= int(elements[5])
	traveltime	= elements[6]
	traffictime	= float(elements[7])
	distance	= float(elements[8])
	dayofweek	= int(elements[9])

	timestring	= "%02d,%02d" % (hour, minute)

	if not timestring in times:
		times[timestring] = []
	if not timestring in distances:
		distances[timestring] = []


	times[timestring].append(traffictime)
	distances[timestring].append(distance)

for key,value in times.iteritems():
	mean = numpy.mean(value)
	stdev = numpy.std(value)

	dist_mean = numpy.mean(distances[key])
	dist_stdev = numpy.std(distances[key])
	print key + "," + str(mean) + "," + str(stdev) + "," + str(dist_mean) + "," + str(dist_stdev)
print "end"
