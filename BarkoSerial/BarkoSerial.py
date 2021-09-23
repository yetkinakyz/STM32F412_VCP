#### Imports
from __future__ import unicode_literals
from pathlib import Path
from threading import Thread
from typing import ValuesView
import serial
import serial.tools.list_ports
from tkinter.ttk import *
from tkinter import *
from tkinter import scrolledtext
from PIL import Image, ImageTk
import os
import pwd

#### Variables
dataSendingText = ''

sendByBytes = False
checksum = 0x00

#### Serial init
serialPort = serial.Serial()

#### Window init
window = Tk()
window.title("Serial Console - BARKO Electronics®")
window.geometry('535x580')
window.resizable(width=False, height=False)

#### Logo image
logoBarko = ImageTk.PhotoImage(Image.open(Path("logo.png")))
labelLogo = Label(window, bd=0, image = logoBarko)
labelLogo.grid(column=0, row=0, sticky = W, padx=190, pady = 10)

#### Port list
labelPort = Label(window, text="Serial Port", font=("Arial", 16))
labelPort.grid(column=0, row=2, sticky = W, padx = 80, pady = 2)
comboPort = Combobox(window, width = 19, font=("Arial", 16))
comboPort.grid(column=0, row=2, sticky = W, padx = 170, pady = 2)

#### Baudrate list
labelBaudrate = Label(window, text="Baudrate(Bit/s)", font=("Arial", 16))
labelBaudrate.grid(column=0, row=3, sticky = W, padx = 50, pady = 2)
comboBaudrate = Combobox(window, width = 19, font=("Arial", 16))
comboBaudrate['values']= (300, 1200, 9600, 115200)
comboBaudrate.grid(column=0, row=3, sticky = W, padx = 170, pady = 2)

#### Refresh port list button
def refresh_ports():
    ports = serial.tools.list_ports.comports()
    connected = []
    for element in ports:
        connected.append(element.device)
    comboPort['values']= (connected)
btn_refresh = Button(window, text="Refresh", command = refresh_ports, width = 10, font=("Arial", 16))
btn_refresh.grid(column=0, row=2, sticky = W, padx = 375, pady = 2)

#### Terminal box
consoleText = scrolledtext.ScrolledText(window, width = 68, height = 21, state='disabled', background = 'black', foreground = "white", font=("Courier", 12))
consoleText.grid(column=0, row=5, sticky = W, padx = 15, pady = 10)

# Print text to terminal box
def txt_print(data):
    consoleText.configure(state ='normal')
    consoleText.insert(END,data)
    consoleText.see(END)
    consoleText.configure(state ='disabled')

#### Receive from device
def receive(): 
    while True:
        if serialPort.is_open:
            # Print received data on terminal box
            try:
                dataReceived = serialPort.readline() #Get data from device
                print(dataReceived)
                # If data exists
                if dataReceived != b'':
                    txt_print("[" + comboPort.get() + "]:" + dataReceived.decode('utf-8'))
                    
            except:
                serialPort.close()
                txt_print("[ i ]: Disconnected.\n")
                buttonConnect.configure(text = "Connect", command = connect)
                break
                

#### Connect and disconnect button
def connect():
    if serialPort.is_open:
        serialPort.close()

    serialPort.port = comboPort.get() # Get port
    serialPort.baudrate = comboBaudrate.get() #Get bauddrate
    serialPort.open() #Open serial
    # Serial port check
    if serialPort.is_open:
        txt_print("[ i ]: Connected.\n")
        buttonConnect.configure(text = "Disconnect", command = disconnect) # Change connect button to disconnect button

        Thread(target = receive).start()
    else:
        txt_print("[ ! ]: Error.\n")

def disconnect():
    serialPort.close() #Open serial
    # Serial port check
    if not serialPort.is_open:
        txt_print("[ i ]: Disconnected.\n")
        buttonConnect.configure(text = "Connect", command = connect)
    else:
        txt_print("[ ! ]: Error.\n")

buttonConnect = Button(window, text="Connect", command = connect, width = 10, font=("Arial", 16))
buttonConnect.grid(column=0, row=3, sticky = W, padx = 375, pady = 2)

#### Sending textbox
textTextboxLabel = Label(window,width = 5, text = "Text:", font=("Arial", 16))
textTextboxLabel.grid(column=0, row=7, sticky = W, padx = 15)
#textTextboxLabel.grid_forget()
textTextbox = Entry(window,width = 49, font=("Arial", 16))
textTextbox.grid(column=0, row=7, sticky = W, padx = 65)
#textTextbox.grid_forget()

