from flask import Flask, request, abort, jsonify

from repository import SensorRepository, SensorParameterRepository, SensorDataRepository, ResultRepository, ModelRepository, TrainData

from controller import InformationController, SensorRequest, SensorParameterRequest
from controller import ModelController, BuildRequest

from model import Models

app = Flask(__name__)

sensor_repository = SensorRepository()
sensor_parameter_repository = SensorParameterRepository()
sensor_data_repository = SensorDataRepository()
result_repository = ResultRepository()

model_controller = ModelController(ModelRepository(), TrainData(sensor_data_repository, result_repository), Models())
information_controller = InformationController(sensor_repository, sensor_parameter_repository)

@app.route("/api/information/sensor", methods=["POST"])
def information_sensor():
    if not request.json or 'name' not in request.json:
        abort(400)

    id = information_controller.handle_sensor(SensorRequest(name = request.json["name"]))

    return jsonify({'id': id}), 201

@app.route("/api/information/sensor_parameter", methods=["POST"])
def information_sensor_parameter():
    if not request.json or 'sensor_id' not in request.json or 'name' not in request.json or 'value' not in request.json:
        abort(400)

    id = information_controller.handle_sensor_parameter(
            SensorParameterRequest(
                sensor_id=request.json['sensor_id'],
                name=request.json['name'],
                value=int(request.json['value'])
            )
        )

    return jsonify({'id': id}), 201

@app.route("/api/model/build", methods=["POST"])
def model_build():
    if not request.json or 'model' not in request.json:
        abort(400)

    id = model_controller.handle_build(
        BuildRequest(
            model=request.json["model"],
            parameters=request.json.get("parameters", {})
        )
    )

    return jsonify({'id': id}), 201
