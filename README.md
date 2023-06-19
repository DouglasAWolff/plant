# plant

## Setup

### Setup virtual environment

```bash
$ python -m venv venv
$ source venv/bin/activate
```

### Install dependencies
```bash
$ pip install -r requirements.txt
```

## Running (production)

Make sure the Arduino is connected, and the serial port is set correctly in `IO.py` (default is `/dev/ttyACM0`).

### Run IO.py

```bash
$ source venv/bin/activate
$ python IO.py
```
To stop - CTRL + C (or pull the plug)


### Troubleshooting / Debugging IO.py

To run test setup:

Install [`socat`](http://www.dest-unreach.org/socat/)) locally (via `brew` or `apt-get`)

Then in one terminal run (for plants 1 to 3):

```bash
$ ./test_serial_scripts/virtual_serial_S0.sh
```

and in another 

```bash
$ ./test_serial_scripts/virtual_serial_ACM1.sh
```
[ plants 4 - 6 ]

Some example output:

```bash
2023/06/19 12:45:51 socat[18750] N PTY is /dev/ttys008
2023/06/19 12:45:51 socat[18750] N PTY is /dev/ttys009
2023/06/19 12:45:51 socat[18750] N starting data transfer loop with FDs [5,5] and [7,7]
```

This creates two pseudo terminals (pty) `/tmp/plant_simulator_S0` and `/tmp/plant_simulator_ACM1`, which are used by `IO.py` (as with the true serial connections) to receive input from the arduino collecting capacitance data about the plants with sensors in the soil.

To test a plant, run the following in a third terminal:
```bash
$ python test_serial_scripts/client.py /tmp/plant_S0 2
```
[ where 2 is the plant number which is connected to `/tmp/plant_simulator_S0` ]

1 2 or 3 can be used with /tmp/plant_simulator_S0

4 5 or 6 can be used with /tmp/plant_simulator_ACM1

```bash
$ python test_serial_scripts/client.py /tmp/plant_ACM1 5
```
