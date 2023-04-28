//Libraries
#include <CapacitiveSensor.h>//https://github.com/PaulStoffregen/CapacitiveSensor
//Parameters
bool autocal   = 0;
const int numReadings   = 1;
long readings [numReadings];
int readIndex   = 0;
long total  = 0;
const int sensitivity   = 1000;
const int thresh  = 200;
const int csStep  = 10000;
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
  Serial.begin(9600);
  Serial.println(F("Initialize System"));
  //Init cs
  if (autocal == 0) {
      {
          cs1.set_CS_AutocaL_Millis(0xFFFFFFFF);
      }
  }
}
void loop() {
  int cap1 = smooth1();
  int cap2 = smooth2();
  int cap3 = smooth3();
  Serial.print("A: ");
  Serial.println(cap2);
  if (cap1 > 2000) {
    if (pcap1 - cap1 > 500) {
      digitalWrite(A0, LOW);
    } else {
      Serial.println("AHHHHHHHH");
      digitalWrite(A0, HIGH);
    }
  } else {
    digitalWrite(A0, LOW);  
  }
  if (cap2 > 1500) {
    if (pcap2 - cap2 > 500) {
      digitalWrite(A1, LOW);
    } else {
      Serial.println("AHHHHHHHH");
      digitalWrite(A1, HIGH);
    }
  } else {
    digitalWrite(A1, LOW);  
 }  
  if (cap3 > 1500) {
    if (pcap3 - cap3 > 500) {
      digitalWrite(A2, LOW);
    } else {
      Serial.println("AHHHHHHHH");
      digitalWrite(A2, HIGH);
    }
  } else {
    digitalWrite(A2, LOW);  
 }
 pcap1 = cap1;
 pcap2 = cap2;
 pcap3 = cap3;
   
}
long smooth1() { /* function smooth */
 return cs1.capacitiveSensor(sensitivity);
}
long smooth2() { /* function smooth */
  return cs2.capacitiveSensor(sensitivity);
}
long smooth3() { /* function smooth */
  return cs3.capacitiveSensor(sensitivity);
}
