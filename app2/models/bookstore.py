from pydantic import BaseModel
from app2.schemas.base_schema import BasicSchema

class bookstore(BaseModel):
    name: str
    location: str