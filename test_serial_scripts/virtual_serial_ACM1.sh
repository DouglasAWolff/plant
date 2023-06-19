# creates the PTYs
echo "Creating virtual serial ports /tmp/plant_simulator_ACM1 and /tmp/plant_ACM1"
socat -d -d pty,raw,echo=0,link=/tmp/plant_simulator_ACM1 pty,raw,echo=0,link=/tmp/plant_ACM1