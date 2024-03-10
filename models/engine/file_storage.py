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
        with open(FileStorage.__file_path,"w") as file:
            json.dump(
            {k: v.to_dict()
            for k, v in FileStorage.__objects.items}, file
        )

    def reload(self):
        try:
            deserialize = {}
            with open(FileStorage.__file_path) as f:
                deserialize = json.loads(f.read())
            FileStorage.__objects = {
                k: eval(v["__class__"])(**v)
                for k, v in deserialize.items()
            }
        except (FileNotFoundError, JSONDecodeError):
            pass
        except Exception as e:
            raise e
