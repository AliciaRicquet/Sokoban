# 0 = case libre   1 = joueur,, 2 = mur, 3 = trou(objectif rien de personnel hein), 4 caisse
class SokobanModel:
    def __init__(self, level):
        assert level == 1 or level == 2

        self.__view = None
        self.caisses = []
        self.__trou = []
        self.direction = (0, 1)
        if level == 1:
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
        else:
            self.matrix = [
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
        for x in range(len(self.matrix)):
            for y in range (len(self.matrix[0])):
                if self.matrix[x][y] == 1:
                    self.coordonneePerso = (x, y)
                elif self.matrix[x][y] == 4:
                    self.caisses.append((x, y))
                elif self.matrix[x][y] == 3:
                    self.__trou.append((x, y))

    def getCoordonneePerso(self):
        return self.coordonneePerso

    def setCoordoneePerso(self,coo):
        self.coordonneePerso = coo

    def addView(self, view):
        self.__view = view

    def update(self, matrix):
        self.matrix = matrix
        self.__view.update()

    def getDirection(self):
        return self.direction

    def getCaisse(self):
        return self.caisses

    def setDirection(self, direction):
        self.direction = direction

    def getMatrix(self):
        return self.matrix
