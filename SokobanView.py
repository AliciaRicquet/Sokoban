from random import randint

from PyQt5.QtCore import Qt, QUrl, QDir
from PyQt5.QtGui import QPixmap, QImage, QIcon
from PyQt5.QtMultimedia import QMediaPlaylist, QMediaContent, QMediaPlayer
from PyQt5.QtWidgets import QMainWindow, QGridLayout, QLabel, QWidget, QDesktopWidget
from PyQt5.Qt import Qt, QSound


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
        self.__controller = None
        self.__model = None
        # Declaration du widget et configuration
        self.__window = QWidget()
        self.setCentralWidget(self.__window)
        self.setWindowIcon(QIcon("sprites/mur3.png"))
        size_ecran = QDesktopWidget().screenGeometry()
        self.move((size_ecran.width() - self.geometry().width()) / 3,
                  (size_ecran.height() - self.geometry().height()) / 10)
        # Declaration du grid Layout
        self.__grid = QGridLayout()
        self.__grid.setSpacing(0)
        self.__labelGrid = []
        self.__window.setLayout(self.__grid)
        # configuration de la musique
        self.playlist = QMediaPlaylist()
        self.playlist.addMedia(QMediaContent(QUrl.fromLocalFile(
            QDir.current().absoluteFilePath("son/musique1.mp3"))
        ))
        self.playlist.setPlaybackMode(QMediaPlaylist.Loop)
        self.musiqueSound = QMediaPlayer()
        self.musiqueSound.setPlaylist(self.playlist)
        self.musiqueSound.play()
        # choix texture
        self.selectionTexture = randint(1, 5)
        self.__player = None
        self.__wall = None
        self.__caisse = None
        self.__hole = None
        self.__ground = None
        self.__grass = None

    def setController(self, controller):
        self.__controller = controller

    def setModel(self, model):
        # Attribution du model
        self.__model = model
        # recupération de la matrice du model
        matrix = self.__model.getMatrix()
        # configuration de la taille de la fenêtre
        self.setFixedSize(len(matrix[0] * 100), len(matrix * 100))
        self.creationLayout()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Up:
            self.__controller.movement((0, -1))
            print((0, -1))
        elif e.key() == Qt.Key_Down:
            self.__controller.movement((0, 1))
            print((0, 1))
        elif e.key() == Qt.Key_Right:
            self.__controller.movement((-1, 0))
            print((-1, 0))
        elif e.key() == Qt.Key_Left:
            self.__controller.movement((1, 0))
            print((1, 0))
        else:
            return

    # fonction pour attribuer les textures
    def attribuerTexture(self):
        matrix = self.__model.getMatrix()

        # configuration et choix des textures
        # images statiques
        imageJoueur = QImage("./sprites/perso_bas.png", 'png')
        imageTrou = QImage("./sprites/hole.png")
        imageSol = QImage("sprites/ground_interior.png")
        imageGrass = QImage("sprites/grass.png")
        # image aléatoire
        if self.selectionTexture == 1:
            imageCaisse = QImage("./sprites/caisse_valide1.png", 'png')
            imageMur = QImage("./sprites/mur1.png", 'png')

        elif self.selectionTexture == 2:
            imageCaisse = QImage("./sprites/caisse_valide2.png", 'png')
            imageMur = QImage("./sprites/mur2.png", 'png')

        elif self.selectionTexture == 3:
            imageCaisse = QImage("./sprites/caisse_valide3.png", 'png')
            imageMur = QImage("./sprites/mur3.png", 'png')
        elif self.selectionTexture == 4:
            imageCaisse = QImage("./sprites/caisse_valide4.png", 'png')
            imageMur = QImage("./sprites/mur4.png", 'png')

        elif self.selectionTexture == 5:
            imageCaisse = QImage("./sprites/caisse_valide5.png", 'png')
            imageMur = QImage("./sprites/mur5.png", 'png')

        # attribution de la texture au joueur au mur et a la caisse
        # taille des textures
        w = self.width() / len(matrix)
        h = self.height() / len(matrix[0])
        # attribution des pixmap
        self.__player = QPixmap(imageJoueur.scaled(w, h))
        self.__wall = QPixmap(imageMur.scaled(w, h))
        self.__caisse = QPixmap(imageCaisse.scaled(w, h))
        self.__hole = QPixmap(imageTrou.scaled(w, h))
        self.__ground = QPixmap(imageSol.scaled(w, h))
        self.__grass = QPixmap(imageGrass.scaled(w, h))

    def creationLayout(self):
        matrix = self.__model.getMatrix()
        self.attribuerTexture()
        # ajout des textures au jeu
        for i in range(len(matrix)):
            tmp = []
            for j in range(len(matrix[i])):
                label = QLabel()
                if matrix[i][j] == 0:
                    label.setPixmap(self.__ground)
                    self.__grid.addWidget(label, i, j)
                    tmp.append(label)

                elif matrix[i][j] == 1:
                    print(matrix[i][j])
                    label.setPixmap(self.__player)
                    self.__grid.addWidget(label, i, j)
                    tmp.append(label)

                elif matrix[i][j] == 2:
                    label.setPixmap(self.__wall)
                    self.__grid.addWidget(label, i, j)
                    tmp.append(label)

                elif matrix[i][j] == 3:
                    label.setPixmap(self.__hole)
                    self.__grid.addWidget(label, i, j)
                    tmp.append(label)

                elif matrix[i][j] == 4:
                    label.setPixmap(self.__caisse)
                    self.__grid.addWidget(label, i, j)
                    tmp.append(label)

                elif matrix[i][j] == 5:
                    label.setPixmap(self.__grass)
                    self.__grid.addWidget(label, i, j)
                    tmp.append(label)
            self.__labelGrid.append(tmp)
        self.afficherJoueur(self.__labelGrid)

    def afficherJoueur(self,matrix):
        posJoueur = self.__model.getCoordonneePerso()
        matrix[posJoueur[0]][posJoueur[1]].setPixmap(self.__player)
