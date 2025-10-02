import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
leds = [16, 20, 21, 25, 26, 17, 27, 22]
GPIO.setup(leds, GPIO.OUT)
GPIO.output(leds, 0)

dynamic_range = 3.15

def voltage_to_number(voltage):
    if not (0.0 <= voltage <= dynamic_range):
        print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {dynamic_range:.2f} B)")
        print("Устанавливаем 0.0 В")
        return 0
    return int(voltage / dynamic_range * 255) #Почему 255, а не 256?

def number_to_dac(num):
    print(num, [int(element) for element in bin(num)[2:].zfill(8)])
    GPIO.output(leds, [int(element) for element in bin(num)[2:].zfill(8)])

try:
    while True:
        try:
            voltage = float(input("Введите напряжение в Вольтах: "))
            number = voltage_to_number(voltage)
            number_to_dac(number)

        except ValueError:
            print("Вы ввели не число. Попробуйте еще раз\n")

finally:
    GPIO.output(leds, 0)
    GPIO.cleanup()