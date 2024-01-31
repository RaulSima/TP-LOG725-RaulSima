
class Entity():
    id = 0
    components = {}

    def __init__(self, id):
        self.id = id

    def addComponent(self, name, component):
        self.components[name] = component
    
    def searchComponent(self, name):
        return self.components[name]
    
    def getId(self):
        return self.id