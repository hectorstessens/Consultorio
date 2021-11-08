#!/usr/bin/env python
from flask import  jsonify, request
import json

class controllerbase:
    def __init__(self,entity,service):
        self.entity = entity
        self.service = service


    def api_getById(self,id):
        ''' Get by id'''
        entity = self.service.getById(id)
        return jsonify(entity.as_dict())

    def api_get(self):
        ''' Get all entities'''
        entities = self.service.get()
        return jsonify([entity.as_dict() for entity in entities])

    def api_post(self):
        ''' Create entity'''
        entity = self.service.post(request.json)
        return jsonify(entity.as_dict())

    def api_put(self,id):
        ''' Update entity by id'''
        body = request.json
        body['id'] = id
        res = self.service.put(body)
        return jsonify(res.as_dict()) if isinstance(res, self.entity) else jsonify(res)

    def api_delete(self,id):
        ''' Delete entity by id'''
        res = self.service.delete(id)
        return jsonify(res)

    def handle_exception(self,e):
        """Return JSON format for HTTP errors."""
        # start with the correct headers and status code from the error
        response = e.get_response()
        # replace the body with JSON
        response.data = json.dumps({
            'success': False,
            "message": e.description
        })
        response.content_type = "application/json"
        return response