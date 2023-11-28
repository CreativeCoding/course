# import pyserial list ports tool
import serial.tools.list_ports as ports

# create a list of all comm ports ['COM1','COM2']
com_ports = list(ports.comports())

# Iterate through list
for i in com_ports:
    print(i.device)
