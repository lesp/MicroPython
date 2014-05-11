# main.py -- put your code here!
import pyb
accel = pyb.Accel()
SENSITIVITY = 3
x1_pin = pyb.Pin.board.X1
g = pyb.Pin(pyb.Pin.board.X1, pyb.Pin.OUT_PP)

def lightup():
    g.high()

while True:
    x = accel.x()
    if abs(x) > SENSITIVITY: 
        lightup()
    else:
        g.low()

    pyb.delay(100)
