import serial
import random
import time
from pyo import * 

################################################################################
#                               pyo setup                                      #
################################################################################

s = Server()
s.setInOutDevice(9)
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

inlen = 10
numvar = 3

inputs = [[x for x in range(numvar)] for i in range(inlen)]

thres = [20, 20, 20]

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


plant1 = Plant1()
plant2 = Plant2()

################################################################################
#                                main loop                                     #
################################################################################

while True:
    with serial.Serial('/dev/ttyS0', '115200', timeout=0.5) as ser: #add timeout later
        ser.write(1)
        inp = ser.readline().decode('utf-8').replace("\0", "")
##        try:
        if True:
            if len(inp) > 1:
                inputs.append(eval(inp[:-2]))
                inputs.pop(0)
#        except:
#            print(f"error happened evaluating this --> {inp}")

    

    if is_touch(0):
        print("touch")
        a.freq = a.freq * random.choice([2.0**(1/12),1/(2.0**(1/12))])
        f.play()

    if is_touch(1):
        plant1.play()

    if is_touch(2):
        plant2.play()

