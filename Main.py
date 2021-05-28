import sys

from SokobanController import SokobanController
from SokobanModel import SokobanModel
from SokobanView import SokobanView
from PyQt5.QtWidgets import QApplication

app = QApplication(sys.argv)
view = SokobanView()
model = SokobanModel()
controller = SokobanController()
view.show()
view.setModel(model)
view.setControler(controller)
controller.setModel(model)
controller.addView(view)
model.addView(view)

view.recupererTab(10)
view.setWindowTitle("Dessin")
sys.exit(app.exec_())
