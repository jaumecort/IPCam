from onvif import ONVIFCamera
import string

class CameraClient:
    def __init__(self, ip) -> None:
        self.mycam = ONVIFCamera(ip, 80, 'admin', 'L2F63400', 'etc/onvif/wsdl/')

        # Get Hostname
        resp = self.mycam.devicemgmt.GetHostname()
        print("My camera`s hostname: " + str(resp.Name))

        self.media_service = self.mycam.create_media_service()
        self.profiles = self.media_service.GetProfiles()
        #print(self.profiles)

        pass
    

    def getStreamUri(self):
        request =  {
            'StreamSetup': {
                'Stream': 'RTP-Unicast',
                'Transport': {'Protocol': 'RTSP'}
                },
            'ProfileToken': self.profiles[0].token
        }
        response = self.media_service.GetStreamUri(request)
        print(response)
        return response.Uri

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

 