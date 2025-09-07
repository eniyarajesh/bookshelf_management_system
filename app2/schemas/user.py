from pydantic import BaseModel, Field, EmailStr
from app2.schemas.base_schema import BaseSchema, BasicSchema
from typing import List, Optional
from datetime import datetime

class CreateUser(BaseModel):
    name: str = Field(..., examples=["Albert Joseph"])
    email: EmailStr = Field(..., examples=["test@gmail.com"])
    gender: str = Field(..., examples=["Male"])
    age: int = Field(..., examples=[25])
    favorite_books: List[str] 

class UpdateUser(BaseModel):
    created_at: Optional[datetime] = Field(None, examples=["2024-07-02T07:27:29.278000"])
    updated_at: Optional[datetime] = Field(None, examples=["2024-07-02T07:27:29.278000"])
    name: Optional[str] = Field(None, examples=["Albert Joseph"])
    email: Optional[EmailStr] = Field(None, examples=["test@gmail.com"])
    gender: Optional[str] = Field(None, examples=["Male"])
    phone_number: Optional[str] = Field(None, examples=["+918856852123"])
    age: Optional[int] = Field(None, examples=[25])
    # favorite_books: Optional[List[str]] = Field(None, examples=[{"id": "6683f946ec61bfa6a3c2d7c7",
    #                                                         "name": "Harry Porter Chambers of secrets (VOLUME 1)"}])
    favorite_books: Optional[List[str]] = []
    total_reviews: Optional[int] = Field(None, examples=[10])

class ResponseUser(BaseSchema):
    created_at: datetime = Field(..., examples=["2024-07-02T07:27:29.278000"])
    updated_at: datetime = Field(..., examples=["2024-07-02T07:27:29.278000"])
    name: str = Field(..., examples=["Albert Joseph"])
    email: EmailStr = Field(..., examples=["test@gmail.com"])
    gender: str = Field(..., examples=["Male"])
    phone_number: Optional[str] = Field(None, examples=["+918856852123"])
    age: Optional[int] = Field(None, examples=[25])
    favorite_books: Optional[list] = []
    # favorite_books: Optional[list] = Field(..., examples=[{"id": "6683f946ec61bfa6a3c2d7c7",
    #                                                         "name": "Harry Porter Chambers of secrets (VOLUME 1)"}])
    total_reviews: int = Field(..., examples=[10])