"""
https://problemsolvingwithpython.com/11-Python-and-External-Hardware/11.03-Controlling-an-LED/#:~:text=In%20the%20next%20part%20of,off%20for%20about%205%20seconds."""

# import libraries
import serial
import time

# Instantiate a serial object and connect it to 'COM4' - check the Arduino port number!!!
ser = serial.Serial('COM4', 9800, timeout=1)

# Wait for a bit while it handshakes the connection
time.sleep(2)

# In a loop
for i in range(10):
    ser.writelines(b'H')   # send a byte
    time.sleep(0.5)        # wait 0.5 seconds
    ser.writelines(b'L')   # send a byte
    time.sleep(0.5)

# It is only proper to close the connection
ser.close()

"""
ARDUINO CODE
// Arduino IDE: 
// File -> Examples -> 04.Communication -> PhysicalPixel

const int ledPin = 13; // pin the LED is attached to
int incomingByte;      // variable stores  serial data

void setup() {
  // initialize serial communication:
  Serial.begin(9600);
  // initialize the LED pin as an output:
  pinMode(ledPin, OUTPUT);
}

void loop() {
  // see if there's incoming serial data:
  if (Serial.available() > 0) {
    // read the oldest byte in the serial buffer:
    incomingByte = Serial.read();
    // if it's a capital H (ASCII 72), turn on the LED:
    if (incomingByte == 'H') {
      digitalWrite(ledPin, HIGH);
    }
    // if it's an L (ASCII 76) turn off the LED:
    if (incomingByte == 'L') {
      digitalWrite(ledPin, LOW);
    }
  }
}
"""