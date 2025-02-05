from pydantic import BaseModel, Field
from typing import Optional

class CreateCategory(BaseModel):
    name : str = Field(...,examples = ['horror'])


class CategoryResponse(BaseModel):
    id : str = Field(...,examples = ['2j39sj3j4nei32k1k1l3o3j3n3h4gv4'])
    name : str = Field(...,examples = ['horror'])


class UpdateCategory(BaseModel):
    name : Optional[str] = Field(None,examples = ['horror'])
