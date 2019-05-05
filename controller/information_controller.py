
from dataclasses import dataclass

class InformationController:

    def __init__(self, sensor_repository, sensor_parameter_repository):
        self.sensor_repository = sensor_repository
        self.sensor_parameter_repository = sensor_parameter_repository

    def handle_sensor(self, sensor):
        return self.sensor_repository.add_entity(sensor)

    def handle_sensor_parameter(self, sensor_parameter):
        return self.sensor_parameter_repository.add_entity(sensor_parameter)

@dataclass
class SensorRequest:
    name: str

@dataclass
class SensorParameterRequest:
    sensor_id: str
    name: str
    value: int
