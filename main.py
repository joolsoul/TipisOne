import matplotlib.pyplot as plt
import numpy as np


def harmonic_signal(a, frequency, shift, t):
    return [a * np.sin(2 * np.pi * frequency * t1 + shift) for t1 in t]


def digital_signal(a, frequency, shift, t):
    return [max(0, a * np.sign(np.sin(2 * np.pi * frequency * t1 + shift))) for t1 in t]


def get_spectre(signal):
    return np.fft.rfft(signal)


if __name__ == '__main__':
    fig, axes = plt.subplots(nrows=4, ncols=4)

    fig.set_figheight(5)
    fig.set_figwidth(10)
    fig.subplots_adjust(wspace=0.5, hspace=0.5)

    axes[0, 0].set_title("harmonic")
    axes[0, 1].set_title("harmonic spectre")
    axes[0, 2].set_title("digital")
    axes[0, 3].set_title("digital spectre")

    row = 0

    amplitude = 1
    shift = 0
    frequencies = [1, 2, 4, 8]
    t = np.linspace(0.0, 1.0, 1000)
    freq_x = np.fft.rfftfreq(len(t), d=1 / 1000)

    for frequency in frequencies:

        harmonic = harmonic_signal(amplitude, frequency, shift, t)
        digital = digital_signal(amplitude, frequency, shift, t)
        harmonic_spectre = get_spectre(harmonic)
        digital_spectre = get_spectre(digital)

        axes[row, 0].set_ylabel(str(frequency) + " Hz")

        axes[row, 0].set_ylim(-2, 2)
        axes[row, 0].plot(t, harmonic, 'b')
        axes[row, 0].grid(True)

        axes[row, 1].set_xlim([-1 * frequency, 10 * frequency])
        axes[row, 1].plot(freq_x, np.abs(harmonic_spectre), 'r')
        axes[row, 1].grid(True)

        axes[row, 2].set_ylim(-2, 2)
        axes[row, 2].plot(t, digital, 'b')
        axes[row, 2].grid(True)

        axes[row, 3].set_xlim([-1 * frequency, 10 * frequency])
        axes[row, 3].plot(freq_x, np.abs(digital_spectre), 'r')
        axes[row, 3].grid(True)

        row = row + 1

    plt.show()
