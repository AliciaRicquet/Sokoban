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
        # initialisation pour mvc
        self.__SokobanController = None
        self.__model = None
        # Declaration du widget et configuration
        self.__window = QWidget()
        self.setCentralWidget(self.__window)
        # Declaration du grid Layout
        self.__grid = QGridLayout()
        self.__labelGrid = []
        self.__window.setLayout(self.__grid)
        # configuration de la musique
        self.playlist = QMediaPlaylist()
        self.playlist.addMedia(QMediaContent(QUrl.fromLocalFile(
            QDir.current().relativeFilePath("../son/musique1.mp3"))))
        self.playlist.setPlaybackMode(QMediaPlaylist.Loop)
        self.levelSound = QMediaPlayer()
        self.levelSound.setPlaylist(self.playlist)
        # configuration et choix des textures
        selectionTexture = randint(1, 5)
        self.__joueur = QImage("./sprites/perso_bas.png", 'png').copy(0, 0, 50, 50)
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
        # Attribution du model
        self.__model = model
        # creation d' un label
        label = QLabel()
        # recupération de la matrice du model
        matrix = self.__model.getMatrix()
        # configuration de la taille de la fenêtre
        self.setFixedSize(len(matrix[0] * 100), len(matrix * 100))
        # w = self.width() / len(matrix)
        # h = self.height() / len(matrix[0])

        # attribution de la texture au joueur au mur et a la caisse
        joueur = QPixmap(self.__joueur)
        wall = QPixmap(self.__mur)
        for i in range(len(matrix)):
            tmp = []
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    self.__grid.addWidget(label, i, j)
                    tmp.append(label)
                elif matrix[i][j] == 1:
                    label.setPixmap(joueur)
                    self.__grid.addWidget(label, i, j)
                    tmp.append(label)
                elif matrix[i][j] == 2:
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
