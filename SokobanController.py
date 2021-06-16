class SokobanController:
    """
    TODO - fonction changement de direction - mise en place timer  et mise a jour du model - gestion des evenements
    TODO - de la vue et gerer deplacement caisse - methode pour ajouter les differentes valeur a la matrice :
    TODO - 0 = case libre   1 = joueur, 2 = mur, 3 = trou(objectif rien de personnel hein)
    PS: hesitez pas a ajouter des idéee
    """

    def __init__(self):
        self.model = None
        self.view = None
        self.__matrix = None

    def setView(self, view):
        self.view = view

    def setModel(self, model):
        self.model = model
        self.__matrix = self.model.getMatrix()

    def upMovement(self):
        tmp = self.model.getCoordoneePerso()

    def downMovement(self):
        self.model.setCoordoneePerso(self.model.getCoordoneePerso[0], self.model.getCoordoneePerso[1] +
                                     self.model.getVitesseDeplacement)

    def rightMovement(self):
        self.model.setCoordoneePerso(self.model.getCoordoneePerso[0] + self.model.getVitesseDeplacement,
                                     self.model.getCoordoneePerso[1])

    def leftMovement(self):
        self.model.setCoordoneePerso(self.model.getCoordoneePerso[0] - self.model.getVitesseDeplacement,
                                     self.model.getCoordoneePerso[1])

    def verifMurPerso(self, dir):
        matrice = self.model.getMatrix()
        cooPerso = self.model.getCoordoneePerso()
        if matrice[cooPerso[0] + dir[0]][cooPerso[1] + dir[1]] != 2:
            return True
        return False

    def changeDirection(self, dir):
        if self.verifMurPerso(dir):
            if self.upMovement():
                self.model.setDirection(dir)
            elif self.downMovement():
                self.model.setDirection(dir)
            elif self.rightMovement():
                self.model.setDirection(dir)
            elif self.leftMovement():
                self.model.setDirection(dir)
