class SokobanController:
    """
    TODO
    - fonction changement de direction
    - mise en place timer  et mise a jour du model
    - gestion des evenements de la vue et gerer deplacement caisse
    PS: hesitez pas a ajouter des idéee
    """
    def __init__(self):
        self.model = None
        self.views = []

    def addView(self, views):
        self.views.append(views)

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
