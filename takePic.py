from gpiozero import MotionSensor
from picamera import PiCamera
from time import sleep

camera = PiCamera()
pir = MotionSensor(4)

while True:
    pir.wait_for_motion()
    print("You moved")
    pir.wait_for_no_motion()