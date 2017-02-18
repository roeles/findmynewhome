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
