# Virtual COM Port project on STM32F412 Discovery
This is a VCP project that peripherals of an STM32 microcontroller are controlled over USB. A user can read and change the logic state of any GPIO pin of the microcontroller, or communicate with a serial device connected to any UART interface of the microcontroller. For the project, I made a Python program with a graphical user interface which can connect to serial devices, send messages as text and hex with automatic calculated checksum value, and receive messages from serial devices.

## Serial Console
<img width="400" alt="gpio_3" src="https://user-images.githubusercontent.com/54535282/140710447-8f2d07b9-68a5-4dc4-8e31-e9ab9aeea00b.png"> <img width="400" alt="uart1" src="https://user-images.githubusercontent.com/54535282/140710637-f181fde7-820e-4e5a-af1d-43a0b00b02c8.png">

Serial console is located in /BarkoSerial directory.
