import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
led = 26
GPIO.setup(led, GPIO.OUT)
pwm = GPIO.PWM(led, 200)
duty = 0.0
pwm.start(duty)

while True:
    duty += 0.7
    time.sleep(0.05)

    duty += 1.0
    if duty > 100.0:
        duty = 0.0