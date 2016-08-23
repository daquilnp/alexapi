import os 
response_file = "/home/pi/alexa_communication/alexa_response.json"
while os.stat(response_file).st_size == 0:
	pass

with open(response_file, 'r') as fin:
    print fin.read()
