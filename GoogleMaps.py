import urllib
import urllib2
import time
import json
import pickle
import os
import sys
import math

from GoogleMapsApiKey import api_key


queries_per_day = 2400

def drange(start, stop, step):
	r = start
	while r < stop:
		yield r
		r += step

def get_url_response(url):
	print >> sys.stderr, url
	response = urllib2.urlopen(url)
	return response

def get_url_contents(base_url, values = None):
	data = urllib.urlencode(values)
	complete_url = base_url + "?" + data

	response = get_url_response(complete_url)
	contents = response.read()
	return contents

def get_google_maps_response(api_name, output_format, values, sleep = True):
	#Google Maps limits me to 2500 requests per 24 hours, so max one query per this amount of seconds
	if sleep:
		sleeptime = math.ceil((60*60*24)/queries_per_day)
		time.sleep(sleeptime) 

	url = 'https://maps.googleapis.com/maps/api/%s/%s' % (api_name, output_format)
	response = get_url_contents(url, values)
	return response

def get_google_maps_directions(mode, departure_time, origin, destination, via = "", sleep = True):
	values = { "origin" : origin, "destination" : destination, "mode" : mode, "departure_time" : departure_time, "key" : api_key}
	if via != "":
		values["waypoints"] = "via:%s" % via
	json_output = get_google_maps_response("directions", "json", values, sleep)
	print >> sys.stderr, json_output
	output = json.loads(json_output)
	return output

def get_google_maps_directions_time(mode, departure, origin, destination, via = "", sleep = True):
	directions = get_google_maps_directions(mode, departure, origin, destination, via, sleep)
	status = directions["status"]
	if status == "ZERO_RESULTS":
		return float(1e100)

	routes = directions["routes"]
	legs = routes[0]["legs"]
	duration = legs[0]["duration"]
	value = duration["value"]
	value_in_traffic = 0
	distance = legs[0]["distance"]
	distance_meters = distance["value"]
	try:
		duration_in_traffic = legs[0]["duration_in_traffic"]
		value_in_traffic = duration_in_traffic["value"]
	except:
		pass

	print >> sys.stderr, str(value) + " " + str(value_in_traffic) + " " + str(distance_meters)
	return [float(value), float(value_in_traffic), float(distance_meters)]


