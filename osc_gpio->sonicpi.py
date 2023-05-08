import random
import time
from pythonosc import udp_client
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.IN)
GPIO.setup(10, GPIO.IN)
GPIO.setup(12, GPIO.IN)
client = udp_client.SimpleUDPClient('127.0.0.1', 4560)
    
fs = [60,60,60]

i = 0

def msg(channel):
    global fs
    if fs[0] < 60 or fs[1] > 90:
        if not random.randint(0, 5):
            fs[0] = random.randint(75, 85) 
    fs[0] = fs[0] + random.choice([2, 4, 5,7,9,11,-2,-4,-5,-7,-9,-11])
    client.send_message(f"/pitch1", fs[0])

def msg2(channel):
    global fs
    if fs[1] < 60 or fs[1] > 90:
        if not random.randint(0, 5):
            fs[1] = random.randint(75, 85) 
    fs[1] = fs[1] + random.choice([1, 3, 6, 8, 10, -1,-3,-6,-8,-10])
    client.send_message(f"/pitch2", fs[1])

def msg3(channel):
    global fs
    client.send_message(f"/pitch3", random.randint(70,90))
    
GPIO.add_event_detect(8, GPIO.RISING, callback=msg)
GPIO.add_event_detect(10, GPIO.RISING, callback=msg2)
GPIO.add_event_detect(12, GPIO.RISING, callback=msg3) 
