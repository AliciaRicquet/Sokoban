from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QMainWindow


class SokobanView1(QMainWindow):
    """
    TODO
    - LevelDesign et dessin
    - gerer les deplacement
    - dessin persos
    - mettre a jour la matrice
    PS: hesitez pas a ajouter des idéee
    - rajouter musique de fond
    - bruit de caisse qui bouge
    - bruit de caisse dans le trou
    - musique de victoire avec ecran de victoire
    fonctionnement matrice = 0 = case libre   1 = joueur,, 2 = mur, 3 = trou(objectif rien de personnel hein)
    """
    def __init__(self):
        super().__init__()
        self.SokobanController = None
        self.model = None


    def setController(self, controller):
        self.SokobanController = controller

    def setModel(self, model):
        self.model = model
        self.setFixedSize(len(self.model.getMatrix()[0]*30),len(self.model.getMatrix()*30))


    def paintEvent(self, event):
        print(self.model.getMatrix())
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
            print((1 ,0))

