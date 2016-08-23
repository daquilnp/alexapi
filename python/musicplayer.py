import pygame 
import os
import sys

music_folder = sys.argv[1] + "/"
pygame.mixer.init()
try:
	for song in os.listdir("/home/pi/Alexa-Media/Songs/" + music_folder):
		
		pygame.mixer.music.load("/home/pi/Alexa-Media/Songs/" + music_folder + song)
	
		pygame.mixer.music.play() 
		while pygame.mixer.music.get_busy() == True:
			continue
except OSError:
	print "folder does not exist"
pygame.quit()
print "done"
exit()
