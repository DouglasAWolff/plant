import serial
import random
import time
from pyo import * 
import traceback

################################################################################
#                               pyo setup                                      #
################################################################################

s = Server()
s.setInOutDevice(pa_get_output_devices()[0].index('default'))
s.boot()
f = Adsr(attack=0.1, decay=1, sustain=0, release=0, dur=1.5, mul=.5)
a = Sine(freq=340, mul=f).out()
s.start()

f.play()
time.sleep(0.5)
f.play()
time.sleep(0.5)
################################################################################
#                            variables setup                                   #
################################################################################



################################################################################
#                        classes/functions setup                               #
################################################################################

class Plant():
    def __init__(self):
        self.thresh = 40
       

class Plant1(Plant):
    def __init__(self):
        self.duration = 0.3
        self.semi_intervals = [2.0**(1/12),1/(2.0**(1/12))]
        self.adsr = Adsr(attack=0.1, decay=0.3, sustain=1, release=.9, dur=0.9, mul=.5)
        self.synth = SuperSaw(freq=340, mul=self.adsr).out()
        self.last_trig = time.perf_counter()

    def play(self):
        if time.perf_counter() - self.last_trig > self.duration:
            self.synth.freq = self.synth.freq * random.choice(self.semi_intervals)
            self.adsr.play()
            self.last_trig = time.perf_counter()

def is_touch(sens):
    if inputs[-1][sens] > thres[sens]:
        return True
    else:
        return False



class Plant2(Plant):
    def __init__(self):
        self.duration = 1
        self.semi_intervals = [2.0**(1/12),1/(2.0**(1/12))]
        self.adsr = Adsr(attack=0.1, decay=0.3, sustain=1, release=.9, dur=self.duration, mul=0.7)
        self.mod = Sine(freq=6, mul=50)
        self.synth = Sine(freq= self.mod + 320, mul=self.adsr).out()
        self.last_trig = time.perf_counter()

