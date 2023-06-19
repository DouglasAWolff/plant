from pyo import *

class PlantServer(Server):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print("PlantServer init")
        print(pa_get_output_devices())
        self.f = None
        self.a = None
        # # pa_get_output_devices()[0].index('default'))
        # macbook pro speakers
        self.setInOutDevice(5)
        self.boot()
        self.start()
        self.setup_plant_sounds()
        self.play_test()

    def setup_plant_sounds(self):
        self.f = Adsr(attack=0.1, decay=1, sustain=0, release=0, dur=1.5, mul=.5)
        self.a = Sine(freq=340, mul=self.f).out()

    def play_test(self):

        self.f.play()
        time.sleep(0.5)
        self.f.play()
        time.sleep(0.5)

    def update_frequency(self, val):
        self.a.freq = self.a.freq * val

    def play_frequency(self):
        self.f.play()
