from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class PublisherInfo(BaseModel):
    id: str
    name: str

class CreateBook(BaseModel):
    name: str = Field(..., examples=["Harry Porter Chambers of secrets (VOLUME 1)"])
    description: str = Field(..., examples=["This is description about a book."])
    average_rating: float = Field(..., examples=[4.5])
    total_reviews: float = Field(..., examples=[150])


class UpdateBook(BaseModel):
    name: Optional[str] = Field(None, examples=["Harry Porter Chambers of secrets (VOLUME 1)"])
    description: Optional[str] = Field(None, examples=["This is description about a book."])
    author: Optional[list[str]] = []
    category: Optional[list[str]] = []
    publisher: Optional[PublisherInfo] = []
    # author: Optional[list[str]] = Field(None, examples=[{"_id": "6683e1a4710824df4e5d76e9",
    #                                                  "name": "James"}])
    # category: Optional[list[str]] = Field(None, examples=[{"_id": "6769be7156ca61f944fa3f90",
    #                                                  "name": "Fiction"}])
    # publisher: Optional[list[str]] = Field(None, examples=[{"_id": "6683e1a4710824df4e5d76e9",
    #                                                  "name": "Penguin Random House"}])
    average_rating: Optional[float] = Field(None, examples=[4.5])
    total_reviews: Optional[float] = Field(None, examples=[150])


class ResponseBook(BaseModel):
    created_at: Optional[datetime] = Field(None, examples=["2024-07-02T12:57:42.076000"])
    updated_at: Optional[datetime] = Field(None, examples=["2024-07-02T12:57:42.076000"])
    name: Optional[str] = Field(None, examples=["Harry Porter Chambers of secrets (VOLUME 1)"])
    description: Optional[str] = Field(None, examples=["This is description about a book."])
    author: Optional[list[str]] = []
    category: Optional[list[str]] = []
    publisher: Optional[PublisherInfo] = ["682376b52efc6621742144b1"]
    # author: Optional[list[str]] = Field(None, examples=[{"_id": "6683e1a4710824df4e5d76e9",
    #                                                  "name": "James"}])
    # category: Optional[str] = Field(None, examples=[{"_id": "6769be7156ca61f944fa3f90",
    #                                                  "name": "Fiction"}])
    # publisher: Optional[list[str]] = Field(None, examples=[{"_id": "6683e1a4710824df4e5d76e9",
    #                                                  "name": "Penguin Random House"}])
    average_rating: Optional[float] = Field(None, examples=[4.5])
    total_reviews: Optional[float] = Field(None, examples=[150])