from datetime import datetime
from PyQt6 import QtGui

class ConsoleBox:
    console = None
    def __init__(self, console) -> None:
        ConsoleBox.console = console
        pass

    def afegirMissatge(missatge):
        ConsoleBox.console.append("<html><b>["+datetime.now().strftime("%d/%m/%Y %H:%M:%S")+"]</b</html>"+"  "+missatge)
        ConsoleBox.console.verticalScrollBar().setValue(ConsoleBox.console.verticalScrollBar().maximum())
