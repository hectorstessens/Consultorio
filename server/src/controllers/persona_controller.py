from http import HTTPStatus
import json

from flask.wrappers import Response
from controllers.controller_base import controllerbase
from flask import Blueprint
from werkzeug.exceptions import HTTPException
from domain.persona import Persona
from domain.personaDNIView import PersonaDNIView
from services.service_base import servicebase;
from services.persona_service import PersonaService
from flask_cors import CORS

apipersona = Blueprint('persona', 'persona')
routeapi = '/api/persona'
service = servicebase(Persona)
controllerapi = controllerbase(Persona, service)
CORS(apipersona)

@apipersona.route(routeapi + '/<string:id>', methods=['GET'])
def api_getById(id):
    return controllerapi.api_getById(id)

@apipersona.route(routeapi, methods=['GET'])
def api_get():
    return controllerapi.api_get()

@apipersona.route(routeapi, methods=['POST'])
def api_post():
    return controllerapi.api_post()

@apipersona.route(routeapi + '/<string:id>', methods=['PUT'])
def api_put(id):
    return controllerapi.api_put(id)

@apipersona.route(routeapi + '/<string:id>', methods=['DELETE'])
def api_delete(id):
    return controllerapi.api_delete(id)

@apipersona.errorhandler(HTTPException)
def handle_exception(e):
    return controllerapi.handle_exception(e)


@apipersona.route(routeapi +'/DNI/<string:DNI>', methods=['GET', 'POST'])
def buscarPersona(DNI):    
    result = PersonaService.buscarPersona(DNI)

    if result is not None:
        persona = PersonaDNIView(result.IdPersona,result.DNI,result.Nombre,result.Apellido)
        response = Response(json.dumps(persona.__dict__), status=HTTPStatus.OK, mimetype='application/json')
    else:
        response = Response("Persona no encontrada", status=HTTPStatus.NOT_FOUND, mimetype='application/json')
    return response