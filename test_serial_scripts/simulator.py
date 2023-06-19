"""
Simulate a Plant server.


Usage:

    python simulator.py [addr]

    addr: serial port address (default: /tmp/plant_simulator)

Example:

    python simulator.py /tmp/plant_simulator

Reads from the serial port in infinite loop and prints the response.

"""

import sys
import logging

import serial

DEFAULT_ADDR = '/tmp/plant_simulator'

logging.basicConfig(level=logging.INFO)

addr = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_ADDR

conn = serial.serial_for_url(addr)
logging.info(f'Ready to receive requests on {addr}')
while True:
    request = conn.readline()
    logging.info('REQ: %r', request)
    request = request.strip().decode().lower()
    reply = 'Cryo-con,24C,305682,1.05A\n' if request == '*idn?' else 'NACK\n'
    reply = reply.encode()
    logging.info('REP: %r', reply)
    conn.write(reply)