#### Sending bitwise textbox labels
bytesLabel = Label(window,width = 5, text = "Hex:", font=("Arial", 16))
#bytesLabel.grid(column=0, row=7, sticky = W, padx = 20)

byte0xLabel = Label(window,width = 2, text = "0x", font=("Arial", 16))
#byte0xLabel.grid(column=0, row=7, sticky = W, padx = 85)
byte1xLabel = Label(window,width = 2, text = "0x", font=("Arial", 16))
#byte1xLabel.grid(column=0, row=7, sticky = W, padx = 155.6)
byte2xLabel = Label(window,width = 2, text = "0x", font=("Arial", 16))
#byte2xLabel.grid(column=0, row=7, sticky = W, padx = 226.2)
byte3xLabel = Label(window,width = 2, text = "0x", font=("Arial", 16))
#byte3xLabel.grid(column=0, row=7, sticky = W, padx = 296.8)
byte4xLabel = Label(window,width = 2, text = "0x", font=("Arial", 16))
#byte4xLabel.grid(column=0, row=7, sticky = W, padx = 367.4)
byte5xLabel = Label(window,width = 2, text = "0x", font=("Arial", 16, 'bold'))
#byte5xLabel.grid(column=0, row=7, sticky = W, padx = 438)

#### Sending bitwise textboxes
byte0Textbox = Entry(window,width = 3, font=("Arial", 16))
#byte0Textbox.grid(column=0, row=7, sticky = W, padx = 105)
byte1Textbox = Entry(window,width = 3, font=("Arial", 16))
#byte1Textbox.grid(column=0, row=7, sticky = W, padx = 175.6)
byte2Textbox = Entry(window,width = 3, font=("Arial", 16))
#byte2Textbox.grid(column=0, row=7, sticky = W, padx = 246.2)
byte3Textbox = Entry(window,width = 3, font=("Arial", 16))
#byte3Textbox.grid(column=0, row=7, sticky = W, padx = 316.8)
byte4Textbox = Entry(window,width = 3, font=("Arial", 16))
#byte4Textbox.grid(column=0, row=7, sticky = W, padx = 387.4)
byte5Textbox = Entry(window,width = 3, font=("Arial", 16, 'bold'))
#byte5Textbox.grid(column=0, row=7, sticky = W, padx = 458)

#### Press enter callbacks
def callbackText(event):
    sendText()    
textTextbox.bind('<Return>', callbackText)

def callbackBytes(event):
    sendBytes()
byte0Textbox.bind('<Return>', callbackBytes)
byte1Textbox.bind('<Return>', callbackBytes)
byte2Textbox.bind('<Return>', callbackBytes)
byte3Textbox.bind('<Return>', callbackBytes)
byte4Textbox.bind('<Return>', callbackBytes)
byte5Textbox.bind('<Return>', callbackBytes)

#### Text/Bitwise button
def changeInputType():
    global sendByBytes

    if sendByBytes:
        sendByBytes = False

        byte0Textbox.grid_forget()
        byte1Textbox.grid_forget()
        byte2Textbox.grid_forget()
        byte3Textbox.grid_forget()
        byte4Textbox.grid_forget()
        byte5Textbox.grid_forget()

        byte0xLabel.grid_forget()
        byte1xLabel.grid_forget()
        byte2xLabel.grid_forget()
        byte3xLabel.grid_forget()
        byte4xLabel.grid_forget()
        byte5xLabel.grid_forget()

        bytesLabel.grid_forget()

        textTextbox.grid(column=0, row=7, sticky = W, padx = 65)
        textTextboxLabel.grid(column=0, row=7, sticky = W, padx = 15)

        buttonChecksum.configure(state=DISABLED)
        buttonChangeInput.configure(text = "Hex", command = changeInputType)
        buttonSend.configure(command=sendText)

    # Connection error
    else:
        sendByBytes = True

        textTextbox.grid_forget()
        textTextboxLabel.grid_forget()

        byte0xLabel.grid(column=0, row=7, sticky = W, padx = 85)
        byte1xLabel.grid(column=0, row=7, sticky = W, padx = 155.6)
        byte2xLabel.grid(column=0, row=7, sticky = W, padx = 226.2)
        byte3xLabel.grid(column=0, row=7, sticky = W, padx = 296.8)
        byte4xLabel.grid(column=0, row=7, sticky = W, padx = 367.4)
        byte5xLabel.grid(column=0, row=7, sticky = W, padx = 438)

        byte0Textbox.grid(column=0, row=7, sticky = W, padx = 105)
        byte1Textbox.grid(column=0, row=7, sticky = W, padx = 175.6)
        byte2Textbox.grid(column=0, row=7, sticky = W, padx = 246.2)
        byte3Textbox.grid(column=0, row=7, sticky = W, padx = 316.8)
        byte4Textbox.grid(column=0, row=7, sticky = W, padx = 387.4)
        byte5Textbox.grid(column=0, row=7, sticky = W, padx = 458)

        bytesLabel.grid(column=0, row=7, sticky = W, padx = 20)

        buttonChecksum.configure(state=NORMAL)
        buttonChangeInput.configure(text = "Text", command = changeInputType)
        buttonSend.configure(command=sendBytes)

