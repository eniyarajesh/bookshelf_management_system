from pydantic import BaseModel

class author(BaseModel):
    name: str
    age: int
    gender: str
    total_published: int
    

    