from datetime import datetime



class ConsoleBox:
    def __init__(self, console) -> None:
        self.console = console
        pass

    def afegirMissatge(self, missatge):

        self.console.append("<html><b>["+datetime.now().strftime("%d/%m/%Y %H:%M:%S")+"]</b</html>"+"  "+missatge)