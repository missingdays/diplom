
from sklearn.ensemble import RandomForestClassifier
from .model import Model

class RandomForest(Model):
    def __init__(self, parameters):
        super().__init__(RandomForestClassifier(**parameters))
