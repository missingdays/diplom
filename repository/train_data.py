
from collections import defaultdict

import pandas as pd

class TrainData:
    def __init__(self, sensor_data_repository, result_repository):
        self.sensor_data_repository = sensor_data_repository
        self.result_repository = result_repository

    def get(self):
        data = self.sensor_data_repository.get_all()
        result = self.result_repository.get_all()

        return self.group_by_process_id(data, result)

    def group_by_process_id(self, data, result):
        X = defaultdict(list)
        y = {}

        for data_point in data:
            X[data_point.process_id].append(data_point)

        for result_point in result:
            y[result_point.process_id] = result_point

        return self.create_df(X, y)

    def create_df(self, X, y):
        index = list(X.keys())

        return pd.DataFrame(self.create_X(X), index=index), pd.Series(self.create_y(y))

    def create_X(self, X):
        columns = defaultdict(list)

        for process_id, values in X.items():
            for value in sorted(values, key=lambda x: x.process_id):
                columns[value.name].append(value.value)

        return columns

    def create_y(self, y):
        result = []

        for r in sorted(y, key=lambda x: x.process_id):
            result.append(r.result)

        return result
