"""
This file contains the plant class and its subclasses.
"""
import time

from pyo import *

minor_scale = [3, 8, 10]
major_scale = [2, 4, 5, 7, 9, 11, 12]

subs_sample_list = [
    "sub tone 1 em 3_26.wav",
    "sub tone 2 em 3_50.wav",
    "sub tone 3 em 11_00.wav"
]

texture_sample_list = [
    "texture 1 ap 6_17.wav",
    "texture 10 em 8_30.wav",
    "texture 11 em 10_09.wav"
    "texture 12 es 2_07.wav",
    "texture 13 es 3_57.wav",
    "texture 14 es 8_31.wav",
    "texture 15 es 14_59.wav",
    "texture 16 es 15_30.wav",
    "texture 17 hk 1_26.wav",
    "texture 18 hk 5_17.wav",
    "texture 19 md 2_30.wav",
    "texture 2 asi 0_00.wav",
    "texture 20 md 7_45.wav",
    "texture 21 me 13_52.wav",
    "texture 22 me 14_08.wav",
    "texture 23 mt 4_30.wav",
    "texture 24 pt 1_43.wav",
    "texture 25 pt 6_30.wav",
    "texture 26 pt 9_34.wav",
    "texture 27 pt 11_47.wav",
    "texture 3 asi 2_59.wav",
    "texture 4 asi 3_23.wav",
    "texture 5 asi 5_39.wav",
    "texture 6 asi 6_52.wav",
    "texture 7 asi 7_15.wav",
    "texture 8 em 0_55.wav",
    "texture 9 em 5_10.wav",
]

tone_sample_list = [
    "TONE 1 EM 1_11.wav",
    "TONE 2 EM 1_18.wav",
    "TONE 3 EM 2_49.wav",
    "TONE 4 EM 7_33.wav",
    "TONE 5 MT  5_36.wav",
    "TONE 6 MT 0_26.wav",
    "TONE 7 MT 1_20.wav"
]
class Plant:
    def __init__(self):
        self.thresh = 40
        self.pitch = 440
        self.semi_intervals = [2.0 ** (1 / 12), 1 / (2.0 ** (1 / 12))]
        self.lower = 100
        self.upper = 1300

    def is_touch(self, sens):
        return inputs[-1][sens] > thres[sens]

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
        self.invervals = [6 for _ in range(3)] + [1, 3]
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


class SamplePlant4(Plant):
    def __init__(self):
        super().__init__()
        self.path = None
        self.update_sample()
        self.duration = 6
        self.last_trig = time.perf_counter()
        self.players = [0 for _ in range(8)]

    def play(self):
        if time.perf_counter() - self.last_trig > self.duration:
            self.players.append(SfPlayer(self.path, loop=False).out())
            self.players.pop(0)
            self.last_trig = time.perf_counter()

    def update_sample(self):
        random_subs_sample = random.choice(subs_sample_list)
        self.path = f'samples/{random_subs_sample}'


class SamplePlant5(Plant):
    def __init__(self):
        super().__init__()
        self.path = None
        self.update_sample()
        self.duration = 6
        self.last_trig = time.perf_counter()
        self.players = [0 for _ in range(8)]

    def play(self):
        if time.perf_counter() - self.last_trig > self.duration:
            self.players.append(SfPlayer(self.path, loop=False).out())
            self.players.pop(0)
            self.last_trig = time.perf_counter()

    def update_sample(self):
        random_texture_sample = random.choice(texture_sample_list)
        self.path = f'samples/{random_texture_sample}'


class SamplePlant6(Plant):
    def __init__(self):
        super().__init__()
        self.path = None
        self.update_sample()
        self.duration = 6
        self.last_trig = time.perf_counter()
        self.players = [0 for _ in range(8)]

    def play(self):
        if time.perf_counter() - self.last_trig > self.duration:
            self.players.append(SfPlayer(self.path, loop=False).out())
            self.players.pop(0)
            self.last_trig = time.perf_counter()

    def update_sample(self):
        random_tone_sample = random.choice(tone_sample_list)
        self.path = f'samples/{random_tone_sample}'
