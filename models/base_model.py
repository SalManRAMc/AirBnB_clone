import uuid
from datetime import datetime
class BaseModel():
    def __init__(self):
        id = str(uuid.uuid4())
        created_at = datetime.now()
        updated_at = datetime.now()

    def save(self):
        self.updated_at = datetime.now()
        # save the storage
    
    def __str__(self):
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