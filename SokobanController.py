

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
        self.timer.timeout.connect(self.timeEvent)
        self.timer.start(60)
        self.mur == False

    def setView(self, view):
        self.view = view

    def setModel(self, model):
        self.model = model


    def upMovement(self):
        self.model.setCoordoneePerso(self.model.getCoordoneePerso[0], self.model.getCoordoneePerso[1]
                                     - self.model.getVitesseDeplacement)

    def downMovement(self):
        self.model.setCoordoneePerso(self.model.getCoordoneePerso[0], self.model.getCoordoneePerso[1] +
                                     self.model.getVitesseDeplacement)

    def rightMovement(self):
        self.model.setCoordoneePerso(self.model.getCoordoneePerso[0] + self.model.getVitesseDeplacement,
                                     self.model.getCoordoneePerso[1])

    def leftMovement(self):
        self.model.setCoordoneePerso(self.model.getCoordoneePerso[0] - self.model.getVitesseDeplacement,
                                     self.model.getCoordoneePerso[1])

    def  verifMur(self):
        matrice = self.model.getMatrix()
        for i in range(len(self.model.matrix)):
            for j in range(len(self.model.matrix[0])):
                if matrice[i][j] == 3:
                    if self.model.getCoordoneePerso == matrice:
                        return True
        return False

    def changerDirection(self, dir):
        if dir != (-self.model.getDirection()[0], -self.model.getDirection()[1]) and dir != self.verifMur():
            if self.upMovement():
                self.model.setDirection(dir)
            elif self.downMovement():
                self.model.setDirection(dir)
            elif self.rightMovement():
                self.model.setDirection(dir)
            elif self.leftMovement():
                self.model.setDirection(dir)

