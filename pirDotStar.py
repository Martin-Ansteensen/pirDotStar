import time
import random
import board
import adafruit_dotstar as dotstar
import datetime
from datetime import timedelta
import RPi.GPIO as GPIO

dots = dotstar.DotStar(board.D6, board.D5, 10, brightness=1) #Define board and how many leds
n_dots = len(dots)
dots.fill((0,0,0)) #Turns off all leds


GPIO.setwarnings(False)
GPIO.setup(4,GPIO.IN) #Defines the GPIO pin 4 as an input

for dot in range(n_dots): #Lights all leds greenn in a "wave" movemonent
	dots[dot] = (0, 204, 0)
margin = 20 #Time before the leds turn from red to green
while True:
	colorStep = 0 #Resets variables
	r = 255
	g = 0
	b = 255 - colorStep
	if GPIO.input(4) == 1: #If PIR is triggered
		lastTriggered = datetime.datetime.now() #The last time the PIR was triggered
		print("You moved")
		for dot in range(n_dots): #Lights all leds pink in a wave "movement"
			dots[dot] = (255,0 , 255)
		
		while GPIO.input(4) == 1 or lastTriggered > datetime.datetime.now() - timedelta(seconds = margin): #If either the sensor is detecting something or it has passed less than "margin" seconds since last detect
			print("Inne i while")
			if colorStep < 255: #Turns the led gradually twoards red
				colorStep += 1 
				r = 255
				g = 0
				b = 255 - colorStep
				dots.fill((r,g,b))
				time.sleep(0.5) #Delay 
		time.sleep(0.5)	#Delay
	
	else:		 
		for dot in range(n_dots): #Turns the leds green in a "wave"  movement
			dots[dot] = (0, 204, 0)
	print("Kommet seg gjennom loop") 


