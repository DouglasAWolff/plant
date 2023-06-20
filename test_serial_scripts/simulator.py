import asyncio
from dotenv import load_dotenv
import random
import time
from os import environ as env
from serial_asyncio import create_serial_connection
from async_test_protocol import ArduinoOutputProtocol


async def task_play(_transport, _protocol, _plant_number):
    while True:
        print("Playing", time.perf_counter())

        _protocol.send_data(f"{_plant_number}\n".encode())
        sleep_time = random.random() * 10 + 3
        print(f"Sleeping for {sleep_time} seconds")
        await asyncio.sleep(random.random() * sleep_time)


if __name__ == '__main__':
    load_dotenv()  # take environment variables from .env file.

    # NB these will never be used in production. Just making this configurable for testing purposes
    ser_port = env.get('FAKE_ARDUINO_SERIAL_PORT', '/tmp/plant_S0')
    ser_baudrate = env.get('FAKE_ARDUINO_SERIAL_BAUDRATE', 115200)

    ser1_port = env.get('FAKE_ARDUINO_SERIAL1_PORT', '/tmp/plant_ACM1')
    ser1_baudrate = env.get('FAKE_ARDUINO_SERIAL1_BAUDRATE', 115200)

    tasks = [task_play] * 6

    loop = asyncio.get_event_loop()
    coro = create_serial_connection(loop, ArduinoOutputProtocol, ser_port, baudrate=ser_baudrate)
    coro1 = create_serial_connection(loop, ArduinoOutputProtocol, ser1_port, baudrate=ser1_baudrate)
    transport_1_2_3, protocol_1_2_3 = loop.run_until_complete(coro)
    transport_4_5_6, protocol_4_5_6 = loop.run_until_complete(coro1)

    for idx, x in enumerate(tasks):
        _task = tasks[idx]
        plant_number = idx + 1
        if plant_number < 4:
            loop.create_task(_task(transport_1_2_3, protocol_1_2_3, plant_number))
        else:
            loop.create_task(_task(transport_4_5_6, protocol_4_5_6, plant_number))

    loop.run_forever()
    loop.close()
