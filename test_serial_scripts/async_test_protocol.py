import asyncio


class ArduinoOutputProtocol(asyncio.Protocol):
    def __init__(self):
        super().__init__()
        self._transport = None

    def connection_made(self, _transport):
        self._transport = _transport
        print("Connection made")

    def send_data(self, data):
        print("Connection lost")
        self._transport.write(data)
