import asyncio

class PlantsOneToThreeOutputProtocol(asyncio.Protocol):

    def __init__(self):
        super().__init__()
        self._transport = None
        self.plant1 = None  # plant1
        self.plant2 = None  # plant2
        self.tritone_plant3 = None  # tritone_plant3

    def set_plants(self, plant1, plant2, tritone_plant3):
        self.plant1 = plant1
        self.plant2 = plant2
        self.tritone_plant3 = tritone_plant3

    def connection_made(self, _transport):
        self._transport = _transport
        print('[1-3] port opened', self._transport)

    def data_received(self, data):
        if b'\n' in data:
            ppreinp = data.decode('utf-8')
            preinp = ppreinp.replace("\0", "").replace("\n", "").replace("\r", "")
            print(f'[1-3] data received {ppreinp}')  # so do something
            inp = int(preinp) if len(preinp) > 0 else 0
            if inp == 1:
                self.plant1.play()

            elif inp == 2:
                self.plant2.play()

            elif inp == 3:
                self.tritone_plant3.play()

    def connection_lost(self, exc):
        print('[1-3] port closed')
        self._transport.loop.stop()

    def pause_writing(self):
        print('[1-3] pause writing')
        print(self._transport.get_write_buffer_size())

    def resume_writing(self):
        print(self._transport.get_write_buffer_size())
        print('[1-3] resume writing')


class PlantsFourToSixOutputProtocol(asyncio.Protocol):

    def __init__(self):
        super().__init__()
        self._transport = None
        self.sample_plant4 = None  # sample_plant4
        self.sample_plant5 = None  # sample_plant5
        self.plant6 = None  # plant6

    def set_plants(self, sample_plant4, sample_plant5, plant6):
        self.sample_plant4 = sample_plant4
        self.sample_plant5 = sample_plant5
        self.plant6 = plant6

    def connection_made(self, _transport):
        self._transport = _transport
        print('[4-6] port opened', self._transport)

    def data_received(self, data):
        if b'\n' in data:
            ppreinp = data.decode('utf-8')
            preinp = ppreinp.replace("\0", "").replace("\n", "").replace("\r", "")
            print('[4-6] data received', ppreinp)
            inp = int(preinp) if len(preinp) > 0 else 0
            if inp == 4:
                self.sample_plant4.play()

            elif inp == 5:
                self.sample_plant5.play()

            elif inp == 6:
                self.plant6.play()

    def connection_lost(self, exc):
        print('[4-6] port closed')
        self._transport.loop.stop()

    def pause_writing(self):
        print('[4-6] pause writing')
        print(self._transport.get_write_buffer_size())

    def resume_writing(self):
        print(self._transport.get_write_buffer_size())
        print('[4-6] resume writing')