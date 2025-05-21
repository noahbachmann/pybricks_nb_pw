#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.parameters import Button, Color
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, UltrasonicSensor
from pybricks.parameters import Port, Stop
from pybricks.robotics import DriveBase
from math import pi

# ------------------------------------------------------------------------
# Initialisierung
# ------------------------------------------------------------------------
ev3 = EV3Brick()                      # Display, Speaker, LED (optional)

medium_motor = Motor(Port.A)               # Mittlerer Motor an Port A
left_motor   = Motor(Port.B)               # Linker Grosser Motor an Port B
right_motor  = Motor(Port.C)               # Rechter Grosser Motor an Port C
infrared = UltrasonicSensor(Port.S3)

# Winkelzähler auf 0 setzen

# ------------------------------------------------------------------------
# 1. Medium-Motor 90° vor und zurück
# ------------------------------------------------------------------------

# medium_motor.run_target(
#     speed=500,               # °/s
#     target_angle=90,         # Zielwinkel
#     then=Stop.HOLD,          # Halten, damit er nicht nachfedert
#     wait=True
# )

# medium_motor.run_target(
#     speed=500,
#     target_angle=0,          # Zurück zur Startposition
#     then=Stop.COAST,
#     wait=True
# )

# ------------------------------------------------------------------------
# 2. DriveBase einrichten und fahren
# ------------------------------------------------------------------------

# Erwartung: 500 mm / (π·56 mm) ≈ 2.84 Umdrehungen → ≈ 1020 °
# ev3.screen.print("Links:  {:.0f}°".format(angle_left))
# ev3.screen.print("Rechts: {:.0f}°".format(angle_right))

# ------------------------------------------------------------------------
# 3. In-Place-Drehung um 90°
# ------------------------------------------------------------------------

wheel_diameter = 56  # Durchmesser der Räder in mm (EV3 Standard: ~56mm)
axle_track = 114     # Spurbreite zwischen den Rädern in mm (z.B. 114mm)
drive_base = DriveBase(left_motor, right_motor,
                       wheel_diameter, axle_track)

# Roboter geradeaus fahren lassen
                  # 500 mm vorwärts (50 cm)
# Winkelstände der Motoren abfragen (beide sollten ~360° = eine Umdrehung haben bei 56mm Rädern)

if __name__ == "__main__":
    while(infrared.distance(True) > 100):
        drive_base.straight(50)

    ev3.screen.print("There is an object in front of me.")