#!/usr/bin/python3
"""Defines the BaseModel class. """
import uuid
from datetime import datetime
import models


class BaseModel:
    """basemodel"""

    def __init__(self, *args, **kwargs):
        """Documentation for __init__"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            for (key, value) in kwargs.items():
                if key in ['updated_at', 'created_at']:
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key != '__class__':
                    setattr(self, key, value)
        else:
            models.storage.new(self)

    def save(self):
        """Documentation for save"""
        self.updated_at = datetime.now()
        models.storage.save()

    def __str__(self):
        """Documentation for __str__"""
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def to_dict(self):
        """Documentation for to_dict"""
        result_dict = self.__dict__.copy()
        result_dict['__class__'] = self.__class__.__name__
        result_dict['created_at'] = self.created_at.isoformat()
        result_dict['updated_at'] = self.updated_at.isoformat()
        return result_dict
