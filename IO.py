import traceback
from os import environ as env

import serial
from dotenv import load_dotenv
from pyo import *

from plant_lib import Plant1, Plant2, PlantServer, TritonePlant3, SamplePlant4, SamplePlant5

load_dotenv()  # take environment variables from .env.

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


################################################################################
#                                main loop                                     #
################################################################################
zcount = [time.perf_counter() for _ in range(6)]

ser_port = env.get('SERIAL_PORT', '/dev/ttyS0')
ser_baudrate = env.get('SERIAL_BAUDRATE', 115200)
ser_timeout = env.get('SERIAL_TIMEOUT', 0.5)

ser1_port = env.get('SERIAL1_PORT', '/dev/ttyACM1')
ser1_baudrate = env.get('SERIAL1_BAUDRATE', 115200)
ser1_timeout = env.get('SERIAL1_TIMEOUT', 0.5)

# TODO: check ser_baudrate and ser_timeout are int and float and not strings

ser = serial.Serial(ser_port, ser_baudrate, timeout=ser_timeout)
ser1 = serial.Serial(ser1_port, ser1_baudrate, timeout=ser1_timeout)

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
        if inp == 1:
            plant1.play()
            zcount[0] = 0

        elif inp == 2:
            plant2.play()
            zcount[1] = 0

        elif inp == 3:
            tritone_plant3.play()
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
        if inp1 == 4:
            sample_plant4.update_sample()
            sample_plant4.play()
            zcount[3] = 0

        elif inp1 == 5:
            sample_plant5.update_sample()
            sample_plant5.play()
            zcount[4] = 0

        elif inp1 == 6:
            sample_plant6.update_sample()
            sample_plant6.play()
            zcount[5] = 0

finally:
    ser.close()
    ser1.close()