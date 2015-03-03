import RPi.GPIO as GPIO
import time
from tkinter import *
class App:
	
	ledPin = 26		
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(ledPin, GPIO.OUT)	
	GPIO.output(ledPin, GPIO.LOW)
	
	def __init__(self, master):
		global ledPin 
		ledPin = 26
		frame = Frame(master)
		frame.pack()
		self.button = Button(frame, 
                        text="OFF", fg="red",
                       command=self.turnOffLed)
		self.button.pack(side=LEFT)
		self.slogan = Button(frame,
                         text="ON", fg="green",
                         command=self.turnOnLed)
		self.slogan.pack(side=LEFT)
	def turnOnLed(self):
		ledPin = 26
		GPIO.output(ledPin, GPIO.HIGH)	
		if GPIO.output(26) == True:
		        print ("pin is high")
		else:
		        print ("pin is low")
	def turnOffLed(self):
		ledPin = 26
		GPIO.output(ledPin, GPIO.LOW)  
		if GPIO.output(26) == True:
		        print ("pin is high")
		else:
		        print ("pin is low")
root = Tk()
app = App(root)
root.mainloop()


		
		
		
