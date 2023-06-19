"""
This file contains the plant class and its subclasses.
"""
from pyo import *


class Plant:
    def __init__(self):
        self.thresh = 40

    def is_touch(self, sens):
        if inputs[-1][sens] > thres[sens]:
            return True
        else:
            return False


class Plant1(Plant):
    def __init__(self):
        super().__init__()
        self.duration = 0.3
        self.semi_intervals = [2.0 ** (1 / 12), 1 / (2.0 ** (1 / 12))]
        self.adsr = Adsr(attack=0.1, decay=0.3, sustain=1, release=.9, dur=0.9, mul=.5)
        self.synth = SuperSaw(freq=340, mul=self.adsr).out()
        self.last_trig = time.perf_counter()

    def play(self):
        if time.perf_counter() - self.last_trig > self.duration:
            self.synth.freq = self.synth.freq * random.choice(self.semi_intervals)
            self.adsr.play()
            self.last_trig = time.perf_counter()


class Plant2(Plant):
    def __init__(self):
        super().__init__()
        self.duration = 1
        self.semi_intervals = [2.0 ** (1 / 12), 1 / (2.0 ** (1 / 12))]
        self.adsr = Adsr(attack=0.1, decay=0.3, sustain=1, release=.9, dur=self.duration, mul=0.7)
        self.mod = Sine(freq=6, mul=50)
        self.synth = Sine(freq=self.mod + 320, mul=self.adsr).out()
        self.last_trig = time.perf_counter()

    def play(self):
        if time.perf_counter() - self.last_trig > self.duration:
            self.synth.freq = self.synth.freq * random.choice(self.semi_intervals)
            self.adsr.play()
            self.last_trig = time.perf_counter()


