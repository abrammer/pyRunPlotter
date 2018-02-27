import stravalib
from stravalib.client import Client
from configparser import SafeConfigParser
import json
import os

config = SafeConfigParser()
config.read('config.yaml')

client = Client()
client.access_token = config.get('strava', 'Bearer')


def update_strava_archive():
	''' update local archive 
		-- strava has api limits so better to grab once and store
	'''
	try:
		with open('outputfile','r') as fin:
			running_data = json.load(fin)
	except FileNotFoundError:
		running_data = {}


	activities = client.get_activities(after = "2012-01-01T00:00:00Z")
	activity_data = []
	for activity in activities:
		if(f'{activity.id}' not in running_data): # saved as string
			print(f'{activity.id} ---')
			activity_stream = client.get_activity_streams(activity.id, types=['latlng','distance'])
			running_data[activity.id] = activity_stream['latlng'].data

	with open('outputfile','w') as fout:
		json.dump(running_data, fout, indent=0)


if __name__ == "__name__":
	update_strava_archive()
