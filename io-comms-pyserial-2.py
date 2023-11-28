"""
https://projecthub.arduino.cc/ansh2919/serial-communication-between-python-and-arduino-663756
"""

# Importing Libraries
import serial
import time

# Instantiate a serial object and connect it to 'COM4' - check the Arduino port number!!!
arduino = serial.Serial(port='COM4', baudrate=115200, timeout=.1)

# Function that sends incoming message to the Arduino in bytes
# and reads its response.
def write_read(x):
    arduino.write(bytes(x, 'utf-8'))  # Formatted as an 8-bit byte
    # Wait for a little bit
    time.sleep(0.05)
    # Read the Arduino's response and return
    data = arduino.readline()
    return data

# On an endless loop
while True:
    num = input("Enter a number: ") # Taking input from user
    value = write_read(num)
    print(value) # printing the value


"""
ARDUINO CODE
============

int x;

void setup() {
  Serial.begin(115200);
  Serial.setTimeout(1);
}

void  loop() {
  while (!Serial.available());
  x = Serial.readString().toInt();
  Serial.print(x + 1);
}
"""