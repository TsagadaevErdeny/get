import numpy as np
import time

def get_sin_wave_amplitude(freq, time):
    sin_value = np.sin(2*(np.pi)*freq*time)
    return((sin_value+1)/2)

def wait_for_sampling_period(sampling_frequency):
    time_period = 1/sampling_frequency
    time.sleep(time_period)
