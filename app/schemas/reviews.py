from pydantic import BaseModel, Field
from typing import Optional


class CreateReview(BaseModel):
    content: str = Field(...,examples = ['A captivating story with deep symbolism.'])
    rating: int = Field(...,examples = [4])

class ReviewResponse(BaseModel):
    id: str = Field(...,examples=['6769be7156ca61f944fa3f90'])
    book_id:  str = Field(...,examples=['6769be7156ca61f944fa3f90'])
    content: str = Field(...,examples = ['A captivating story with deep symbolism.'])
    rating: int = Field(...,examples = [4])

class UpdateReview(BaseModel):
    content: Optional[str] = Field(None,examples = ['A captivating story with deep symbolism.'])
    rating: Optional[int] = Field(None,examples = [4])