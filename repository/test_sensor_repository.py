
from .sensor_repository import SensorRepository, Sensor

def test_add_sensor():
    repository = SensorRepository()

    id = repository.add_entity(Sensor(0, name="test"))
    assert id is not None

    repository.drop()

def test_get_sensor():
    repository = SensorRepository()

    id1 = repository.add_entity(Sensor(0, name="test1"))
    id2 = repository.add_entity(Sensor(0, name="test2"))

    sensor = repository.get_entity(id1)
    assert sensor.name == "test1"

    sensor = repository.get_entity(id2)
    assert sensor.name == "test2"

    repository.drop()
