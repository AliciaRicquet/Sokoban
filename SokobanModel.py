from PyQt5.QtCore import QTimer


# 0 = case libre   1 = joueur, 2 = mur, 3 = trou(objectif rien de personnel hein), 4 caisse
class SokobanModel:
    def __init__(self, level):
        assert level == 1 or level == 2

        self.__views = []
        self.__timer = QTimer()
        self.__timer.timeout.connect(self.timeEvent)
        self.__vitesseDeplacement = 10
        self.__caisses = []
        self.__direction = (0, 1)
        self.__level = level
        self.__tabGoal = []
        if self.__level == 1:
            self.__matrix = [
                [0, 0, 2, 2, 2, 0, 0, 0],
                [0, 0, 2, 3, 2, 0, 0, 0],
                [0, 0, 2, 4, 2, 2, 2, 2],
                [2, 2, 2, 0, 1, 4, 3, 2],
                [2, 3, 0, 4, 4, 2, 2, 2],
                [2, 2, 2, 2, 0, 2, 0, 0],
                [0, 0, 0, 2, 3, 2, 0, 0],
                [0, 0, 0, 2, 2, 2, 0, 0]
            ]
        elif self.__level == 2:
            self.__matrix = [
                [0, 0, 0, 2, 2, 2, 2, 2, 0],
                [0, 2, 2, 2, 0, 0, 0, 2, 0],
                [0, 2, 3, 1, 4, 0, 0, 2, 0],
                [0, 2, 2, 2, 0, 4, 3, 2, 0],
                [0, 2, 3, 2, 2, 4, 0, 2, 2],
                [0, 2, 0, 2, 0, 3, 0, 0, 2],
                [0, 2, 4, 0, 0, 4, 4, 3, 2],
                [0, 2, 0, 0, 0, 3, 0, 0, 2],
                [0, 2, 2, 2, 2, 2, 2, 2, 2]
            ]
        for i in range(len(self.__matrix)):
            for j in range(len(self.__matrix[0])):
                if self.__matrix[i][j] == 3:
                    self.__tabGoal.append((i, j))
                if self.__matrix[i][j] == 1:
                    self.__coordonneePerso = (i, j)

    def getTabGoal(self):
        return self.__tabGoal

    def getCoordonneePerso(self):
        return self.__coordonneePerso

    def addView(self, views):
        self.__views.append(views)

    def timeEvent(self, numberOfView):
        self.__views[numberOfView].update()

    def getVitesseDeplacement(self):
        return self.__vitesseDeplacement

    def setMatrix(self):
        self.__views.update()

    def addCaisse(self, coordonee):
        self.__caisses.append(coordonee)

    def getLevel(self):
        return self.__level

    def setLevel(self, number):
        self.__level = number

    def getMatrix(self):
        return self.__matrix
