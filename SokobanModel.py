from PyQt5.QtCore import QTimer


class SokobanModel:
    def __init__(self):
        self.views = []
        self.timer = QTimer()
        self.timer.timeout.connect(self.timeEvent)
        self.coordoneePerso = (0, 0)
        self.deplacement = 10
        self.caisses = []

    def setCoordoneePerso(self, x, y):
        self.coordoneePerso = (x, y)

    def addView(self, views):
        self.views.append(views)

    def timeEvent(self, number):
        self.views[number].update()

    def upMovement(self):
        self.setCoordoneePerso(self.coordoneePerso[0],self.coordoneePerso[1]-self.deplacement)

    def downMovement(self):
        self.setCoordoneePerso(self.coordoneePerso[0],self.coordoneePerso[1]+self.deplacement)

    def rightMovement(self):
        self.setCoordoneePerso(self.coordoneePerso[0]+self.deplacement,self.coordoneePerso[1])

    def leftMovement(self):
        self.setCoordoneePerso(self.coordoneePerso[0]-self.deplacement,self.coordoneePerso[1])

    def addCaisse(self,coordonee):
        self.caisses.append(coordonee)


