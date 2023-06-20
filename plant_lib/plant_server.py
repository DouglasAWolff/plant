from pyo import *

class PlantServer(Server):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print("PlantServer init")
        # print(pa_get_default_devices_from_host('core audio'))
        self.f = None
        self.f_reverb = None
        self.a = None
        self.a_reverb = None
        # macbook pro speakers
        self.setInOutDevice((1, 2))
        # this might be Raspberry Pi specific
        # # pa_get_output_devices()[0].index('default'))
        self.boot()
        self.start()
        self.setup_plant_sounds()
        self.play_test()

    def setup_plant_sounds(self):
        self.f = Adsr(attack=0.1, decay=1, sustain=0, release=0, dur=1.5, mul=.5)
        self.f_reverb = Freeverb(self.f, size=0.8, damp=0.5, bal=0.3)
        self.f_reverb.out()

        self.a = Sine(freq=340, mul=self.f).out()

        self.a_reverb = Freeverb(self.a, size=[.79,.8], damp=.9, bal=.3) #size=0.8, damp=0.5, bal=0.3)
        self.a_reverb.out()

    def play_test(self):

        self.f.play()
        time.sleep(0.5)
        self.f.play()
        time.sleep(0.5)

    def update_frequency(self, val):
        self.a.freq = self.a.freq * val

    def play_frequency(self):
        self.f.play()
