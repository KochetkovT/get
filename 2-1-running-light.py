import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

import time

leds = (2, 3, 4, 17, 27, 22, 10, 9)

GPIO.setup(leds, GPIO.OUT, initial = GPIO.LOW)

time.sleep(1)

for i in range(3):
    for led in leds:
        GPIO.output(led, GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(led, GPIO.LOW)

GPIO.output(leds, GPIO.LOW)    
GPIO.cleanup()    