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


# Create your objects here.
ev3 = EV3Brick()
motor_b = Motor(Port.B)
motor_c = Motor(Port.C)
motor_a = Motor(Port.A)
# Write your program here.
color_sensor = ColorSensor(Port.S3)
colorSeen = color_sensor.color()
us = UltrasonicSensor(Port.S2)
ts = TouchSensor(Port.S1)



# Write your program here.
ev3.speaker.beep()


def claw_open():
    start_angle = motor_a.angle() 
    print(motor_a.angle())
    motor_a.run_until_stalled(50, duty_limit=70)
    print(motor_a.angle())
    if (motor_a.angle() - start_angle > 100):
        motor_a.run_angle(100, -90)
        ev3.speaker.beep()
    else:
        motor_a.run_angle(100, -90)
    
def claw_close():
    start_angle = motor_a.angle() 
    motor_a.run_until_stalled(50, duty_limit=70)
    motor_a.run_time(500, 200)

def cookie_monster():
    motor_b.run_until_stalled(-200, Stop.HOLD, duty_limit=50)
    claw_open()
    ev3.speaker.say("Do you want this cookie?")
    claw_open()
    motor_b.run_until_stalled(200, Stop.HOLD, duty_limit=50)
    claw_close()
    motor_b.run_until_stalled(-200, Stop.HOLD, duty_limit=50)
    motor_c.run_target(500, -300, wait=True)
    ev3.speaker.say("MY cookie now")

def cookie_st():
    motor_b.run_until_stalled(-200, Stop.HOLD, duty_limit=50)
    claw_open()
    ev3.speaker.say("Do you want this cookie?")
    ev3.speaker.say("Press my button")
    touch_not_found = True
    while touch_not_found:
        if(ts.pressed()== True):
            touch_not_found = False
            motor_b.run_until_stalled(200, Stop.HOLD, duty_limit=50)
            claw_close()
            motor_b.run_until_stalled(-200, Stop.HOLD, duty_limit=50)
            ev3.speaker.say("Here you go")

cookie_st()