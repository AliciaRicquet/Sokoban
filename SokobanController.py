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

    def movement(self, dir):
        perso = [self.model.getCoordonneePerso()[0] - dir[0]], [self.model.getCoordonneePerso()[1] - dir[1]]
        if self.verifMurPerso(dir) and self.verifCaisses(dir):
            self.model.setCoordoneePerso([self.model.getCoordonneePerso()[0] + dir[0], self.model.getCoordonneePerso()[1] + dir[1]])
            self.__matrix = perso
            self.model.update(self.model.getMatrix())


    def verifMurPerso(self, dir):
        matrice = self.model.getMatrix()
        cooPerso = self.model.getCoordonneePerso()
        if matrice[cooPerso[0] + dir[0]][cooPerso[1] + dir[1]] != 2:
            return True
        return False

    def verifCaisses(self, dir):
        matrice = self.model.getMatrix()
        cooPerso = self.model.getCoordonneePerso()
        cooCaisse = self.model.getCaisse()
        for elements in cooCaisse:
            if  elements[0] == cooPerso[0]+dir[0] and elements[1] == cooPerso[1]+dir[1]:
                return False
            print(cooPerso)
        return True
