import sys

from SokobanController import SokobanController
from SokobanModel import SokobanModel
from SokobanView import SokobanView
from PyQt5.QtWidgets import QApplication

app = QApplication(sys.argv)
view = SokobanView()
model = SokobanModel(2)
controller = SokobanController()
view.show()
view.setModel(model)
view.setController(controller)
controller.setModel(model)
controller.setView(view)

view.setWindowTitle("Sokoban Empire des A2")
sys.exit(app.exec_())
