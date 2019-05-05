from .sensor_data_repository import SensorDataRepository, SensorData
from .sensor_repository import SensorRepository, Sensor

def test_add_sensor_data():
    sensor_repository = SensorRepository()
    repository = SensorDataRepository()

    sensor_id = sensor_repository.add_entity(Sensor(0, "test_sensor"))

    id = repository.add_entity(SensorData(0, sensor_id, process_id=0, value=100))
    assert id is not None

    repository.drop()
    sensor_repository.drop()

def test_get_sensor_data():
    sensor_repository = SensorRepository()
    repository = SensorDataRepository()

    sensor_id = sensor_repository.add_entity(Sensor(0, "test_sensor"))

    id = repository.add_entity(SensorData(0, sensor_id, process_id=0, value=100))
    sensor_data = repository.get_entity(id)

    assert sensor_data.id == id
    assert sensor_data.sensor_id == sensor_id
    assert sensor_data.process_id == 0
    assert sensor_data.value == 100

    repository.drop()
    sensor_repository.drop()
