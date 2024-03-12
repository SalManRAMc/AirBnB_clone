import json
from json.decoder import JSONDecodeError
import os

class FileStorage:
    """Initialise FileStorage"""
        
    __file_path = "file.json"
    __objects = {}


    def all(self):
        """Returns everything"""
        return FileStorage.__objects
    
    def new(self, obj):
        """Add Instance to dict"""
        key  = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """Saves Data"""
        existing_data = {}
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                existing_data = json.load(file)
        
        # Merge existing data with new data
        existing_data.update(self.__objects)

        # Write merged data back to the file
        with open(self.__file_path, 'w') as file:
            json.dump(existing_data, file)

    def reload(self):
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                self.__objects = data
            return
