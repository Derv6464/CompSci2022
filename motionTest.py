import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.IN)     #Define pin 3 as an output pin
i=0
while True:
      if GPIO.input(11)==1:
          i=i+1
          print("motion"+str(i))
      else:
          print("still")
      time.sleep(2)