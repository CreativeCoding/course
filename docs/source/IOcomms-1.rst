I/O Comms 1
===========

In these sessions you will learn about Inpuy/ Output communications using pyton.
We will focus on 2 types of I/O comms: the serial port (e.g. USB) and Ip sockets
(e.g. the Internet). To do this we will first explore *pyserial* and the *socket*.

*pyserial*
----------
*pyserial* is a useful package for problem solvers because it allows us to exchange data between
computers and pieces of external hardware such as voltmeters, oscilloscopes, strain gauges, flow meters,
actuators, and lights. *pyserial* provides an interface to communicate over the serial communication protocol.

    | Follow installation instructions here https://people.csail.mit.edu/hubert/pyaudio/


Get *pyserial*
^^^^^^^^^^^^^^
To import *pyserial* into your IDE you may need to install other
dependencies into your system. This differs on OS, so follow the guidance here::

    https://pythonhosted.org/pyserial/pyserial.html#installation

-
    | Full docs for *pyserial* can be found here: https://pythonhosted.org/pyserial/index.html


1. *Hello pyserial*
^^^^^^^^^^^^^^^^^^^^^^^
In this example we will import *pyserial* and list the I/O comms ports on this computer.
This is likely to be a combination of UART, USB and Bluetooth.

Import pyserial list ports tool::

    import serial.tools.list_ports as ports

Create a list of all comm ports ['COM1','COM2']::

    com_ports = list(ports.comports())

Iterate through list and print out to console::

    for i in com_ports:
        print(i.device)
2. Example with Arduino
^^^^^^^^^^^^^^^^^^^^^^^
In this example we will explore a simple in-out communications between Python and an Arduino.
You will need an Arduino for this experiment. The tutorial is taken from here:

    | https://projecthub.arduino.cc/ansh2919/serial-communication-between-python-and-arduino-663756

**PYTHON CODE**

Importing Libraries::

    import serial
    import time

Instantiate a serial object and connect it to 'COM4' - check the Arduino port number!!!::

    arduino = serial.Serial(port='COM4', baudrate=115200, timeout=.1)

Function that sends incoming message to the Arduino in bytes and reads its response.::

    def write_read(x):
        arduino.write(bytes(x, 'utf-8'))  # Formatted as an 8-bit byte
        # Wait for a little bit
        time.sleep(0.05)
        # Read the Arduino's response and return
        data = arduino.readline()
        return data

On an endless loop::

    while True:
        num = input("Enter a number: ") # Taking input from user
        value = write_read(num)
        print(value) # printing the value

**ARDUINO CODE**
You will need to upload this to the Arduino.
Declare an integer variable called x::

    int x;

Setup the serial port parameters::

    void setup() {
      Serial.begin(115200);
      Serial.setTimeout(1);
    }

While there is a connection to the serial port, read the incoming data and print to console::

    void  loop() {
      while (!Serial.available());
      x = Serial.readString().toInt();
      Serial.print(x + 1);
    }

3. Advanced Arduino example: blink
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
In this example we will connect python to an Arduino, and control
one of its LED's. The code has been taken from:

    | https://problemsolvingwithpython.com/11-Python-and-External-Hardware/11.03-Controlling-an-LED/#:~:text=In%20the%20next%20part%20of,off%20for%20about%205%20seconds."""

**PYTHON CODE**

Import libraries::

    import serial
    import time

Instantiate a serial object and connect it to 'COM4' - check the Arduino port number!!!::

    ser = serial.Serial('COM4', 9800, timeout=1)

Wait for a bit while it handshakes the connection::

    time.sleep(2)

In a loop::

    for i in range(10):
        ser.writelines(b'H')   # send a byte
        time.sleep(0.5)        # wait 0.5 seconds
        ser.writelines(b'L')   # send a byte
        time.sleep(0.5)

It is only proper to close the connection. This is important!::

    ser.close()

**ARDUINO CODE**
You will need to upload this to your Arduino. It can be found in the Arduino IDE:
// Arduino IDE:
// File -> Examples -> 04.Communication -> PhysicalPixel

Declare the constants and variables::

    const int ledPin = 13; // pin the LED is attached to
    int incomingByte;      // variable stores  serial data

Open the serial port and initialise the connection to the LED pin (declared in the constant above)::

    void setup() {
      // initialize serial communication:
      Serial.begin(9600);
      // initialize the LED pin as an output:
      pinMode(ledPin, OUTPUT);
    }

If there is a connection, read the incoming signal::

    void loop() {
      // see if there's incoming serial data:
      if (Serial.available() > 0) {
        // read the oldest byte in the serial buffer:
        incomingByte = Serial.read();

// If it's a capital H (ASCII 72), turn on the LED::

        if (incomingByte == 'H') {
          digitalWrite(ledPin, HIGH);
        }

// If it's an L (ASCII 76) turn off the LED::
        if (incomingByte == 'L') {
          digitalWrite(ledPin, LOW);
        }
      }
    }
