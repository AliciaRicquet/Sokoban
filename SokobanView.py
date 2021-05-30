from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QMainWindow


class SokobanView1(QMainWindow):
    def __init__(self):
        super().__init__()
        self.controller = None
        self.model = None

    def setController(self, controller):
        self.controller = controller

    def setModel(self, model):
        self.model = model

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawRect(self.model.getCoordonneePerso()[0],self.model.getCoordonneePerso()[1],30,30)

class SokobanView2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.controller = None
        self.model = None

    def setController(self, controller):
        self.controller = controller

    def setModel(self, model):
        self.model = model


