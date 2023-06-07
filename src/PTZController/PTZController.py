import asyncio, sys
from onvif import ONVIFCamera
import time

class PTZController:

    mycam = None

    XMAX = 1
    XMIN = -1
    YMAX = 1
    YMIN = -1
    moverequest = None
    ptz = None
    active = False

    def __init__(self, ipcam):
        self.mycam = ipcam

        # Create media service object
        media = self.mycam.create_media_service()
        # Create self.ptz service object
        self.ptz = self.mycam.create_ptz_service()

        # Get target profile
        media_profile = media.GetProfiles()[0]

        # Get self.ptz configuration options for getting continuous move range
        request = self.ptz.create_type('GetConfigurationOptions')
        request.ConfigurationToken = media_profile.PTZConfiguration.token
        ptz_configuration_options = self.ptz.GetConfigurationOptions(request)

        self.moverequest = self.ptz.create_type('ContinuousMove')
        self.moverequest.ProfileToken = media_profile.token
        if self.moverequest.Velocity is None:
            self.moverequest.Velocity = self.ptz.GetStatus({'ProfileToken': media_profile.token}).Position

        # Get range of pan and tilt
        # NOTE: X and Y are velocity vector
        self.XMAX = ptz_configuration_options.Spaces.ContinuousPanTiltVelocitySpace[0].XRange.Max
        self.XMIN = ptz_configuration_options.Spaces.ContinuousPanTiltVelocitySpace[0].XRange.Min
        self.YMAX = ptz_configuration_options.Spaces.ContinuousPanTiltVelocitySpace[0].YRange.Max
        self.YMIN = ptz_configuration_options.Spaces.ContinuousPanTiltVelocitySpace[0].YRange.Min

    def do_move(self, request):
        # Start continuous move
        if self.active:
            self.ptz.Stop({'ProfileToken': request.ProfileToken})
        self.active = True
        self.ptz.ContinuousMove(request)

    def move_up(self):
        print ('move up...')
        request = self.moverequest
        request.Velocity.PanTilt.x = 0
        request.Velocity.PanTilt.y = self.YMAX
        self.do_move(request)

    def move_down(self):
        print ('move down...')
        request = self.moverequest
        request.Velocity.PanTilt.x = 0
        request.Velocity.PanTilt.y = self.YMIN
        self.do_move(request)

    def move_right(self):
        print ('move right...')
        request = self.moverequest
        request.Velocity.PanTilt.x = self.XMAX
        request.Velocity.PanTilt.y = 0
        self.do_move(request)

    def move_left(self):
        print ('move left...')
        request = self.moverequest
        request.Velocity.PanTilt.x = self.XMIN
        request.Velocity.PanTilt.y = 0
        self.do_move(request)

    def move_upleft(self):
        print ('move up left...')
        request = self.moverequest
        request.Velocity.PanTilt.x = self.XMIN
        request.Velocity.PanTilt.y = self.YMAX
        self.do_move(request)
        
    def move_upright(self):
        print ('move up left...')
        request = self.moverequest
        request.Velocity.PanTilt.x = self.XMAX
        request.Velocity.PanTilt.y = self.YMAX
        self.do_move(request)
        
    def move_downleft(self):
        print ('move down left...')
        request = self.moverequest
        request.Velocity.PanTilt.x = self.XMIN
        request.Velocity.PanTilt.y = self.YMIN
        self.do_move(request)
        
    def move_downright(self):
        print ('move down left...')
        request = self.moverequest
        request.Velocity.PanTilt.x = self.XMAX
        request.Velocity.PanTilt.y = self.YMIN
        self.do_move(request)


        
                
if __name__ == '__main__':
    mycam = ONVIFCamera('192.168.88.253', 80, 'admin', 'L2F63400', 'etc/onvif/wsdl/')
    ptz = ptzController(mycam)
    while True:
        ptz.move_left()
        time.sleep(0.5)
        ptz.move_right()
        time.sleep(0.5)
        