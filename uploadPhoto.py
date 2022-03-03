from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from requests import post
from time import sleep, ctime

time = ctime()
print(time)

baseUrl = ""

gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

file_list=['/home/pi/Documents/compSci2022/CompSci2022-main/pictures/2022-01-20.jpg']
for files in file_list:
    file = drive.CreateFile({'title': time, 'mimeType':'image/jpg'})
    file.SetContentFile(files)
    file.Upload()
    myObject = {"field": "name", "value": time}
    x = requests.post(baseUrl, data = myObject)
    print(x.text)