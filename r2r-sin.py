import r2r_dac as r2r
import signal_generator as sg
import time

amplitude = 3.15
signal_frequency = 10
sampling_frequency = 200 #1000

try:
    #time.clock
    start_time = time.time()
        
    dac = r2r.R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.15, True)
    while True:
        end_time = time.time()
        elapsed_time = end_time - start_time
        #print(elapsed_time)
        voltage = amplitude*sg.get_sin_wave_amplitude(signal_frequency, elapsed_time)
        dac.set_voltage(voltage)
        sg.wait_for_sampling_period(sampling_frequency)

finally:
    dac.deinit()
