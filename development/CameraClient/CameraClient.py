from onvif import ONVIFCamera
from OnvifDiscovery import OnvifDiscovery
import string



def canviarHora():
    time_params = mycam.devicemgmt.create_type('SetSystemDateAndTime')

    DateTime = dt.UTCDateTime
    DateTime.Date.Year = 2023
    DateTime.Date.Month = 5
    DateTime.Date.Day = 15
    DateTime.Time.Hour = 7
    DateTime.Time.Minute = 38
    DateTime.Time.Second = 30

    dt = mycam.devicemgmt.GetSystemDateAndTime()
    tz = dt.TimeZone

    time_params.DateTimeType = 'Manual'
    time_params.DaylightSavings = True
    time_params.TimeZone = tz
    time_params.UTCDateTime = DateTime
    
    mycam.devicemgmt.SetSystemDateAndTime(time_params)


if __name__=="__main__":
   
    mycam = ONVIFCamera('192.168.88.253', 80, 'admin', 'L2F63400', 'etc/onvif/wsdl/')

    # Get Hostname
    resp = mycam.devicemgmt.GetHostname()
    print("My camera`s hostname: " + str(resp.Name))

    # Create ptz service
    ptz_service = mycam.create_ptz_service()
    media_service = mycam.create_media_service()

    confs = ptz_service.GetConfigurations()
    profiles = media_service.GetProfiles()

    move = ptz_service.create_type('ContinuousMove')
    move.ProfileToken = profiles[0].token
    move.Velocity = {

    }
    print(move)

    
    response = mycam.ptz.AbsoluteMove(profiles[0].token)
    #print(response)


   
 