from dataclasses import dataclass


class ModelController:
    def __init__(self, model_repository, train_data, models):
        self.train_data = train_data
        self.models = models

        self.model_repository = model_repository

    def handle_build(self, build_request):
        X, y = train_data.get()

        model = models.get(build_request.model, build_request.parameters)
        model.fit(X, y)

        return self.model_repository.add_entity(model)


@dataclass
class BuildRequest:
    model: str
    parameters: object
