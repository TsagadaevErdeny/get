import pwm_dac
import signal_generator as sg
import time

amplitude = 3.15
signal_frequency = 10
sampling_frequency = 1000 #1000


try:
    #time.clock
    start_time = time.time()
        
    dac = pwm_dac.R2R_DAC(22, sampling_frequency, amplitude, True)
    while True:
        end_time = time.time()
        elapsed_time = end_time - start_time
        #print(elapsed_time)
        voltage = amplitude*sg.get_triangular_amplitude(signal_frequency, elapsed_time)
        dac.set_voltage(voltage)
        sg.wait_for_sampling_period(sampling_frequency)

finally:
    dac.deinit()
