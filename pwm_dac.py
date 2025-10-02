import RPi.GPIO as GPIO
import time

class R2R_DAC:
    def __init__(self, gpio_pin, pwm_frequancy, dynamic_range, verbose = False):
        self.gpio_pin = gpio_pin
        self.pwm_frequancy = pwm_frequancy
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_pin, GPIO.OUT) #, initial = 0)
    
    def deinit(self):
        GPIO.output(self.gpio_pin, 0)
        GPIO.cleanup()
    
    def set_voltage(self, voltage):
        if not (0.0 <= voltage <= self.dynamic_range):
            print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {self.dynamic_range:.2f} B)")
            print("Устанавливаем 0.0 В\n")
            return 0
        
        pwm = GPIO.PWM(self.gpio_pin, self.pwm_frequancy)
        duty = 0.0
        pwm.start(duty)
        duty = int(voltage / self.dynamic_range * 10000)/100
        print("Коэффициент заполнения: ", duty)
        print("")
        for i in range(5*self.pwm_frequancy):
            pwm.ChangeDutyCycle(duty)
            time.sleep(1/self.pwm_frequancy)

if __name__ == "__main__":
    try:
        dac = R2R_DAC(22, 500, 3.290, True) #Почему 3.290, а не 3.3?
        
        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах: "))
                dac.set_voltage(voltage)
            except ValueError:
                print("Вы ввели не число. Попробуйте еще раз\n")
    finally:
        dac.deinit()
