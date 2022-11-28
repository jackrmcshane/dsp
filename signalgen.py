
import numpy as np


def sine_wave(f, over_samp_rate, phase, n_cycl):
    """A function for generating a sine wave signal

    :f: frequency of the wave
    :over_samp_rate: TODO
    :phase: TODO
    :n_cycl: TODO
    :returns: TODO

    """
    fs = over_samp_rate * f # sampling frequency
    # arange(start, stop, step)
    t = np.arange(0, n_cycl/f - 1/fs, 1/fs) # what?
    g = np.sin(2*np.pi*f*t+phase)
    return t, g



def square_wave(f, samp_rate, n_cyc):
    fs = samp_rate*f # sampling frequency
    t = np.arange(0, n_cycl*1/f - 1/fs, 1/fs)
    sig = np.sign(np.sin(2*np.pi*f*t))

    return t, sig


def scipy_square_wave():

    import numpy as np
    import matplotlib as plt
    from scipy import signal

    f = 10 # Hz
    samp_rate = 30
    n_cycl = 5

    fs = samp_rate*f
    t = np.arange(0, n_cycl*1/f, 1/fs)
    sig = signal.square(2*np.pi*f*t, duty=.2)
    
    plt.plot(t,sig)
    plt.show()
