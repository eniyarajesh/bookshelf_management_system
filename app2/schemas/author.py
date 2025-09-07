from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class CreateAuthor(BaseModel):
    name: str = Field(..., example="James")
    age: int = Field(..., example=25)
    gender: str = Field(..., example="Male")
    total_published: int = Field(..., example=4)

class UpdateAuthor(BaseModel):
    created_at: Optional[datetime] = Field(None, examples=["2024-07-02T12:57:42.076000"])
    updated_at: Optional[datetime] = Field(None, examples=["2024-07-02T12:57:42.076000"])
    latest_books: Optional[list[str]] = []
    name: Optional[str] = Field(None, example="James")
    age: Optional[int] = Field(None, example=25)
    gender: Optional[str] = Field(None, example="Male")
    total_published: Optional[int] = Field(None, example=4)

class ResponseAuthor(BaseModel):
    created_at: Optional[datetime] = Field(None, examples=["2024-07-02T12:57:42.076000"])
    updated_at: Optional[datetime] = Field(None, examples=["2024-07-02T12:57:42.076000"])
    latest_books: Optional[list[str]] = []
    name: Optional[str] = Field(None, example="James")
    age: Optional[int] = Field(None, example=25)
    gender: Optional[str] = Field(None, example="Male")
    total_published: Optional[int] = Field(None, example=4)

