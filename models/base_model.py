import uuid
from datetime import datetime
class BaseModel():
    def __init__(self):
        id = str(uuid.uuid4())
        created_at = datetime.today()
        updated_at = datetime.today()

    def save(self):
        self.updated_at = datetime.today()
        # save the storage
    
    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
