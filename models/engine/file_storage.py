import json
from json.decoder import JSONDecodeError

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
        new_dict = {}
        for k, v in self.__objects.items():
            new_dict[k] = v.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(new_dict, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
