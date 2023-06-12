//Libraries
#include <CapacitiveSensor.h>//https://github.com/PaulStoffregen/CapacitiveSensor
//Parameters
const int sensitivity   = 10;

int pcap1 = 0;
int pcap2 = 0;
int pcap3 = 0;

CapacitiveSensor cs1   = CapacitiveSensor(2, 3);
CapacitiveSensor cs2   = CapacitiveSensor(8, 9);
CapacitiveSensor cs3   = CapacitiveSensor(12, 11);

void setup() {
  Serial.begin(115200);
  
}

void loop() {
  int cap1 = cs1.capacitiveSensor(sensitivity);
  int cap2 = cs2.capacitiveSensor(sensitivity);
  int cap3 = cs3.capacitiveSensor(sensitivity);
  if (cap1 > 100) {
    Serial.println(1);
  }
  if (cap2 > 100) {
    Serial.println(2);
  }
  if (cap3 > 100) {
    //Serial.println(cap3);
    Serial.println(3);
  }
}
