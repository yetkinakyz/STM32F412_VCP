# Modules
import io
import sys
import glob
import serial
import serial.tools.list_ports

# Variables
counter = 1

# List available serial ports
ports = serial.tools.list_ports.comports()
print("\n AVAILABLE SERIAL PORTS ")
print("========================")
for port in sorted(ports):
        print("[  {}  ]: {}".format(counter, port))
        counter += 1

# Serial port configuration
serialPort = serial.Serial() #Serial iinitialization
serialPort.port = input("\nPORT: ") #Set port
serialPort.baudrate = input("BAUDRATE (Default = 9600): ") #Set baudrate
serialPort.open() #Open serial

# Serial port check
if serialPort.is_open:
    print("\n[  i  ]: Done.")
else:
    print("\n[  !  ]: Error!")

while True:
    # Get data from user
    dataSending = input("\n>>> ")

    # Calculate checksum
    checksum = int(hex(ord(dataSending[0])), 16)
    for n in range(1, len(dataSending)):
        checksum = checksum ^ int(hex(ord(dataSending[n])), 16)

    # Add checksum to data
    dataSending += chr(checksum)

    #print(str(checksum))
    #print(str(dataSending))

    #Send message to device
    serialPort.write(dataSending.encode('Ascii'))

    # Receive data from device
    dataReceived = serialPort.readline(len(dataSending))
    print("\n[STM32]: " + "|" + dataReceived.hex('|', -1) + "|")