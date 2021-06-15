from random import randint

from PyQt5.QtCore import Qt, QUrl, QDir
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtMultimedia import QMediaPlaylist, QMediaContent, QMediaPlayer
from PyQt5.QtWidgets import QMainWindow, QGridLayout, QLabel, QWidget


class SokobanView(QMainWindow):
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
        self.__SokobanController = None
        self.__model = None
        self.__window = QWidget()
        self.setCentralWidget(self.__window)
        self.__joueur = QImage("./sprites/perso_bas.png", 'png').copy(0, 0, 50, 50)
        selectionTexture = randint(1, 5)
        self.__grid = QGridLayout()
        self.__labelGrid = []
        self.__window.setLayout(self.__grid)
        self.__matrix = None
        self.playlist = QMediaPlaylist()
        self.playlist.addMedia(QMediaContent(QUrl.fromLocalFile(
            QDir.current().relativeFilePath("../son/musique1.mp3"))))
        self.playlist.setPlaybackMode(QMediaPlaylist.Loop)
        self.levelSound = QMediaPlayer()
        self.levelSound.setPlaylist(self.playlist)

        if selectionTexture == 1:
            self.__caisse_valide = QImage("./sprites/caisse_valide1.png", 'png').copy(30, 0, 0, 350)
            self.__mur = QImage("./sprites/mur1.png", 'png').copy(30, 0, 400, 350)

        elif selectionTexture == 2:
            self.__caisse_valide = QImage("./sprites/caisse_valide2.png", 'png')
            self.__mur = QImage("./sprites/mur2.png", 'png').copy(30, 0, 400, 350)

        elif selectionTexture == 3:
            self.__caisse_valide = QImage("./sprites/caisse_valide3.png", 'png').copy(30, 0, 400, 350)
            self.__mur = QImage("./sprites/mur3.png", 'png').copy(30, 0, 400, 350)
        elif selectionTexture == 4:
            self.__caisse_valide = QImage("./sprites/caisse_valide4.png", 'png').copy(30, 0, 400, 350)
            self.__mur = QImage("./sprites/mur4.png", 'png').copy(30, 0, 400, 350)

        elif selectionTexture == 5:
            self.__caisse_valide = QImage("./sprites/caisse_valide5.png", 'png').copy(30, 0, 400, 350)
            self.__mur = QImage("./sprites/mur5.png", 'png').copy(30, 0, 400, 350)

    def setController(self, controller):
        self.__SokobanController = controller

    def setModel(self, model):
        self.__model = model
        label = QLabel()

        self.__matrix = self.__model.getMatrix()
        self.setFixedSize(len(self.__matrix[0] * 100), len(self.__matrix * 100))
        w = self.width() / len(self.__matrix)
        h = self.height() / len(self.__matrix[0])
        joueur = QPixmap(self.__joueur)
        wall = QPixmap(self.__mur)
        for i in range(len(self.__matrix)):
            tmp = []
            for j in range(len(self.__matrix[i])):
                if self.__matrix[i][j] == 0:
                    self.__grid.addWidget(label, i, j)
                    tmp.append(label)
                elif self.__matrix[i][j] == 1:
                    label.setPixmap(joueur)
                    self.__grid.addWidget(label, i, j)
                    tmp.append(label)
                elif self.__matrix[i][j] == 2:
                    label.setPixmap(wall)
                    self.__grid.addWidget(label, i, j)
                    tmp.append(label)
            self.__labelGrid.append(tmp)

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Up:
            self.__SokobanController.changeDirection((0, -1))
            print((0, -1))
        elif e.key() == Qt.Key_Down:
            self.__SokobanController.changeDirection((0, 1))
            print((0, 1))
        elif e.key() == Qt.Key_Right:
            self.__SokobanController.changeDirection((-1, 0))
            print((-1, 0))
        elif e.key() == Qt.Key_Left:
            self.__SokobanController.changeDirection((1, 0))
            print((1, 0))
