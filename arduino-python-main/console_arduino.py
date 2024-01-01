import serial
import time
ser = serial.Serial(port = "COM3")  
time.sleep(2)
ser.reset_input_buffer()

while True:
    try:
        text = input("Write on\off: ")
        if text == "on":
            ser.write(b'H')
        if text == "off":
            ser.write(b'L')

    except:
        print("Keyboard Interrupt")
        break
