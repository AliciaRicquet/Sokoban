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
view.setController(controller)
controller.setModel(model)
controller.addView(view)
model.addView(view)

view.setWindowTitle("Dessin")
sys.exit(app.exec_())
