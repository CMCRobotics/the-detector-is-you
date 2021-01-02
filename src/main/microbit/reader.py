from microbit import *
from math import sqrt,ceil

def distance(point1, point2):
    return sqrt( ((point1[0]-point2[0])**2)+((point1[1]-point2[1])**2) )

def scale(unscaled, to_min, to_max, from_min, from_max):
    return (to_max-to_min)*(unscaled-from_min)/(from_max-from_min)+to_min

def scale_distance(point1, point2):
    return ceil(scale(distance(point1, point2), 9, 0, 0,2894))


scope = Image("03330:"
              "30003:"
              "30303:"
              "30003:"
              "03330")
sight = Image("00000:"
              "01110:"
              "01010:"
              "01110:"
              "00000")
countdown = Image("90009:"
              "00000:"
              "00000:"
              "00000:"
              "90009")


val = 0
display.show(scope)

target = [500,-200]
while True:
    newval = scale_distance(target, [accelerometer.get_x(),accelerometer.get_y()])
    if(val != newval):
        val = newval
        display.show(scope+(sight*val))
    sleep(100)
