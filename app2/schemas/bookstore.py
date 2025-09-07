from pydantic import BaseModel, Field
from typing import Optional

from app2.schemas.base_schema import BaseSchema, BasicSchema


class CreateBookstore(BaseModel):
    name: str = Field(..., example="Barnes & Noble")
    location: str = Field(..., example="New York, USA")

class UpdateBookstore(BaseModel):
    name: str = Field(..., example="Barnes & Noble")
    location: str = Field(..., example="New York, USA")

class ResponseBookstore(BaseSchema):
    name: str = Field(..., example=["Barnes & Noble"])
    location: str = Field(..., example=["New York, USA"])
    books: Optional[list[BasicSchema]] = Field(None, examples=[[{"id": "6683f946ec61bfa6a3c2d7c7", 
                                                      "name": "Harry Porter Chambers of secrets (VOLUME 1)"}]])
