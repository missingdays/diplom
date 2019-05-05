from .sensor_parameter_repository import SensorParameterRepository, SensorParameter
from .sensor_repository import SensorRepository, Sensor

def test_add_sensor_parameter():
    sensor_repository = SensorRepository()
    repository = SensorParameterRepository()

    sensor_id = sensor_repository.add_entity(Sensor(0, "test_sensor"))

    id = repository.add_entity(SensorParameter(0, sensor_id, name="test", value=0))
    assert id is not None

    repository.drop()
    sensor_repository.drop()

def test_get_sensor_parameter():
    sensor_repository = SensorRepository()
    repository = SensorParameterRepository()

    sensor_id = sensor_repository.add_entity(Sensor(0, "test_sensor"))

    id = repository.add_entity(SensorParameter(0, sensor_id, name="test", value=0))
    sensor_parameter = repository.get_entity(id)

    assert sensor_parameter.id == id
    assert sensor_parameter.sensor_id == sensor_id
    assert sensor_parameter.name == "test"
    assert sensor_parameter.value == 0

    repository.drop()
    sensor_repository.drop()
