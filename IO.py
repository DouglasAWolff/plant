import serial
import random
import time
from pythonosc import udp_client

client = udp_client.SimpleUDPClient('127.0.0.1', 4560)

inlen = 10
numvar = 3

inputs = [[x for x in range(numvar)] for i in range(inlen)]

touch = [False for i in range(numvar)]

def is_touch(sens):
    if sum(inputs[-2:][sens])/2 > 500:
        return True
    else:
        return False

def is_new_touch(sens):
    if touch[sens]:
        touch[sens] = is_touch(sens) 
        return False
    else:
        touch[sens] = is_touch(sens)
        return touch[sens]

while True:
    with serial.Serial('/dev/ttyS0', '115200') as ser: #add timeout later
        ser.write(1)
        inp = ser.readline().decode('utf-8')
        try:
            inputs.append(eval(inp[:-2]))
        except:
            print(f"error happened evaluating this --> {inp}")
            time.sleep(10)
        inputs.pop(0)
    
    if is_new_touch(0):
        client.send_message(f"/pitch1", random.randint(60,65))

import serial
import random
import time
from pythonosc import udp_client

client = udp_client.SimpleUDPClient('127.0.0.1', 4560)

inlen = 10
numvar = 3

inputs = [[x for x in range(numvar)] for i in range(inlen)]

touch = [False for i in range(numvar)]

def is_touch(sens):
    if sum(inputs[-2:][sens])/2 > 500:
        return True
    else:
        return False

def is_new_touch(sens):
    if touch[sens]:
        touch[sens] = is_touch(sens) 
        return False
    else:
        touch[sens] = is_touch(sens)
        return touch[sens]

while True:
    with serial.Serial('/dev/ttyS0', '115200') as ser: #add timeout later
        ser.write(1)
        inp = ser.readline().decode('utf-8')
        try:
            inputs.append(eval(inp[:-2]))
        except:
            print(f"error happened evaluating this --> {inp}")
            time.sleep(10)
        inputs.pop(0)
    
    if is_new_touch(0):
        client.send_message(f"/pitch1", random.randint(60,65))

