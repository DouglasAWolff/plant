"""
This file contains the plant class and its subclasses.
"""
import time

from pyo import *

minor_scale = [3, 8, 10]
major_scale = [2, 4, 5, 7, 9, 11, 12]

class Plant:
    def __init__(self):
        self.thresh = 40
        self.pitch = 440
        self.semi_intervals = [2.0 ** (1 / 12), 1 / (2.0 ** (1 / 12))]
        self.lower = 100
        self.upper = 1300


    def is_touch(self, sens):
        if inputs[-1][sens] > thres[sens]:
            return True
        else:
            return False

    def change_pitch(self, semitones):
        if self.pitch > self.upper:
            self.pitch = self.pitch * (self.semi_intervals[0] ** (abs(semitones) * -1))

        elif self.pitch < self.lower:
            self.pitch = self.pitch * (self.semi_intervals[0] ** abs(semitones))

        else:
            self.pitch = self.pitch * (self.semi_intervals[0] ** semitones)


class Plant1(Plant):
    def __init__(self):
        super().__init__()
        self.duration = 0.2
        self.adsr = Adsr(attack=0.1, decay=0.3, sustain=1, release=.9, dur=0.9, mul=.5)
        self.synth = SuperSaw(freq=340, mul=self.adsr).out()
        self.last_trig = time.perf_counter()
        self.uppper = 400

    def play(self):
        if time.perf_counter() - self.last_trig > self.duration:
            self.change_pitch(random.choice(major_scale) * random.choice([-1, 1]))
            self.synth.freq = self.pitch
            self.adsr.play()
            self.last_trig = time.perf_counter()


class Plant2(Plant):
    def __init__(self):
        super().__init__()
        self.duration = 1
        self.adsr = Adsr(attack=0.4, decay=0.3, sustain=1, release=.3, dur=self.duration, mul=0.7)
        self.mod = Sine(freq=6, mul=50)
        self.synth = Sine(freq=self.mod + 320, mul=self.adsr).out()
        self.last_trig = time.perf_counter()
        self.lower = 500

    def play(self):
        if time.perf_counter() - self.last_trig > self.duration:
            self.change_pitch(random.choice(minor_scale) * random.choice([-1, 1]))
            self.synth.freq = self.pitch
            self.adsr.play()
            self.last_trig = time.perf_counter()

class TritonePlant3(Plant):
    def __init__(self):
        super().__init__()
        self.duration = 1
        self.invervals = [6 for i in range(3)] + [1, 3]
        self.adsr = Adsr(attack=0.1, decay=0.3, sustain=1, release=.9, dur=self.duration, mul=0.7)
        self.mod = Sine(freq=6, mul=50)
        self.synth = Sine(freq=self.mod + 320, mul=self.adsr).out()
        self.last_trig = time.perf_counter()
        self.upper = 400

    def play(self):
        if time.perf_counter() - self.last_trig > self.duration - 0.7:
            self.change_pitch(random.choice(self.invervals) * random.choice([-1, 1]))
            self.synth.freq = self.pitch
            self.adsr.play()
            self.last_trig = time.perf_counter()

class SamplePlant4():
    def __init__(self):
        self.path = 'samples/KAZOO.wav'
        self.duration = 6
        self.last_trig = time.perf_counter()
        self.players = [0 for i in range(8)]

    def play(self):
        if time.perf_counter() - self.last_trig > self.duration:
            self.players.append(SfPlayer(self.path, loop=False).out())
            self.players.pop(0)
            self.last_trig = time.perf_counter()

class SamplePlant5():
    def __init__(self):
        self.path = 'samples/london underground.wav'
        self.duration = 6
        self.last_trig = time.perf_counter()
        self.players = [0 for i in range(8)]

    def play(self):
        if time.perf_counter() - self.last_trig > self.duration:
            self.players.append(SfPlayer(self.path, loop=False).out())
            self.players.pop(0)
            self.last_trig = time.perf_counter()
