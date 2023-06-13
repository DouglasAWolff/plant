//Libraries
#include <CapacitiveSensor.h>//https://github.com/PaulStoffregen/CapacitiveSensor
//Parameters
const int sensitivity   = 10;

int pcap1 = 0;
int pcap2 = 0;
int pcap3 = 0;

CapacitiveSensor cs1   = CapacitiveSensor(2, 3);
CapacitiveSensor cs2   = CapacitiveSensor(2, 9);
CapacitiveSensor cs3   = CapacitiveSensor(2, 11);

void setup() {
  Serial.begin(115200);
  cs1.reset_CS_AutoCal();
}

void loop() {
  int cap1 = cs1.capacitiveSensor(sensitivity);
  int cap2 = cs2.capacitiveSensor(sensitivity);
  int cap3 = cs3.capacitiveSensor(sensitivity);
  // Serial.print(cap1);
  // Serial.print(" ");
  // Serial.print(cap2);
  // Serial.print(" ");
  // Serial.println(cap3);


  if (abs(pcap1 - cap1)> ((cap1 + 2)*5)) {
    Serial.println(1);
  }
  if (abs(pcap2 - cap2)> ((cap2 + 2)*5)) {
    Serial.println(2);
  }
  if (abs(pcap3 - cap3)> ((cap3 + 2)*5)) {
    Serial.println(3);
  }

  pcap1 = cap1;
  pcap2 = cap2;
  pcap3 = cap3;
  
}
