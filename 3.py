import thinkdsp
import thinkplot
import numpy as np
import pandas as pd

## 3-a
f= open('taiwanStock.csv')
s= f.read()
sL= s.split('\n')
xL= [x.split(',')[-1] for x in sL]
yL= [float(x) for x in xL[1:-1]]
pData= np.array(yL)
print(len(pData))

## 3-b
print(pData[len(pData)-10:len(pData)])

## 3-c
import pylab as pl
def movingaverage(x,length):
    y = np.convolve(x, np.ones(length)/length)
    y = y[:len(x)]
    return y

ma100 = movingaverage(pData,100)
ma500 = movingaverage(pData,500)
ma1000= movingaverage(pData,1000)
pl.plot(pData)
pl.plot(ma100)
pl.plot(ma500)
pl.plot(ma1000)

## 3-d
duration = len(pData)
framerate = 20
linewidth = 1
### wNoise
signal1 = thinkdsp.UncorrelatedUniformNoise()
wNoise = signal1.make_wave(duration=duration,framerate=framerate)
wNoise.plot()
### pNoise
signal2 = thinkdsp.PinkNoise()
pNoise = signal2.make_wave(duration=duration,framerate=framerate)
pNoise.plot()
### rNoise
signal3 = thinkdsp.BrownianNoise()
rNoise = signal3.make_wave(duration=duration,framerate=framerate)
rNoise.plot()  

## 3-e
def make_spectrum(signal):
        wave = signal.make_wave(duration=duration, framerate=framerate)
        spectrum = wave.make_spectrum()
        spectrum.hs[0] = 0
        return spectrum
### wSpec
signal1 = thinkdsp.UncorrelatedUniformNoise()
wSpec = make_spectrum(signal1)
wSpec.plot_power(label='wSpec',color='#000000',linewidth=linewidth)
### pSpec
signal2 = thinkdsp.PinkNoise()
pSpec = make_spectrum(signal2)
pSpec.plot_power(label='pSpec', color='#FFC0CB', linewidth=linewidth)
### rSpec
signal3 = thinkdsp.BrownianNoise()
rSpec = make_spectrum(signal3)
rSpec.plot_power(label='rSpec', color='#FF0000', linewidth=linewidth)

thinkplot.config(xlabel='frequency (Hz)',
                 ylabel='power',
                 xscale='log',
                 yscale='log')
