import cv2
import datetime
import math
from constants import COLORS
from constants import RADIUS
from constants import CENTER

def get_ticks():
    hours_init = []
    hours_det = []

    for i in range(0,360,6):
        x_coordinate =int(CENTER[0] + RADIUS * math.cos(i * math.pi /180))
        y_coordinate = int(CENTER[1] + RADIUS * math.sin(i * math.pi /180))

        hours_init.append((x_coordinate,y_coordinate))

    for i in range(0,360,6):
        x_coordinate = int(CENTER[0] + (RADIUS-20) * math.cos(i * math.pi/180))
        y_coordinate = int(CENTER[1] + (RADIUS-20) * math.sin(i * math.pi/180))

        hours_det.append((x_coordinate,y_coordinate))

    return hours_init, hours_det

def getDigitalTime(h,m,s):
    time = ""
    hour = ""
    minute = ""
    second = ""
    if(h<10):
        hour = "0{}:".format(h)
    else:
        hour = "{}:".format(h)
    if(m<10):
        minute = "0{}:".format(m)
    else:
        minute = "{}:".format(m)
    if(s<10):
        second = "0{}:".format(s)
    else:
        second = "{}:".format(s)
    time = hour+minute+second
    return time
