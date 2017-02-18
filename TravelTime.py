import GoogleMaps
import datetime
import time
import sys
import random

if len(sys.argv) < 6:
	sys.stderr.write("Usage: " + sys.argv[0] + " start_hour end_hour interval_minutes origin destination [via]\n")
	sys.exit(-1)
start_hour 		= int(sys.argv[1])
end_hour 		= int(sys.argv[2])
interval_minutes 	= int(sys.argv[3])
origin 			= sys.argv[4]
destination 		= sys.argv[5]
via 			= None
max_duration_days 	= 7
if len(sys.argv) > 6:
	via = sys.argv[6]
if len(sys.argv) > 7:
	max_duration_days = float(sys.argv[7])

mode = "car"
min_month = 3
max_month = 13
min_day = 1
max_day = 32
min_minute = 0
max_minute = 60

seconds_in_a_day = 60*60*24

queries_per_day = (end_hour - start_hour) * (60.0/interval_minutes)
queries_per_month = queries_per_day * (max_day - min_day)
queries_per_year = queries_per_month * (max_month - min_month)

estimated_time = float(queries_per_year) / float(GoogleMaps.queries_per_day)

if max_duration_days == None or max_duration_days >= estimated_time:
	max_duration_days = estimated_time

query_chance = max_duration_days / estimated_time

print >> sys.stderr,  "%d queries per day, %d per month, %d total. Estimated time %f days. Have %f days, so only performing %f part of all queries: %f." % (queries_per_day, queries_per_month, queries_per_year, estimated_time, max_duration_days, query_chance, (queries_per_year * query_chance))

time.sleep(10)

for month in range(min_month, max_month):
	for day in range(min_day,max_day):
		for hour in range(start_hour,end_hour):
			for minute in range(0, 60, interval_minutes):
				query_random = random.random()
				perform_query = (query_random >= query_chance)
				try:
					current_datetime = datetime.datetime(2017, month, day, hour, minute)
				except:
					continue
				if current_datetime.weekday() < 5 and perform_query: #weekdays, monday = 0..sunday = 6
					current_time = int(time.mktime(current_datetime.timetuple()))
					try:				
						[travel_time, travel_time_in_traffic, travel_distance] = GoogleMaps.get_google_maps_directions_time(mode, current_time, origin, destination, via)
						print ",".join([str(current_time),str(current_datetime.year), str(current_datetime.month), str(current_datetime.day), str(current_datetime.hour), str(current_datetime.minute), str(travel_time), str(travel_time_in_traffic), str(travel_distance),str(current_datetime.weekday())])
						sys.stdout.flush()
					except:
						pass
