from abc import ABC, abstractmethod

class System(ABC):

    @abstractmethod
    # rien à implémenter ici, c'est une classe abstraite
    def execute(self, actor):
        pass