buttonChangeInput = Button(window, text="Hex", command = changeInputType, width = 10, height = 2, font=("Arial", 16))
buttonChangeInput.grid(column=0, row=8, sticky = W, padx = 165, pady = 20)

#### Checksum button
def checksum():
    variables = [byte1Textbox, byte2Textbox, byte3Textbox, byte4Textbox]
    
    result = int(byte0Textbox.get(), 16)
    for i in variables:
        result ^= int(i.get(), 16)

    byte5Textbox.delete(0, END)
    byte5Textbox.insert(0, hex(result)[2:])
    


buttonChecksum = Button(window, text="Checksum", command=checksum, width = 10, height = 2, state=DISABLED, font=("Arial", 16))
buttonChecksum.grid(column=0, row=8, sticky = W, padx = 65, pady = 20)

#### Clear button
def clear():

    byte0Textbox.delete(0, END)
    byte1Textbox.delete(0, END)
    byte2Textbox.delete(0, END)
    byte3Textbox.delete(0, END)
    byte4Textbox.delete(0, END)
    byte5Textbox.delete(0, END)

    print(byte2Textbox.get())

    textTextbox.delete(0, END)

    # Clear terminal box
    consoleText.configure(state = 'normal')
    consoleText.delete(1.0, END)
    consoleText.configure(state = 'disabled')

buttonClear = Button(window, text="Clear", command=clear, width = 10, height = 2, font=("Arial", 16))
buttonClear.grid(column=0, row=8, sticky = W, padx = 265, pady = 20)

#### Send button
def sendText():
    global dataSendingText

    dataSendingText = textTextbox.get()

    if serialPort.is_open:
        # Print on terminal box
        if dataSendingText != b'':
            txt_print("[" + os.environ.get('USER') + "]:" + dataSendingText + "\n")

        textTextbox.delete(0, END) # Clear sending textbox

        # Calculate checksum
        checksum = int(hex(ord(dataSendingText[0])), 16)
        for n in range(1, len(dataSendingText)):
            checksum = checksum ^ int(hex(ord(dataSendingText[n])), 16)

        dataSendingText += chr(checksum) # Add checksum to sending data
        serialPort.write(dataSendingText.encode('Ascii')) #Send data to device

    # Connection error
    else:
        txt_print("[ ! ]: Error: Not connected.\n")
        textTextbox.delete(0, END)

def sendBytes():
    dataSendingBytes = ''
    dataBytes = [byte0Textbox.get(), byte1Textbox.get(), byte2Textbox.get(), byte3Textbox.get(), byte4Textbox.get(), byte5Textbox.get()]
    
    if serialPort.is_open:
        for byte in range(len(dataBytes)):
            # Print on terminal box
            dataSendingBytes += chr(int(dataBytes[byte], 16))

        txt_print("[" + os.environ.get('USER') + "]:")
        for i in range(len(dataBytes)):
            txt_print("|" + hex(ord(dataSendingBytes[i]))[2:])
        txt_print("|\n")

        serialPort.write(dataSendingBytes.encode('utf-8')) #Send data to device

    # Connection error
    else:
        txt_print("[ ! ]: Error: Not connected.\n")
        textTextbox.delete(0, END)

buttonSend = Button(window, text="Send", command=sendBytes, width = 16, height = 2, font=("Arial", 16))
buttonSend.grid(column=0, row=8, sticky = W, padx = 365, pady = 20)

#### Main loop
window.mainloop()