from pydantic import BaseModel, Field, validator


class Book(BaseModel):
    title: str
    author: str
    isbn: str = Field(..., pattern=r"^\d{13}$")
    publisher: str
    year_published: int
    copies_available: int

    @validator('isbn')
    def check_isbn_length(cls, v):
        if len(v) != 13:
            raise ValueError('ISBN must be exactly 13 digits.')
        return v