class Manager():
    entities = []

    def addEntity(self, entity):
        self.entities.append(entity)
    
    def getEntities(self):
        return self.entities