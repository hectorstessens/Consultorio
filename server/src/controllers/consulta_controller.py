from controllers.controller_base import controllerbase
from flask import Blueprint
from werkzeug.exceptions import HTTPException
from domain.consulta import Consulta
from services.service_base import servicebase;
from flask_cors import CORS

apiconsulta = Blueprint('consulta', 'consulta')
routeapi = '/api/consulta'
service = servicebase(Consulta)
controllerapi = controllerbase(Consulta, service)
CORS(apiconsulta)

@apiconsulta.route(routeapi + '/<string:id>', methods=['GET'])
def api_getById(id):
    return controllerapi.api_getById(id)

@apiconsulta.route(routeapi, methods=['GET'])
def api_get():
    return controllerapi.api_get()

@apiconsulta.route(routeapi, methods=['POST'])
def api_post():
    return controllerapi.api_post()

@apiconsulta.route(routeapi + '/<string:id>', methods=['PUT'])
def api_put(id):
    return controllerapi.api_put(id)

@apiconsulta.route(routeapi + '/<string:id>', methods=['DELETE'])
def api_delete(id):
    return controllerapi.api_delete(id)

@apiconsulta.errorhandler(HTTPException)
def handle_exception(e):
    return controllerapi.handle_exception(e)