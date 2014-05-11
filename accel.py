# main.py -- put your code here!
import pyb
from time import sleep
accel = pyb.Accel()
SENSITIVITY = 6
x1_pin = pyb.Pin.board.X1
g = pyb.Pin(pyb.Pin.board.X1, pyb.Pin.OUT_PP)
x12_pin = pyb.Pin.board.X12
h = pyb.Pin(pyb.Pin.board.X12, pyb.Pin.OUT_PP)

def lightup():
    g.high()

def lightup2():
    h.high()

while True:
    x = accel.x()
    y = accel.y()
    if abs(x) > SENSITIVITY: 
        lightup()
        sleep(0.5)
    elif abs(y) > SENSITIVITY:
        lightup2()
        sleep(0.5)
    else:
        g.low()
        h.low()

    pyb.delay(100)
