import r2r_dac as r2r
import signal_generator as sg
import time
import RPi.GPIO as GPIO

from signal_generator import get_sin_wave_amplitude
from signal_generator import wait_for_sampling_period

amplitude = 3.1
signal_frequency = 10
sampling_frequency = 10 #1000

try:
    #time.clock
    start_time = time.time()
    class R2R_DAC:
        def __init__(self, gpio_bits, dynamic_range, verbose = False):
            self.gpio_bits = gpio_bits
            self.dynamic_range = dynamic_range
            self.verbose = verbose
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(self.gpio_bits, GPIO.OUT, initial = 0)
        
        def deinit(self):
            GPIO.output(self.gpio_bits, 0)
            GPIO.cleanup()

        def set_number(self, num):
            print(num, [int(element) for element in bin(num)[2:].zfill(8)])
            GPIO.output(self.gpio_bits, [int(element) for element in bin(num)[2:].zfill(8)])
        
        def set_voltage(self, voltage):
            if not (0.0 <= voltage <= self.dynamic_range):
                print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {self.dynamic_range:.2f} B)")
                print("Устанавливаем 0.0 В")
                return 0
            self.set_number(int(voltage / self.dynamic_range * 255)) #Почему 255, а не 256?
        
    dac = R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.15, True)
    while True:
        end_time = time.time()
        elapsed_time = end_time - start_time
        #print(elapsed_time)
        voltage = amplitude*get_sin_wave_amplitude(signal_frequency, elapsed_time)
        dac.set_voltage(voltage)
        wait_for_sampling_period(sampling_frequency)

finally:
    dac.deinit()
