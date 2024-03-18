import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

from time import sleep

leds = (8, 11, 7, 1, 0, 5, 12, 6)

GPIO.setup(leds, GPIO.OUT, initial = GPIO.LOW)

def decimal2binary(value):
    return [int(i) for i in bin(value)[2:].zfill(8)]

try:
    while True:
        T = input("Введите значение периода \n")
        try:
            T = float(T)
            t = T/256/2
            break
        except ValueError:
            print("Введённое значение должно быть числом") 
        
    while True:
        for i in range(256):
            GPIO.output(leds, decimal2binary(int(i)))
            sleep(t)
        for i in range(255, -1, -1):
            GPIO.output(leds, decimal2binary(int(i)))
            sleep(t)


finally:
    GPIO.output(leds, GPIO.LOW)    
    GPIO.cleanup() 