import sys

from SokobanController import SokobanController
from SokobanModel import SokobanModel
from SokobanView import SokobanView1
from PyQt5.QtWidgets import QApplication

app = QApplication(sys.argv)
view = SokobanView1()
model = SokobanModel(10,10)
controller = SokobanController()
view.show()
view.setModel(model)
view.setController(controller)
controller.setModel(model)
controller.addView(view)
model.addView(view)

view.setWindowTitle("Sokoban Empire des A2")
sys.exit(app.exec_())
