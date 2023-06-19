import serial
import random
import time
from pyo import * 
import traceback

from plant_lib import Plant1, Plant2, PlantServer

################################################################################
#                               pyo setup                                      #
################################################################################

s = PlantServer(duplex=0, nchnls=2)

################################################################################
#                        classes/functions setup                               #
################################################################################

plant1 = Plant1()
plant2 = Plant2()




################################################################################
#                                main loop                                     #
################################################################################
zcount = [time.perf_counter() for i in range(6)]

ser = serial.Serial('/tmp/plant_simulator_S0', '115200', timeout=0.5)
ser1 = serial.Serial('/tmp/plant_simulator_ACM1', '115200', timeout=0.5)

# ser = serial.Serial('/dev/ttyS0', '115200', timeout=0.5)
# ser1 = serial.Serial('/dev/ttyACM1', '115200', timeout=0.5)
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
        if not inp == 0:
            if inp == 1 and zcount[0] - time.perf_counter() < -0.3:
                s.update_frequency(random.choice([2.0**(1/12),1/(2.0**(1/12))]))
                s.play_frequency()
                zcount[0] = 0

            elif inp == 2 and zcount[1] - time.perf_counter() < -0.3:
                plant1.play()
                zcount[1] = 0

            elif inp == 3 and zcount[2] - time.perf_counter() < -0.3:
                plant2.play()
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
        if not inp1 == 0:
            if inp1 == 4 and zcount[3] - time.perf_counter() < -0.3:
                s.update_frequency(random.choice([2.0**(1/12),1/(2.0**(1/12))]))
                s.play_frequency()
                zcount[3] = 0

            elif inp1 == 5 and zcount[4] - time.perf_counter() < -0.3:
                plant1.play()
                zcount[4] = 0

            elif inp1 == 6 and zcount[5] - time.perf_counter() < -0.3:
                plant2.play()
                zcount[5] = 0

finally:
    ser.close()
    ser1.close()