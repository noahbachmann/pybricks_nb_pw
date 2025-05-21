#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, UltrasonicSensor
from pybricks.parameters import Port, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait

from math import pi


# ------------------------------------------------------------------------

ev3 = EV3Brick()  

medium_motor = Motor(Port.A)
left_motor   = Motor(Port.B)            
right_motor  = Motor(Port.C)

left_motor.reset_angle(0)
right_motor.reset_angle(0)


# ------------------------------------------------------------------------

medium_motor.run_target(
    speed = 800,
    target_angle = 90,
    then = Stop.HOLD,
    wait = True
)

