from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QMainWindow


class SokobanView1(QMainWindow):
    def __init__(self):
        super().__init__()
        self.SokobanController = None
        self.model = None

    def setController(self, controller):
        self.SokobanController = controller

    def setModel(self, model):
        self.model = model

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawRect(self.model.getCoordonneePerso()[0],self.model.getCoordonneePerso()[1],30,30)

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Up:
            self.SokobanController.changeDirection((0,-1))
            print((0,-1))
        elif e.key() == Qt.Key_Down:
            self.SokobanController.changeDirection((0, 1))
            print((0,1))
        elif e.key() == Qt.Key_Right:
            self.SokobanController.changeDirection((-1, 0))
            print((-1,0))
        elif e.key() == Qt.Key_Left:
            self.SokobanController.changeDirection((1, 0))
            print((1,0))

