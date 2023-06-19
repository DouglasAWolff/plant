import asyncio
from os import environ as env
from dotenv import load_dotenv
from pyo import *

from plant_lib import Plant1, Plant2, PlantServer, TritonePlant3, SamplePlant4, SamplePlant5
from plant_lib.async_protocols import PlantsOneToThreeOutputProtocol, PlantsFourToSixOutputProtocol

from serial_asyncio import create_serial_connection


# test
if __name__ == '__main__':
    load_dotenv()  # take environment variables from .env file.
    ################################################################################
    #                               pyo setup                                      #
    ################################################################################

    s = PlantServer(duplex=0, nchnls=2)

    ################################################################################
    #                        classes/functions setup                               #
    ################################################################################

    plant1 = Plant1()
    plant2 = Plant2()
    tritone_plant3 = TritonePlant3()
    sample_plant4 = SamplePlant4()
    sample_plant5 = SamplePlant5()

    # new class needed for plant 6
    plant6 = Plant2()

    ################################################################################
    #                                main loop                                     #
    ################################################################################

    ser_port = env.get('SERIAL_PORT', '/dev/ttyS0')
    ser_baudrate = env.get('SERIAL_BAUDRATE', 115200)

    ser1_port = env.get('SERIAL1_PORT', '/dev/ttyACM1')
    ser1_baudrate = env.get('SERIAL1_BAUDRATE', 115200)

    loop = asyncio.get_event_loop()
    coro = create_serial_connection(loop, PlantsOneToThreeOutputProtocol, ser_port, baudrate=ser_baudrate)
    coro1 = create_serial_connection(loop, PlantsFourToSixOutputProtocol, ser1_port, baudrate=ser1_baudrate)
    transport, protocol = loop.run_until_complete(coro)
    transport1, protocol1 = loop.run_until_complete(coro1)
    protocol.set_plants(plant1, plant2, tritone_plant3)
    protocol1.set_plants(sample_plant4, sample_plant5, plant6)

    loop.run_forever()
    loop.close()