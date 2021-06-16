# 0 = case libre   1 = joueur,, 2 = mur, 3 = trou(objectif rien de personnel hein), 4 caisse
class SokobanModel:
    def __init__(self, level):
        assert level == 1 or level == 2

        self.__view = None
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
            for x in range(self.matrix):
                for y in (self.matrix[0]):
                    if self.matrix[x][y] == 4:
                        self.caisses.append((x, y))

    def getCoordonneePerso(self):
        return self.coordoneePerso

    def addView(self, view):
        self.__view.append(view)

    def updateView(self):
        self.__view.update()

    def getDirection(self):
        return self.direction

    def getCaisse(self):
        return self.caisses

    def setDirection(self, direction):
        self.direction = direction

    def getLevel(self):
        return self.level

    def setLevel(self, number):
        self.level = number

    def getMatrix(self):
        return self.matrix
