# main.py -- put your code here!
import pyb
import time
sw = pyb.Switch()
def lightup():
    x1_pin = pyb.Pin.board.X1

    g = pyb.Pin(pyb.Pin.board.X1, pyb.Pin.OUT_PP)

    for i in range(1,4):
        g.high()
        pyb.delay(1000)
        g.low()
        pyb.delay(1000)

sw.callback(lightup)
