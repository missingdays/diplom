from sklearn.neighbors import KNeighborsClassifier
from .model import Model

class KNeighbors(Model):
    def __init__(self, parameters):
        super().__init__(KNeighborsClassifier(**parameters))
