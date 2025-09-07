from pydantic import BaseModel, Field


class BaseSchema(BaseModel):
    id: str = Field(..., alias="_id")  # Accepts _id from Mongo

    class Config:
        populate_by_name = True  # ✅ Allows using `id` in your code, even if input has `_id`
        arbitrary_types_allowed = True
    
class BasicSchema(BaseModel):
    id: str = Field(..., example=["6683f946ec61bfa6a3c2d7c7"])
    name: str = Field(..., example=["Harry Porter Chambers of secrets (VOLUME 1)"])