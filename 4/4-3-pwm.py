import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

pwm_pin = 24

GPIO.setup(pwm_pin, GPIO.OUT)
pwm = GPIO.PWM(pwm_pin, 1000)
pwm.start(0)

try:
    while True:
        d = input("Введите значение duty cycle из дипазона [0, 100]\n")
        try:
            d = float(d)
        except ValueError:
            print("Введённое значение должно быть числом") 
            continue
        if not 0 <= d <= 100:
            print("Введённое значение должно быть из дипазона [0, 100")
        else:
            pwm.ChangeDutyCycle(d)
            print("{:.4f}".format(d * 3.3 / 100))
    



finally:  
    GPIO.cleanup() 