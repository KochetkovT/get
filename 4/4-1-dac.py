import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

import time

leds = (8, 11, 7, 1, 0, 5, 12, 6)

GPIO.setup(leds, GPIO.OUT, initial = GPIO.LOW)

def decimal2binary(value):
    return [int(i) for i in bin(value)[2:].zfill(8)]

try:
    while True:
        value = input("Введите число из диапазона [0, 255] \n")
        if value == "q":
            exit(0)
        try:
            value = float(value)
        except ValueError:
            print("Введённое значение должно быть числом") 
            continue 
        if value != int(value):
            print("Введённое значение должно быть целым числом")
        elif not 0 <= value <= 255:
           print("Введённое значение должно принадлежать дипазону [0, 255]")
        else:
            GPIO.output(leds, decimal2binary(int(value)))
            print("{:.4f}".format(value/256 * 3.3))


finally:
    GPIO.output(leds, GPIO.LOW)    
    GPIO.cleanup() 
    