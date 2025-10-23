import RPi.GPIO as GPIO
import time;

class R2R_ADC:
    def __init__(self, dynamic_range, compare_time = 0.01, verbose = False):
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.compare_time = compare_time

        self.bits_gpio = [26, 20, 19, 16, 13, 12, 25, 11]
        self.comp_gpio = 21

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bits_gpio, GPIO.OUT, initial = 0)
        GPIO.setup(self.comp_gpio, GPIO.IN)
    
    def deinit(self):
        GPIO.output(self.gpio_bits, 0)
        GPIO.cleanup()
    
    def number_to_dac(self, number):
        GPIO.output(self.bits_gpio, [int(element) for element in bin(number)[2:].zfill(8)])
        print(number, [int(element) for element in bin(number)[2:].zfill(8)])
    
    def sequential_counting_adc(self):
        for i in range(256):
            self.number_to_dac(i)
            time.sleep(self.compare_time)
            comparator_value = GPIO.input(21)
            if not comparator_value:
                return(i-1)
                break
            elif (i == 255):
                return(i)
    
    def get_sc_voltage(self):
        value = self.sequential_counting_adc;
        return(self.dynamic_range * value/256)


if __name__ == "__main__":
    try:
        adc = R2R_ADC(3.70, 0.01, True)
        while True:
            print(adc.get_sc_voltage)
    finally:
        adc.deinit()