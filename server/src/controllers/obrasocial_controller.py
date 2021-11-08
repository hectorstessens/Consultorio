from controllers.controller_base import controllerbase
from flask import Blueprint
from werkzeug.exceptions import HTTPException
from domain.obrasocial import ObraSocial
from services.service_base import servicebase;
from flask_cors import CORS

apiobrasocial = Blueprint('obrasocial', 'obrasocial')
routeapi = '/api/obrasocial'
service = servicebase(ObraSocial)
controllerapi = controllerbase(ObraSocial, service)
CORS(apiobrasocial)

@apiobrasocial.route(routeapi + '/<string:id>', methods=['GET'])
def api_getById(id):
    return controllerapi.api_getById(id)

@apiobrasocial.route(routeapi, methods=['GET'])
def api_get():
    return controllerapi.api_get()

@apiobrasocial.route(routeapi, methods=['POST'])
def api_post():
    return controllerapi.api_post()

@apiobrasocial.route(routeapi + '/<string:id>', methods=['PUT'])
def api_put(id):
    return controllerapi.api_put(id)

@apiobrasocial.route(routeapi + '/<string:id>', methods=['DELETE'])
def api_delete(id):
    return controllerapi.api_delete(id)

@apiobrasocial.errorhandler(HTTPException)
def handle_exception(e):
    return controllerapi.handle_exception(e)