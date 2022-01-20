from datetime import datetime
from picamera import PiCamera
from time import sleep
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

camera = PiCamera()
filename = "{0:%Y}-{0:%m}-{0:%d},{0:%H}.{0:%M}.{0:%S}".format(datetime.now())


camera.start_preview()
sleep(2)
camera.capture('/home/pi/Documents/compSci2022/CompSci2022-main/pictures/'+filename+'.jpg')
camera.stop_preview()