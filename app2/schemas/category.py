from pydantic import BaseModel, Field
from app2.schemas.base_schema import BaseSchema

class CreateCategory(BaseModel):
    name: str = Field(..., examples=["Fiction"])
    description: str = Field(..., examples=["Fiction description"])

class UpdateCategory(BaseModel):
    name: str = Field(..., examples=["Fiction"])
    description: str = Field(..., examples=["Fiction description"])

class ResponseCategory(BaseSchema):
    name: str = Field(..., examples=["Fiction"])
    description: str = Field(..., examples=["Fiction description"])
    