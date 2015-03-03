import time
import RPi.GPIO as GPIO
import os


GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(26, GPIO.OUT)

while True:	
	print("1")
	GPIO.output(26, True)
	print("2")
	time.sleep(2)
	print("3")
	GPIO.output(26, False)
	time.sleep(2)
