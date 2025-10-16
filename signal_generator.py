import numpy as np
import time

def get_sin_wave_amplitude(freq, time):
    sin_value = np.sin(2*(np.pi)*freq*time)
    return((sin_value+1)/2)

def wait_for_sampling_period(sampling_frequency):
    time_period = 1/sampling_frequency
    time.sleep(time_period)

def get_triangular_amplitude(freq, time):
    time = time - int(time)
    triang_value = np.abs(1-(time*freq%1)*2)
    return(triang_value)