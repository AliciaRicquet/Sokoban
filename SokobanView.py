from PyQt5.QtWidgets import QMainWindow


class SokobanView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.controller = None
        self.model = None

    def setController(self,controller):
        self.controller = controller

    def setModel(self,model):
        self.model = model


