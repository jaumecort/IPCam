# This Python file uses the following encoding: utf-8
from PyQt6.QtWidgets import *

from onvif import ONVIFCamera
from development.PTZController.PTZController import PTZController




if __name__ == "__main__":
    mycam = ONVIFCamera('192.168.88.253', 80, 'admin', 'L2F63400', 'etc/onvif/wsdl/')
    ptz = PTZController(mycam)

    app = QApplication([])
    window = QWidget()
    

    buttonDreta = QPushButton('Girar dreta')
    buttonEsquerra = QPushButton('Girar esquerra')

    buttonDreta.clicked.connect(ptz.move_right)
    buttonEsquerra.clicked.connect(ptz.move_left)

    layout = QVBoxLayout()
    layout.addWidget(buttonEsquerra)
    layout.addWidget(buttonDreta)
    window.setLayout(layout)

    window.show()
    app.exec()
