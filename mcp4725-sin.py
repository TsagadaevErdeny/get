import mcp4725_driver
import signal_generator as sg
import time

amplitude = 5.2
signal_frequency = 10
sampling_frequency = 1000 #1000

try:
    #time.clock
    start_time = time.time()
        
    dac = mcp4725_driver.MCP4725(amplitude, 0x61, True)
    while True:
        end_time = time.time()
        elapsed_time = end_time - start_time
        #print(elapsed_time)
        voltage = amplitude*sg.get_sin_wave_amplitude(signal_frequency, elapsed_time)
        dac.set_voltage(voltage)
        sg.wait_for_sampling_period(sampling_frequency)

finally:
    dac.deinit()
