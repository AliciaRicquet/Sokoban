from PyQt5.QtCore import QTimer


class SokobanModel:
    def __init__(self):
        self.views = []
        self.timer = QTimer()
        self.timer.timeout.connect(self.timeEvent)
        self.coordoneePerso = (0, 0)
        self.vitesseDeplacement = 10
        self.caisses = []

    def setCoordoneePerso(self, x, y):
        self.coordoneePerso = (x, y)

    def getCoordonneePerso(self):
        return self.coordoneePerso
    def addView(self, views):
        self.views.append(views)

    def timeEvent(self, numberOfView):
        self.views[numberOfView].update()

    def upMovement(self):
        self.setCoordoneePerso(self.coordoneePerso[0], self.coordoneePerso[1] - self.vitesseDeplacement)

    def downMovement(self):
        self.setCoordoneePerso(self.coordoneePerso[0], self.coordoneePerso[1] + self.vitesseDeplacement)

    def rightMovement(self):
        self.setCoordoneePerso(self.coordoneePerso[0] + self.vitesseDeplacement, self.coordoneePerso[1])

    def leftMovement(self):
        self.setCoordoneePerso(self.coordoneePerso[0] - self.vitesseDeplacement, self.coordoneePerso[1])

    def addCaisse(self, coordonee):
        self.caisses.append(coordonee)

    def moveUpCaisse(self, numCaisse):
        self.caisses[numCaisse] = (self.caisses[numCaisse][0], self.caisses[numCaisse][1] - self.vitesseDeplacement)

    def moveDownCaisse(self, numCaisse):
        self.caisses[numCaisse] = (self.caisses[numCaisse][0], self.caisses[numCaisse][1] + self.vitesseDeplacement)

    def moveRightCaisse(self, numCaisse):
        self.caisses[numCaisse] = (self.caisses[numCaisse][0] + self.vitesseDeplacement, self.caisses[numCaisse][1])

    def moveLeftCaisse(self, numCaisse):
        self.caisses[numCaisse] = (self.caisses[numCaisse][0] - self.vitesseDeplacement, self.caisses[numCaisse][1])


