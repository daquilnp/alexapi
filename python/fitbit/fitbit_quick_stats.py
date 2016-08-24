import fitbit
import json
import datetime

authd_client = fitbit.Fitbit('client_id', 'client_secret',
                             access_token='access_token',
                              refresh_token='refresh_token')

jdata  = authd_client.activities(date=None, user_id=None, data=None)

total_distance = 0
total_steps = 0
total_calories = 0

for distance in jdata["summary"]["distances"]:
	if distance["activity"] == "total":
		total_distance = distance["distance"]
		break

total_steps = jdata["summary"]["steps"]
total_calories = jdata["summary"]["caloriesOut"]

response_string = "Today you have travelled " + str(total_distance) + " miles, taking " + str(total_steps) + " steps. Along the way you have burnt " + str(total_calories) + " calories." 

print response_string
