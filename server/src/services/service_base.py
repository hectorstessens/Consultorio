#!/usr/bin/env python
from domain.paciente import Paciente
from config import db
from werkzeug.exceptions import NotFound

class servicebase:
 
    def __init__(self,_entity):
        self.entitymodel = _entity

    def getById(self,id):
        '''
        Delete entity by id
        :param id: the entity id
        :returns: the response
        '''
        entity = self.entitymodel.query.get(id)
        if entity:
            return entity
        raise NotFound('no such entity found with id=' + str(id))

    def get(self):
        '''
        Get all entities
        :returns: all entity
        '''
        return self.entitymodel.query.all()

    def post(self,body):
        '''
        Create entity with body
        :param body: request body
        :returns: the created entity
        '''
        print(body) 
        entity = self.entitymodel(**body)
        db.session.add(entity)
        db.session.commit()
        return entity

    def put(self,body):
        '''
        Update entity by id
        :param body: request body
        :returns: the updated entity
        '''
        entity = self.getentitymodel.query.get(body['id'])
        if entity:
            entity = self.entitymodel(**body)
            db.session.merge(entity)
            db.session.flush()
            db.session.commit()
            return entity
        raise NotFound('no such entity found with id=' + str(body['id']))

    def delete(self,id):
        '''
        Delete entity by id
        :param id: the entity id
        :returns: the response
        '''
        entity = self.entitymodel.query.get(id)
        if entity:
            db.session.delete(entity)
            db.session.commit()
            return {'success': True}
        raise NotFound('no such entity found with id=' + str(id))


