
def sine_wave_demo():

    import numpy as np
    import matplotlib.pyplot as plt
    from signalgen import sine_wave # our function

    f = 10
    over_samp_rate = 30
    phase = 1/3*np.pi
    n_cycl = 5

    time, sig = sine_wave(f, over_samp_rate, phase, n_cycl)

    # viewing our signal
    plt.plot(time, sig)
    plt.title('Sine wave f='+str(f)+' Hz') 
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.show()




def main():
    sine_wave_demo()
    


if __name__ == "__main__":
    main()
