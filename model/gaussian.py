from sklearn.naive_bayes import GaussianNB as GNB
from .model import Model

class GaussianNB(Model):
    def __init__(self, parameters):
        super().__init__(GNB(**parameters))

