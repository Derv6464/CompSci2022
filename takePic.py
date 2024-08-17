from gpiozero import MotionSensor

from time import sleep


pir = MotionSensor(4)
i = 0
while True:
    pir.wait_for_motion()
    i=i+1
    print("You moved"+str(i))
    pir.wait_for_no_motion()