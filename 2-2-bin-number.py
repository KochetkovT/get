import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

import time

from random import randint

def decimalToBinary(n): 
    ans_str = bin(n).replace("0b", "")
    ans_str = ans_str[::-1]
    ans_lst = [0]*8
    for i in range(len(ans_str)):
        ans_lst[i] = int(ans_str[i])
    return ans_lst

number = decimalToBinary(255)

# for i in range(8):
#     number.append(randint(0, 1))

dac = (6, 12, 5, 0, 1, 7, 11, 8)

GPIO.setup(dac, GPIO.OUT, initial = GPIO.LOW)

time.sleep(1)

GPIO.output(dac, number)

time.sleep(15)

GPIO.output(dac, GPIO.LOW)    
GPIO.cleanup() 