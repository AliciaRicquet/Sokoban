class SokobanController:
    def __init__(self):
        self.model = None
        self.views = []

    def addView(self,views):
        self.views.append(views)

    def setModel(self, model):
        self.model = model

