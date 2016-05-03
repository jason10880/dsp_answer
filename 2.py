import thinkdsp
import thinkplot

## 2-a
signal = thinkdsp.Chirp(start=100, end=1000)
wave = signal.make_wave(duration=10)

## 2-b
spectrum = wave.make_spectrum()
spectrum.plot()
thinkplot.config(xlabel='frequency (Hz)', ylabel='amplitude')

## 2-c
def plot_spectrogram(wave, seg_length):
    spectrogram = wave.make_spectrogram(seg_length)
    print('Time resolution (s)', spectrogram.time_res)
    print('Frequency resolution (Hz)', spectrogram.freq_res)
    spectrogram.plot(high=1200)
    thinkplot.config(xlabel='Time(s)', ylabel='Frequency (Hz)')

plot_spectrogram(wave,1024)