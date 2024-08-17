from datetime import datetime
from picamera import PiCamera
from time import sleep
import requests
# from pydrive.auth import GoogleAuth
# from pydrive.drive import GoogleDrive

# camera = PiCamera()
filename = "{0:%Y}-{0:%m}-{0:%d},{0:%H}.{0:%M}.{0:%S}".format(datetime.now())
date = "{0:%Y}-{0:%m}-{0:%d}".format(datetime.now())
time = "{0:%H}.{0:%M}.{0:%S}".format(datetime.now())
# print('test')
# camera.start_preview()
# print('test')
# sleep(2)
# print('test')
# camera.capture('/home/pi/Documents/compSci2022/CompSci2022-main/pictures/'+filename+'.jpg')
# camera.stop_preview()

#sending file name/time to database
# when motion detected
myobj = {'field':time,'value':date}
print(time,date)
baseurl = 'https://compsci2022.glitch.me/addData'
x = requests.post(baseurl,data = myobj)
print(x.text)
