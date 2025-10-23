import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
leds = [16, 12, 25, 17, 27, 23, 22, 24]
GPIO.setup(leds, GPIO.OUT)
GPIO.output(leds, 0)
up = 9
GPIO.setup(up, GPIO.IN)
down = 10
GPIO.setup(down, GPIO.IN)
num = 0


def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]


sleep_time = 0.2
while True:
    if GPIO.input(up):
        num += 1
        if num >= 256:
            num = 0
            print("You've exceeded the maximum so now num is 0")
        print(num, dec2bin(num))
        GPIO.output(leds, dec2bin(num))
        time.sleep(sleep_time)
    if GPIO.input(down):
        num -= 1
        if num < 0:
            num = 0
            print("You've reached negative numbers so num is still 0")
        GPIO.output(leds, dec2bin(num))
        print(num, dec2bin(num))
        time.sleep(sleep_time)
