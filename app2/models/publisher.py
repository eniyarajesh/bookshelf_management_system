from pydantic import BaseModel, Field
from typing import Optional
from app2.schemas.base_schema import BasicSchema

class Publisher(BaseModel):
    name: str
    location: str
