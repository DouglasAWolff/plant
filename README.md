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





### Troubleshooting / Debugging

To run test setup:

Install [`socat`](http://www.dest-unreach.org/socat/)) locally (via `brew` or `apt-get`)

Then in one terminal run:

```bash
$ ./test_serial_scripts/virtual_serial_line.sh
```

Note the pseudo terminal(s) that are created by `socat`, some example output:

```bash
 % ./test_serial_scripts/virtual_serial_line.sh 
2023/06/19 12:45:51 socat[18750] N PTY is /dev/ttys008
2023/06/19 12:45:51 socat[18750] N PTY is /dev/ttys009
2023/06/19 12:45:51 socat[18750] N starting data transfer loop with FDs [5,5] and [7,7]
```

This creates a pseudo terminal (pty) `/tmp/plant_simulator`, which can be read using the following command in a new terminal:
```bash
$ python test_serial_scripts/simulator.py /tmp/plant_simulator
```

In another terminal run:

```bash
$ python test_serial_scripts/client.py
```
This sends a test message or two to the simulator, which should be echoed back to the client.
