
import thinkdsp

# 1-a
##  1-a-1

sin_sig = thinkdsp.SinSignal(freq=100,amp=1)
wave_sig = sin_sig.make_wave()
wave_sig.segment(start=0.1, duration=0.02).plot()


## 1-a-2
squ_sig = thinkdsp.SquareSignal(freq=100,amp=1)
wave_squ = squ_sig.make_wave()
wave_squ.segment(start=0.1, duration=0.02).plot()

## 1-a-3
tri_sig = thinkdsp.TriangleSignal(freq=100,amp=1)
wave_tri = tri_sig.make_wave()
wave_tri.segment(start=0.1, duration=0.02).plot()

## 1-a-4
saw_sig = thinkdsp.SawtoothSignal(freq=100,amp=1)
wave_saw = saw_sig.make_wave()
wave_saw.segment(start=0.1, duration=0.02).plot()

# 1-b

spec1 = wave_sig.make_spectrum()
spec1.plot()

spec2 = wave_squ.make_spectrum()
spec2.plot()

spec3 = wave_tri.make_spectrum()
spec3.plot()

spec4 = wave_saw.make_spectrum()
spec4.plot()
