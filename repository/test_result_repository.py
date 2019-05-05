
from .result_repository import ResultRepository, Result

def test_add_result():
    repository = ResultRepository()

    id = repository.add_entity(Result(0, 1, 1))
    assert id is not None

    repository.drop()

def test_get_result():
    repository = ResultRepository()

    id = repository.add_entity(Result(0, 1, 1))
    sensor_parameter = repository.get_entity(id)

    assert sensor_parameter.id == id
    assert sensor_parameter.process_id == 1
    assert sensor_parameter.result == 1

    repository.drop()

def test_get_all():
    repository = ResultRepository()

    repository.add_entity(Result(0, 1, 1))
    repository.add_entity(Result(0, 2, 0))

    result = list(repository.get_all())

    assert len(result) == 2
    assert result[0].process_id == 1
    assert result[0].result == 1
    assert result[1].process_id == 2
    assert result[1].result == 0

    repository.drop()
