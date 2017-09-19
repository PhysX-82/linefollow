from rc8 import raspRobot, readConfig
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

config = readConfig('config.yaml')
r = raspRobot( config )
GPIO.setup(26,GPIO.IN)

r.setDirection(0)
r.setSpeed(12)


while True:
	if (GPIO.input(26)):
		print("On-Line"),
		r.setDirection(12)
	else:
		print("Off-Line"),
		r.setDirection(-12)
