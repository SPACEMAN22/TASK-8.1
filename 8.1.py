# TASK-8.1

import RPi.GPIO as GPIO
import dht11
import time
import datetime


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

temprecorder = dht11.DHT11(pin=4)

while True:
     result = temprecorder.read()
     if result.is_valid():
        print("temperature and humidity at: " + str(datetime.datetime.now()))
        print("temperature reading: %d C" % result.temperature)
        
        
     time.sleep(2)
