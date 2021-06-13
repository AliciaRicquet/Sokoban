from random import randint

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPixmap
from PyQt5.QtWidgets import QMainWindow,QGridLayout
from SokobanModel import *

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
        joueur = QImage("./sprites/perso_bas.png", 'png').copy(370, 0, 400, 350)
        if randint(1,5) == 1 :
            caisse_valide = QImage("./sprites/caisse_valide1.png", 'png').copy(30, 0, 400, 350)
        elif randint(1,5) == 2 :
            caisse_valide2= QImage("./sprites/caisse_valide2.png", 'png').copy(30, 0, 400, 350)
        elif randint(1,5) == 3 :
            caisse_valide3= QImage("./sprites/caisse_valide3.png", 'png').copy(30, 0, 400, 350)
        elif randint(1,5) == 4 :
            caisse_valide4= QImage("./sprites/caisse_valide4.png", 'png').copy(30, 0, 400, 350)
        elif randint(1,5) == 5 :
            caisse_valide5= QImage("./sprites/caisse_valide5.png", 'png').copy(30, 0, 400, 350)

            mur= QImage("./sprites/mur1.png", 'png').copy(30, 0, 400, 350)
            mur2= QImage("./sprites/mur2.png", 'png').copy(30, 0, 400, 350)
            mur3= QImage("./sprites/mur3.png", 'png').copy(30, 0, 400, 350)
            mur4= QImage("./sprites/mur4.png", 'png').copy(30, 0, 400, 350)

        self.__cross = QIcon(QPixmap.fromImage(crossImage).scaled(w, h))
        self.__round = QIcon(QPixmap.fromImage(roundImage).scaled(w, h))

    def setController(self, controller):
        self.SokobanController = controller

    def setModel(self, model):
        self.model = model
        self.setFixedSize(len(self.model.getMatrix()[0] * 30), len(self.model.getMatrix() * 30))
        self.gridLayout= QGridLayout()
        for i in range (len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] == 0:
                    button.setStyleSheet(
                        "background-color:rgb(127,127,127)")
                elif self.matrix[i][j] == 1 :
                    QPixmap joueur("/photo.png");




    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Up:
            self.SokobanController.changeDirection((0, -1))
            print((0, -1))
        elif e.key() == Qt.Key_Down:
            self.SokobanController.changeDirection((0, 1))
            print((0, 1))
        elif e.key() == Qt.Key_Right:
            self.SokobanController.changeDirection((-1, 0))
            print((-1, 0))
        elif e.key() == Qt.Key_Left:
            self.SokobanController.changeDirection((1, 0))
            print((1, 0))
