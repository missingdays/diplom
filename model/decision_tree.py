
from sklearn.tree import DecisionTreeClassifier
from .model import Model

class DecisionTree(Model):
    def __init__(self, parameters):
        super().__init__(DecisionTreeClassifier(**parameters))
