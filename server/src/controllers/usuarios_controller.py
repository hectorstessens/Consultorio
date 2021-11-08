import json
from flask.globals import request
from flask.wrappers import Response
from controllers.controller_base import controllerbase
from flask import Blueprint
from werkzeug.exceptions import HTTPException
from domain.usuarios import Usuarios
from domain.user import User
from services.service_base import servicebase
from services.usuarios_service import UsuarioService
from http import HTTPStatus
from flask_cors import CORS

apiusuarios = Blueprint('usuarios', 'usuarios')
routeapi = '/api/usuarios'
service = servicebase(Usuarios)
controllerapi = controllerbase(Usuarios, service)
CORS(apiusuarios)

@apiusuarios.route(routeapi + '/<string:id>', methods=['GET'])
def api_getById(id):
    return controllerapi.api_getById(id)

@apiusuarios.route(routeapi, methods=['GET'])
def api_get():
    return controllerapi.api_get()

@apiusuarios.route(routeapi, methods=['POST'])
def api_post():
    return controllerapi.api_post()

@apiusuarios.route(routeapi + '/<string:id>', methods=['PUT'])
def api_put(id):
    return controllerapi.api_put(id)

@apiusuarios.route(routeapi + '/<string:id>', methods=['DELETE'])
def api_delete(id):
    return controllerapi.api_delete(id)

@apiusuarios.errorhandler(HTTPException)
def handle_exception(e):
    return controllerapi.handle_exception(e)

@apiusuarios.route(routeapi + '/login', methods=['GET', 'POST'])
def login():
    content = request.json
    username = content['username']
    password = content['password']
    result = UsuarioService.login(username,password)
    if result is not None:
        user = User(result.IdUsuario,result.UserName,result.Password,"first","Last","token")
        response = Response(json.dumps(user.__dict__), status=HTTPStatus.OK, mimetype='application/json')
        return response
    else:
        response = Response("Usuario o Password Incorrecto", status=HTTPStatus.NOT_FOUND, mimetype='application/json')
        return response

 