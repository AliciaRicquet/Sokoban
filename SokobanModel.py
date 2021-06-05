from PyQt5.QtCore import QTimer


class SokobanModel:
    def __init__(self, h, w):
        self.views = []
        self.timer = QTimer()
        self.timer.timeout.connect(self.timeEvent)
        self.coordoneePerso = (0, 0)
        self.vitesseDeplacement = 10
        self.caisses = []
        self.direction = (0, 1)
        self.matrix = [[[0] for i in range(h)] for j in range(w)]
        self.level = 0

    def setCoordoneePerso(self, x, y):
        self.coordoneePerso = (x, y)

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

    def setLevel(self,number):
        self.level = number

    def getMatrix(self):
        return self.matrix

