from controllers.controller_base import controllerbase
from flask import Blueprint
from werkzeug.exceptions import HTTPException
from domain.apm import Apm
from services.service_base import servicebase;
from flask_cors import CORS

apiamp = Blueprint('amp', 'amp')
routeapi = '/api/apm'
service = servicebase(Apm)
controllerapi = controllerbase(Apm, service)
CORS(apiamp)

@apiamp.route(routeapi + '/<string:id>', methods=['GET'])
def api_getById(id):
    return controllerapi.api_getById(id)

@apiamp.route(routeapi, methods=['GET'])
def api_get():
    return controllerapi.api_get()

@apiamp.route(routeapi, methods=['POST'])
def api_post():
    return controllerapi.api_post()

@apiamp.route(routeapi + '/<string:id>', methods=['PUT'])
def api_put(id):
    return controllerapi.api_put(id)

@apiamp.route(routeapi + '/<string:id>', methods=['DELETE'])
def api_delete(id):
    return controllerapi.api_delete(id)

@apiamp.errorhandler(HTTPException)
def handle_exception(e):
    return controllerapi.handle_exception(e)