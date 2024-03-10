import uuid
from datetime import datetime


class BaseModel():
    # both args and kwargs indicate an unknown number
    # of passed parameters. However kwargs makes use of parameters
    # that have keywords in them (mostly used for dictionaries)
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['updated_at', 'created_at']:
                        value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)
                else:
                    continue
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        # initialise a class either through dictionary input
        # or manual initialisation

    def save(self):
        self.updated_at = datetime.now()
        # save the update time into storage

    def __str__(self):
        # returns a string with object's name ID
        # and the dictionary with the rest of its attributes
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def to_dict(self):
        # Get the dictionary representation of the object's attributes
        result_dict = dict(self.__dict__)

        # Add a new field "__class__" to store the object's name
        result_dict['__class__'] = self.__class__.__name__

        # Convert created_at and updated_at into their ISO Format
        result_dict['created_at'] = self.created_at.isoformat()
        result_dict['updated_at'] = self.updated_at.isoformat()

        return result_dict
