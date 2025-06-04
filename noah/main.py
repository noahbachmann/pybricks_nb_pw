#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.parameters import Button, Color
from pybricks.hubs import EV3Brick
from pybricks.tools import wait
from pybricks.ev3devices import Motor, UltrasonicSensor, ColorSensor
from pybricks.parameters import Port, Stop
from pybricks.robotics import DriveBase
from math import pi

# ------------------------------------------------------------------------
# Initialisierung
# ------------------------------------------------------------------------
ev3 = EV3Brick()

middle_motor = Motor(Port.A)         
left_motor   = Motor(Port.B)              
right_motor  = Motor(Port.C)               
infrared = UltrasonicSensor(Port.S3)
color = ColorSensor(Port.S4)

# screenWidth = 178
# screenHeight = 128

wheel_diameter = 56  # Durchmesser der Räder in mm (EV3 Standard: ~56mm)
axle_track = 114     # Spurbreite zwischen den Rädern in mm (z.B. 114mm)
drive_base = DriveBase(left_motor, right_motor,
                       wheel_diameter, axle_track)

if __name__ == "__main__":
    distance = 0
    middle_motor.run(100)
    while(infrared.distance(True) > 120):
        drive_base.straight(100)
        distance += 100
        if color.color() == Color.BROWN:
            break
        elif color.color() == Color.BLACK:
            ev3.screen.load_image("black_image.jpg")
            ev3.speaker.play_file("black_sound.wav")
        elif color.color() == Color.GREEN:
            ev3.screen.load_image("green_image.png")
            ev3.speaker.play_file("green_sound.wav")
        elif color.color() == Color.RED:
            ev3.light.on(Color.RED)
            ev3.screen.load_image("red_image.png")
            drive_base.drive(0, 500)
            middle_motor.run(250)
            wait(3000)
            drive_base.stop()
            drive_base.drive(0, -500)
            wait(3000)
            drive_base.stop()
            middle_motor.run(100)
            ev3.light.off()
        elif color.color() == Color.WHITE:
            ev3.screen.load_image("white_image.jpg")
            ev3.speaker.play_file("white_sound.wav")
        elif color.color() == Color.BLUE:
            ev3.screen.load_image("blue_image.jpg")
            ev3.speaker.play_file("blue_sound.wav")
        elif color.color() == Color.YELLOW:
            ev3.screen.load_image("yellow_image.jpg")
            ev3.speaker.play_file("yellow_sound.wav")
        else:
            pass

        wait(2000)
    
    ev3.screen.load_image("end.jpg")
    middle_motor.stop(Stop.HOLD)
    drive_base.turn(180)    
    drive_base.straight(distance)
    drive_base.turn(180)
    ev3.speaker.play_file("end-sound.wav")