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
        perso = [[self.model.getCoordonneePerso()[0] + dir[0]], [self.model.getCoordonneePerso()[1] + dir[1]]]
        if self.verifMurPerso(dir):
            if self.verifCaisses(dir):
                self.model.setCoordoneePerso(
                    [self.model.getCoordonneePerso()[0] + dir[0], self.model.getCoordonneePerso()[1] + dir[1]]
                )
                self.model.addPas()
                self.__matrix = perso
                self.model.update(self.model.getMatrix())
            elif not self.verifCaisses(dir):
                if self.verifMurCaisse(dir):
                    print("caisse avant ", self.model.getCaisse())
                    indice = self.obtenirLaCaisseABouger(dir)
                    self.model.modifierCaisse(
                        indice,[
                            self.model.getCaisse()[indice][0] + dir[0], self.model.getCaisse()[indice][1] + dir[1]
                        ])
                    self.model.setCoordoneePerso(
                        [self.model.getCoordonneePerso()[0] + dir[0], self.model.getCoordonneePerso()[1] + dir[1]]
                    )
                    print("caisse après", self.model.getCaisse())
                    self.model.addPas()
                    self.__matrix = perso
                    self.model.update(self.model.getMatrix())
                print(self.model.getPas())


    def obtenirLaCaisseABouger(self,coo):
        caisse = self.model.getCaisse()
        perso = self.model.getCoordonneePerso()
        for i in range(len(caisse)):
            if perso[0] + coo[0] == caisse[i][0] and  perso[1] + coo[1] == caisse[i][1]:
                return i


    def verifMurPerso(self, dir):
        matrice = self.model.getMatrix()
        cooPerso = self.model.getCoordonneePerso()
        if matrice[cooPerso[0] + dir[0]][cooPerso[1] + dir[1]] != 2:
            return True
        return False

    def verifMurCaisse(self,dir):
        matrice = self.model.getMatrix()
        cooPerso = self.model.getCoordonneePerso()
        if matrice[cooPerso[0] + (dir[0])*2][cooPerso[1] + (dir[1])*2] != 2:
            for element in self.model.getCaisse():
                if element[0] == cooPerso[0] + (dir[0])*2 and element[0] == cooPerso[1] + (dir[1])*2 :
                    return False
            return True
        return False

    def verifCaisses(self, dir):
        cooPerso = self.model.getCoordonneePerso()
        cooCaisse = self.model.getCaisse()
        for elements in cooCaisse:
            if  elements[0] == cooPerso[0]+dir[0] and elements[1] == cooPerso[1]+dir[1]:
                return False
        return True
