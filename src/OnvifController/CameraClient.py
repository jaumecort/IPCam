from onvif import ONVIFCamera
import string
from UI.SimpleLogin.SimpleLogin import *

class CameraClient:
    ip = ''
    username = ''
    password = ''

    isWebCam = False

    devicemgmt_service = None
    media_service = None

    device_information = None

    def __init__(self, ip, cred) -> None:
        if (ip=='0'):
            print('Webcam')
            self.isWebCam = True
            self.ip = 0
            return 

        self.username=cred[0]
        self.password=cred[1]
        print("Trying to connect with usr: "+self.username+" and pssw: "+self.password)
        try:
            self.mycam = ONVIFCamera(ip, 80, self.username, self.password, 'config/wsdl/')
            print('Conection Stablished')
            self.devicemgmt_service = self.mycam.devicemgmt
            self.media_service = self.mycam.create_media_service()
        except Exception as ex:
            print(ex)

        self.profiles = self.media_service.GetProfiles()
        #print(self.profiles)
    

    def getStreamUri(self):
        if(self.isWebCam): return 0
        request =  {
            'StreamSetup': {
                'Stream': 'RTP-Unicast',
                'Transport': {'Protocol': 'RTSP'}
                },
            'ProfileToken': self.profiles[0].token
        }
        response = self.media_service.GetStreamUri(request)
        uri = response.Uri.split("//")
        urilogin = f'{uri[0]}//{self.username}:{self.password}@{uri[1]}'
        return urilogin

    def canviarHora(self):
        time_params = self.mycam.devicemgmt.create_type('SetSystemDateAndTime')
        DateTime = dt.UTCDateTime
        DateTime.Date.Year = 2023
        DateTime.Date.Month = 5
        DateTime.Date.Day = 15
        DateTime.Time.Hour = 7
        DateTime.Time.Minute = 38
        DateTime.Time.Second = 30
        dt = self.mycam.devicemgmt.GetSystemDateAndTime()
        tz = dt.TimeZone
        time_params.DateTimeType = 'Manual'
        time_params.DaylightSavings = True
        time_params.TimeZone = tz
        time_params.UTCDateTime = DateTime
        self.mycam.devicemgmt.SetSystemDateAndTime(time_params)



if __name__=="__main__":
    cam = CameraClient("192.168.1.107")
    cam.getStreamUri()

 