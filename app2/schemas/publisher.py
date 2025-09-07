from pydantic import BaseModel, Field
from typing import Optional

from app2.schemas.base_schema import BaseSchema, BasicSchema


class CreatePublisher(BaseModel):
    name: str = Field(..., example="Penguin Random House")
    location: str = Field(..., example="New York, USA")

class UpdatePublisher(BaseModel):
    name: str = Field(None, example="Penguin Random House")
    location: str = Field(None, example="New York, USA")

class ResponsePublisher(BaseSchema):
    name: str = Field(..., example=["Penguin Random House"])
    location: str = Field(..., example=["New York, USA"])
    books: list[BasicSchema] = []
