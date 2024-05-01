import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

import time

dac = (8, 11, 7, 1, 0, 5, 12, 6)
comp = 14
troyka = 13

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

def decimal2binary(value):
    return [int(i) for i in bin(value)[2:].zfill(8)]

def adc():
    val = 0
    for i in range(7, -1, -1):
        val += 2**i
        dac_value = decimal2binary(val)
        GPIO.output(dac, dac_value)
        time.sleep(0.001)
        comp_value = GPIO.input(comp)
        if comp_value != 0:
            val -= 2**i
    return val

try:
    while True:
        val = adc()
        print("{}, {:.2f}".format(val, val*3.3/256))
        time.sleep(1)


finally:
    GPIO.output(dac, GPIO.LOW)    
    GPIO.cleanup() 