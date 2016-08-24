import fitbit
import json
import datetime
import time    

authd_client = fitbit.Fitbit('client_id', 'client_secret',
                             access_token='access_token',
                              refresh_token='refresh_token')

jdata  = authd_client.activities(date=None, user_id=None, data=None)

total_distance = 0
total_steps = 0


for distance in jdata["summary"]["distances"]:
	if distance["activity"] == "total":
		total_distance = distance["distance"]
		break

total_steps = jdata["summary"]["steps"]
data = {}
data['distance'] = str(total_distance)
data['steps'] = str(total_steps)
data['date'] = time.strftime('%Y-%m-%d')
json_data = json.dumps(data)



print json_data
