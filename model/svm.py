
from sklearn.svm import SVC
from .model import Model

class SVM(Model):
    def __init__(self, parameters):
        super().__init__(SVC(**parameters))
