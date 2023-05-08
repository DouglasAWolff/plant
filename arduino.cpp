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
  pinMode(A0, OUTPUT);
  pinMode(A1, OUTPUT);
  pinMode(A2, OUTPUT);
  //Init Serial USB
  Serial.begin(115200);
  Serial.println(F("Initialize System"));
}

void loop() {
  int cap1 = cs1.capacitiveSensor(sensitivity);
  int cap2 = cs2.capacitiveSensor(sensitivity);
  int cap3 = cs3.capacitiveSensor(sensitivity);
  Serial.println(cap1);
  if (pcap1 < 500 && cap1 < 500) {
    digitalWrite(A0, LOW);
  } else {
    digitalWrite(A0, HIGH);  
  }
  if (pcap2 < 500 && cap2 < 500) {
    digitalWrite(A1, LOW);
  } else {
    digitalWrite(A1, HIGH);  
  }  
 if (pcap3 < 500 && cap3 < 500) {
  digitalWrite(A2, LOW);
 } else {
  digitalWrite(A2, HIGH);  
 }
 pcap1 = cap1;
 pcap2 = cap2;
 pcap3 = cap3;
   
}

