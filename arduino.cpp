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

    def play(self):
        if time.perf_counter() - self.last_trig > self.duration:
            self.synth.freq = self.synth.freq * random.choice(self.semi_intervals)
            self.adsr.play()
            self.last_trig = time.perf_counter()

    


plant1 = Plant1()
plant2 = Plant2()

################################################################################
#                                main loop                                     #
################################################################################
zcount = [time.perf_counter() for i in range(6)]

ser = serial.Serial('/dev/ttyS0', '115200', timeout=0.5)
ser1 = serial.Serial('/dev/ttyACM0', '115200', timeout=0.5)
try:
    while True:
        inp = 0
        try:
            ppreinp = ser.readline().decode('utf-8')
            preinp = ppreinp.replace("\0", "").replace("\n", "").replace("\r", "")
            if len(preinp) > 0:
                inp = int(preinp)
                
            ser.reset_input_buffer()
        except Exception:
            print(traceback.format_exc())
            time.sleep(0.05)
        if not inp == 0:
            if inp == 1 and zcount[0] - time.perf_counter() < -0.3:
                a.freq = a.freq * random.choice([2.0**(1/12),1/(2.0**(1/12))])
                f.play()
                zcount[0] = 0


            elif inp == 2 and zcount[1] - time.perf_counter() < -0.3:
                plant1.play()
                zcount[1] = 0

            elif inp == 3 and zcount[2] - time.perf_counter() < -0.3:
                plant2.play()
                zcount[2] = 0

        inp1 = 0
        try:
            ppreinp = ser1.readline().decode("utf-8")
            preinp = ppreinp.replace("\0", "").replace("\n", "").replace("\r", "")

            if len(preinp) > 0:
                inp1 = int(preinp)
            ser1.reset_input_buffer()
        except Exception:
            print(traceback.format_exc())
            time.sleep(0.05)
        if not inp1 == 0:
            if inp1 == 4 and zcount[3] - time.perf_counter() < -0.3:
                a.freq = a.freq * random.choice([2.0**(1/12),1/(2.0**(1/12))])
                f.play()
                zcount[3] = 0


            elif inp1 == 5 and zcount[4] - time.perf_counter() < -0.3:
                plant1.play()
                zcount[4] = 0

            elif inp1 == 6 and zcount[5] - time.perf_counter() < -0.3:
                plant2.play()
                zcount[5] = 0

finally:
    ser.close()
    ser1.close()
