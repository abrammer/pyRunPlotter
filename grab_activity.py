''' Script to grab activities from strava '''    

import sys
#sys.path.append('/Users/abrammer/local/strava_python')
import stravalib
from stravalib.client import Client
from configparser import SafeConfigParser

config = SafeConfigParser()
config.read('/Users/abrammer/local/strava_python/config.yaml')

client = Client()
authorize_url = client.authorization_url(client_id=config.get('strava','client_id'), redirect_uri='http://localhost:8282/authorized')
# Extract the code from your webapp response
# access_token = client.exchange_code_for_token(client_id=config.get('strava', 'client_id'), client_secret=config.get('strava', 'client_secret'), code=config.get('strava', 'code'))

# Now store that access token somewhere (a database?)
client.access_token = config.get('strava', 'Bearer')
athlete = client.get_athlete()


activities = client.get_activities(after = "2017-11-17T00:00:00Z",  limit=15)
activity_data = []
for activity in activities:
	activity_stream = client.get_activity_streams(activity.id, types=['latlng','distance'])
	activity_data.append(activity_stream['latlng'].data)

