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

def test_get_all():
    sensor_repository = SensorRepository()
    repository = SensorDataRepository()

    sensor_id_1 = sensor_repository.add_entity(Sensor(0, "test_sensor_1"))
    sensor_id_2 = sensor_repository.add_entity(Sensor(0, "test_sensor_2"))

    repository.add_entity(SensorData(0, sensor_id_1, process_id=0, value=100))
    repository.add_entity(SensorData(0, sensor_id_2, process_id=0, value=50))

    result = list(repository.get_all())

    assert len(result) == 2

    assert result[0].sensor_id == sensor_id_1
    assert result[0].process_id == 0
    assert result[0].value == 100
    assert result[1].sensor_id == sensor_id_2
    assert result[1].process_id == 0
    assert result[1].value == 50

    repository.drop()
    sensor_repository.drop()


