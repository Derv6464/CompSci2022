from datetime import datetime
from picamera import PiCamera
from time import sleep
import requests
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


camera = PiCamera()
filename = "{0:%Y}-{0:%m}-{0:%d},{0:%H}.{0:%M}.{0:%S}".format(datetime.now())
date = "{0:%Y}-{0:%m}-{0:%d}".format(datetime.now())
time = "{0:%H}.{0:%M}.{0:%S}".format(datetime.now())
baseUrl = ""

gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

def takePic():
    camera.start_preview()
    sleep(2)
    camera.capture('/home/pi/Documents/compSci2022/CompSci2022-main/pictures/'+filename+'.jpg')
    camera.stop_preview()
    
def dataToGlitch(time,date,driveID):
    myobj = {'field':time,'value':date}
    print(time,date)
    baseurl = 'https://compsci2022.glitch.me/addData'
    x = requests.post(baseurl,data = myobj)
    print(x.text)

def dataToDrive(filename):
    file = drive.CreateFile({'title': filename, 'mimeType':'image/jpg'})
    file.SetContentFile(files)
    file.Upload()
#     idk if this needed
    myObject = {"field": "name", "value": filename}
    x = requests.post(baseUrl, data = myObject)
    print(x.text)
    
def getDriveID():
    
#sending file name/time to database
# when motion detected

# must get drive id and send it with data to glitch