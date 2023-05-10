from zeep import Client
from zeep.exceptions import Fault
from zeep.wsse.username import UsernameToken

from PySide6.QtCore import Qt, QObject, Slot

class OnvifPtzController(QObject):
    def __init__(self, url, username, password):
        QObject.__init__(self)
        self.url = url
        self.username = username
        self.password = password
        self.client = self.create_client()

    def create_client(self):
        # Crea un cliente ONVIF utilizando Zeep
        # y autentica con el usuario y contraseña especificados
        auth = UsernameToken(self.username, self.password)
        #return Client(self.url, wsse=auth)
        return 0

    @Slot()
    def move(self, pan_speed, tilt_speed, zoom_speed):
        # Envía un comando de movimiento de PTZ a la cámara ONVIF
        try:
            # Prepara los parámetros del comando de movimiento
            velocity = self.client.get_type('tt:PTZSpeed')()
            velocity.PanTilt = self.client.get_type('tt:Vector2D')(
                x=pan_speed, y=tilt_speed)
            velocity.Zoom = self.client.get_type('tt:Vector1D')(x=zoom_speed)
            # Envía el comando de movimiento a la cámara ONVIF
            self.client.ptz.Move(velocity)
        except Fault as f:
            print(f)

    def stop(self):
        # Envía un comando de detención de movimiento a la cámara ONVIF
        try:
            self.client.ptz.Stop()
        except Fault as f:
            print(f)

    def get_status(self):
        # Obtiene el estado actual de la cámara ONVIF
        try:
            # Obtiene la posición actual de la cámara
            status = self.client.ptz.GetStatus()
            position = status.Position
            return {'pan': position.PanTilt.x,
                    'tilt': position.PanTilt.y,
                    'zoom': position.Zoom.x}
        except Fault as f:
            print(f)