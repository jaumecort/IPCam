from datetime import datetime
from PyQt6 import QtGui

class ConsoleBox:
    def __init__(self, console) -> None:
        self.console = console
        pass

    def afegirMissatge(self, missatge):
        self.console.append("<html><b>["+datetime.now().strftime("%d/%m/%Y %H:%M:%S")+"]</b</html>"+"  "+missatge)
        self.console.verticalScrollBar().setValue(self.console.verticalScrollBar().maximum())