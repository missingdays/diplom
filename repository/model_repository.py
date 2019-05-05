
class ModelRepository:

    def __init__(self):
        self.models = {}
        self.current_model = 0

    def add_entity(self, model):
        self.models[self.current_model] = model
        self.current_model += 1
        return self.current_model - 1

