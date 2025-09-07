from pydantic import BaseModel, Field


class Book(BaseModel):
    name: str
    description: str
    average_rating: str
    total_reviews: str
