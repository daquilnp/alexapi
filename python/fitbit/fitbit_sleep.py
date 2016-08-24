import fitbit
import json
import datetime

authd_client = fitbit.Fitbit('client_id', 'client_secret',
                             access_token='access_token',
                              refresh_token='refresh_token')

jdata  = json.loads(json.dumps(authd_client.get_sleep(datetime.date.today()), ensure_ascii=False))

sleep_data_total_asleep = int(json.dumps(jdata["summary"]["totalMinutesAsleep"], ensure_ascii=False))
sleep_data_time_in_bed = int(json.dumps(jdata["summary"]["totalTimeInBed"], ensure_ascii=False))

hours_slept = sleep_data_total_asleep/60
hours_in_bed = sleep_data_time_in_bed/60
time_asleep = str(hours_slept) + " hours and " + str(int((sleep_data_total_asleep/60.0 - hours_slept)*60.0)) + " minutes" 
time_in_bed = str(hours_in_bed) + " hours and " + str(int((sleep_data_time_in_bed/60.0 - hours_in_bed)*60.0)) + " minutes" 
time_awake = sleep_data_time_in_bed - sleep_data_total_asleep
total_efficiency = float("{0:.3f}".format(sleep_data_total_asleep*1.0/sleep_data_time_in_bed))

response_string = "You were in bed for " + time_in_bed + ". You slept a total of " + time_asleep + " and spent " + str(time_awake) + " minutes awake. Total efficiency of sleep was " + str(total_efficiency*100) + " percent" 
# hours_asleep = int(sleep_data_total_asleep/60)
print response_string