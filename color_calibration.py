#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
 
#sensors
color_sensor_left = ColorSensor(Port.S1)
 
ev3 = EV3Brick()

ev3.speaker.beep()
while not any(ev3.buttons.pressed()):
    continue
wait(1000)
white_color = color_sensor_left.reflection()
ev3.screen.print("white color:", white_color)

ev3.speaker.beep()    
while not any(ev3.buttons.pressed()):
    continue
wait(1000)
black_color = color_sensor_left.reflection()
ev3.screen.print("black color:", black_color)

ev3.speaker.beep()
color_threshould = (white_color + black_color)/2
ev3.screen.print("threshould:", color_threshould)
while not any(ev3.buttons.pressed()):
    continue
#BLACK = 8
#WHITE = 66
#color_threshould = 37
 
 