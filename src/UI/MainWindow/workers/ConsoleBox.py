class ConsoleBox:
    def __init__(self, console) -> None:
        self.console = console
        pass

    def afegirMissatge(self, missatge):
        self.console.append(missatge)