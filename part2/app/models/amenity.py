from app.models.BaseModel import BaseModel

class Amenity(BaseModel):
    def __init__(self, name=None, **kwargs):
        super().__init__()
        self.name = name or kwargs.get('name')
