import RPi.GPIO as GPIO
import time

#BCM Pin numbers 
Rpin = 12
Gpin = 13
Bpin = 19
 
GPIO.setmode(GPIO.BCM)

#Setup pins as output
GPIO.setup(Rpin,GPIO.OUT)
GPIO.setup(Bpin,GPIO.OUT)
GPIO.setup(Gpin,GPIO.OUT)

#Set PWM values to pins
red = GPIO.PWM(Rpin, 50)
green = GPIO.PWM(Gpin, 50)
blue = GPIO.PWM(Bpin, 50)
 
red.start(3)
time.sleep(1)
red.stop()
green.start(3)
time.sleep(1)
green.stop()
blue.start(3)
time.sleep(1)
blue.stop()

GPIO.cleanup()
