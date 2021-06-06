from PyQt5.QtCore import QTimer


# 0 = case libre   1 = joueur,, 2 = mur, 3 = trou(objectif rien de personnel hein), 4 caisse
class SokobanModel:
    def __init__(self, level):
        assert level == 1 or level == 2

        self.views = []
        self.timer = QTimer()
        self.timer.timeout.connect(self.timeEvent)

        self.vitesseDeplacement = 10
        self.caisses = []
        self.direction = (0, 1)
        self.level = level
        if self.level == 1:
            self.matrix = [
                [0, 0, 2, 2, 2, 0, 0, 0],
                [0, 0, 2, 3, 2, 0, 0, 0],
                [0, 0, 2, 4, 2, 2, 2, 2],
                [2, 2, 2, 0, 1, 4, 3, 2],
                [2, 3, 0, 4, 4, 2, 2, 2],
                [2, 2, 2, 2, 0, 2, 0, 0],
                [0, 0, 0, 2, 3, 2, 0, 0],
                [0, 0, 0, 2, 2, 2, 0, 0]
            ]
            self.coordoneePerso = (3, 4)

    def getCoordonneePerso(self):
        return self.coordoneePerso

    def addView(self, views):
        self.views.append(views)

    def timeEvent(self, numberOfView):
        self.views[numberOfView].update()

    def getVitesseDeplacement(self):
        return self.vitesseDeplacement

    def addCaisse(self, coordonee):
        self.caisses.append(coordonee)

    '''def moveUpCaisse(self, numCaisse):
        self.caisses[numCaisse] = (self.caisses[numCaisse][0], self.caisses[numCaisse][1] - self.vitesseDeplacement)

    def moveDownCaisse(self, numCaisse):
        self.caisses[numCaisse] = (self.caisses[numCaisse][0], self.caisses[numCaisse][1] + self.vitesseDeplacement)

    def moveRightCaisse(self, numCaisse):
        self.caisses[numCaisse] = (self.caisses[numCaisse][0] + self.vitesseDeplacement, self.caisses[numCaisse][1])

    def moveLeftCaisse(self, numCaisse):
        self.caisses[numCaisse] = (self.caisses[numCaisse][0] - self.vitesseDeplacement, self.caisses[numCaisse][1])
    '''

    def getLevel(self):
        return self.level

    def setLevel(self, number):
        self.level = number

    def getMatrix(self):
        return self.matrix
