from pydantic import BaseModel, EmailStr
from typing import List

class User(BaseModel):
    name: str
    email: EmailStr
    gender: str
    age: int
    favorite_books: List[str]

# from datetime import datetime
# from typing import List, Optional
# from pydantic import BaseModel, EmailStr

# class UserModel(BaseModel):
#     id: str
#     created_at: datetime
#     updated_at: datetime
#     name: str
#     email: EmailStr
#     gender: str
#     phone_number: str
#     age: int
#     favorite_books: Optional[List[dict]] = []
#     total_reviews: int
