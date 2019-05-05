
from . import KNeighbors, SVM, DecisionTree, GaussianNB

class Models:
    def get(self, name, parameters):
        if name == 'KNeighbors':
            return KNeighbors(**parameters)
        elif name == 'SVM':
            return SVM(**parameters)
        elif name == 'DecisionTree':
            return DecisionTree(**parameters)
        elif name == 'RandomForest':
            return RandomForest(**parameters)
        elif name == 'GaussianNB':
            return GaussianNB(**parameters)

        raise Exception("Unknown model {}".format(name))
