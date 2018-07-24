import os
import sys
import serial
import keyboard

"""
The program accepts 3 arguments
    PORT: The port at which the Arduino is present
    BAUD: The Baud rate of the Arduino. We can keep that fixed
    KEY: The key to be represented
"""
PORT = sys.argv[1]
BAUD = sys.argv[2]
KEY = sys.argv[3]

s = serial.Serial(PORT, BAUD)


def extractSensorVal():
    """
    This function will fetch sensor values and give proper formatting
    """
    global s
    x = s.readline()
    x = x.decode()
    x = x.rstrip()
    x = x.split(",")
    out = [float(i) for i in x]
    return out

def getStatus(x):
    """
    This function will implement the key press depending on the keypress
    """
    if x[0] > 25 and x[2] > 25:
        keyboard.press(KEY)
    else:
        keyboard.release(KEY)

def main():
    while(True):
        x = extractSensorVal()
        status = getStatus(x)        
        
if __name__ == '__main__':
    main()