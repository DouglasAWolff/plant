"""

Usage:
    python client.py [addr [cmd]]

    addr: serial port address (default: /tmp/plant)
    cmd: command to send (default: *IDN?)

Example:
    python client.py /tmp/plant '*IDN?'

Sends a command to the serial port and prints the response.
"""

import sys
import serial
DEFAULT_ADDR = '/tmp/plant'
DEFAULT_CMD = '*IDN?'
args = len(sys.argv) - 1
if args == 0:
    addr, cmd = DEFAULT_ADDR, DEFAULT_CMD
elif args == 1:
    addr, cmd = DEFAULT_ADDR, sys.argv[1]
else:
    addr, cmd = sys.argv[1:3]

cmd += '\n'
s = serial.serial_for_url(addr)
s.write(cmd.encode())
# print(s.readline())
s.close()
exit()
