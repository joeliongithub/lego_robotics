#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
 
# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

def gyro_turn(angle):
   gyro_init_angle = gyro_sensor.angle()
   ev3.screen.print("[gyro: ", gyro_sensor.angle(), "; ag:", angle)
   turn_angle = angle
   robot.turn(turn_angle)
   # ev3.screen.print("gyro: ", gyro_sensor.angle())
   while(gyro_sensor.angle() != (gyro_init_angle + turn_angle)) :
      diff = gyro_init_angle + turn_angle - gyro_sensor.angle()
      if(abs(diff)<=1):
          break
      robot.turn (diff)
   robot.stop()
   ev3.screen.print("]gyro: ", gyro_sensor.angle())
 
def gyro_straight(distance):
   robot.reset()
   ev3.screen.print("straight gyro: ", gyro_sensor.angle())
   SPEED = 180
   if(distance < 0) :
       speed = -SPEED
       sign = -1
   else:
       speed = SPEED
       sign = 1
   init_angle = gyro_sensor.angle()
   while abs(robot.distance()) <= abs(distance):
       correction = (init_angle - gyro_sensor.angle())*2
       robot.drive(speed, correction)
   robot.stop()
   left_motor.brake()
   right_motor.brake()
 
def line_follow(distance):
   speed = 50
   KP = 21
   if distance < 0:
       sign = -1
   else:
       sign = 1
 
   robot.reset()
   while abs(robot.distance()) <= abs(distance):
       correction = (color_sensor.reflection()-35) * KP
       robot.drive(sign*speed, correction)
   robot.stop()
 
#main
#BLACK = 1
#WHITE = 24
 
 
# motors
# motors variable
left_motor = Motor(Port.D, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
medium_motorC = Motor(Port.C, Direction.COUNTERCLOCKWISE,[12,24])
medium_motorB = Motor(Port.B, Direction.CLOCKWISE,[12,24])
#sensors
gyro_sensor = GyroSensor(Port.S3)
color_sensor_left = ColorSensor(Port.S1)
color_sensor_right = ColorSensor(Port.S4)
 
#initialization
 
robot = DriveBase(left_motor,right_motor,100,145)
robot.settings (370)
gyro_sensor.reset_angle(0)
cur_angle = 0
 
ev3 = EV3Brick()
ev3.speaker.beep()
 
# start from Home
gyro_straight(100)
gyro_turn(45)
cur_angle = cur_angle + 45
 
gyro_straight(350)
# line_follow(1000)
 
 
ev3.screen.print("line follow")
distance =300
speed = 50
KP = 3
robot.reset()
while abs(robot.distance()) <= abs(distance) :
   correction = (color_sensor_right.reflection()-35) * KP
   robot.drive(speed, correction)
robot.stop()
final_distance1 = robot.distance()
 
cur_angle = 90
 
ev3.screen.print("straight")
 
gyro_straight(250)
 
 
while color_sensor_left.reflection() > 10 :
   robot.drive(speed, correction)
robot.stop()
final_distance2 = robot.distance()
 
ev3.screen.print("final-d: ", final_distance1, ";", final_distance2)
ev3.screen.print("gyro angle: ", gyro_sensor.angle())
gyro_turn(-90)
gyro_straight(140)
while color_sensor_left.reflection() > 10 :
   robot.drive(speed, correction)
robot.stop()
 
gyro_straight(10)
gyro_turn(100)
 
ev3.screen.print("line follow")
distance = 10
speed = 50
KP = 3
robot.reset()
while abs(robot.distance()) <= abs(distance) :
    correction = (color_sensor_left.reflection()-35) * KP
    robot.drive(speed, correction)
robot.stop()
 
robot.reset()
 
medium_motorC.run_angle(1000, 260, Stop.HOLD, True)
robot.reset()
 
gyro_straight(95)
gyro_straight(-50)
medium_motorC.run_angle(1000, -260, Stop.HOLD, True)
 
