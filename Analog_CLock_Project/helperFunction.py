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

def draw_time(image):
    time_now = datetime.datetime.now().time()
    hour = time_now.hour % 12
    minute = time_now.minute
    second = time_now.second

    # Calculate the angles in radians
    second_angle = math.radians(second * 6 - 90)
    minute_angle = math.radians(minute * 6 - 90)
    hour_angle = math.radians(hour * 30 + minute * 0.5 - 90)

    # Calculate the positions of the hands
    second_x = int(CENTER[0] + (RADIUS - 25) * math.cos(second_angle))
    second_y = int(CENTER[1] + (RADIUS - 25) * math.sin(second_angle))
    cv2.line(image, CENTER, (second_x, second_y), COLORS['black'], 2)

    minute_x = int(CENTER[0] + (RADIUS - 60) * math.cos(minute_angle))
    minute_y = int(CENTER[1] + (RADIUS - 60) * math.sin(minute_angle))
    cv2.line(image, CENTER, (minute_x, minute_y), COLORS['amber'], 3)

    hour_x = int(CENTER[0] + (RADIUS - 100) * math.cos(hour_angle))
    hour_y = int(CENTER[1] + (RADIUS - 100) * math.sin(hour_angle))
    cv2.line(image, CENTER, (hour_x, hour_y), COLORS['amber'], 7)

    cv2.circle(image, CENTER, 5, COLORS['dark_gray'], -1)

    time = getDigitalTime(hour, minute, second)
    cv2.putText(image, time, (200, 390), cv2.FONT_HERSHEY_DUPLEX, 1.6, COLORS['red'], 1, cv2.LINE_AA)

    return image
