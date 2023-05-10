# This Python file uses the following encoding: utf-8
import sys
from pathlib import Path
from PySide6.QtCore import Qt, QObject, Slot
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine

import onvif.OnvifPtzController as ptz
import onvif.ejem as onvif

def moveCameraUp():
    controller.moveUp()

class ejemp(QObject):
    def __init__(self):
        QObject.__init__(self)
    @Slot()
    def saludar(self):
        print('ola')



if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    ej = onvif.ejemp()
    controller = ptz.OnvifPtzController(url='http://192.168.1.10/onvif/ptz_service', username='admin', password='password')
    engine.rootContext().setContextProperty('onvif_controller', controller)
    engine.rootContext().setContextProperty('ej', ej)
    qml_file = Path(__file__).resolve().parent / "qml/main.qml"
    engine.load(qml_file)
    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec())
