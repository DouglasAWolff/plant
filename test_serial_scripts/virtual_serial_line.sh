# creates the PTYs
echo "Creating virtual serial ports /tmp/plant_simulator_S0 and /tmp/plant_S0"
socat -d -d pty,raw,echo=0,link=/tmp/plant_simulator pty,raw,echo=0,link=/tmp/plant