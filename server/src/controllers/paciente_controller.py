from controllers.controller_base import controllerbase
from flask import Blueprint
from werkzeug.exceptions import HTTPException

from services.service_base import servicebase;
from controllers.controller_base import controllerbase
from domain.paciente import Paciente
from flask_cors import CORS

apipaciente = Blueprint('pacientes', 'pacientes')
routeapi = '/api/pacientes'
service = servicebase(Paciente)
controllerapi = controllerbase(Paciente, service)
CORS(apipaciente)

@apipaciente.route(routeapi + '/<string:id>', methods=['GET'])
def api_getById(id):
    return controllerapi.api_getById(id)

@apipaciente.route(routeapi, methods=['GET'])
def api_get():
    return controllerapi.api_get()

@apipaciente.route(routeapi, methods=['POST'])
def api_post():
    return controllerapi.api_post()

@apipaciente.route(routeapi + '/<string:id>', methods=['PUT'])
def api_put(id):
    return controllerapi.api_put(id)

@apipaciente.route(routeapi + '/<string:id>', methods=['DELETE'])
def api_delete(id):
    return controllerapi.api_delete(id)

@apipaciente.errorhandler(HTTPException)
def handle_exception(e):
    return controllerapi.handle_exception(e)
