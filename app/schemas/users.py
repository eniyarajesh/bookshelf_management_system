from pydantic import BaseModel, Field
from typing import Optional, List


class CreateUser(BaseModel):
    username: str  = Field(...,examples = ['udayreddy_26'])
    email: str = Field(..., examples = ["uday@zysec.ai"])
    full_name :str = Field(...,examples=["uday kiran reddy"])
    password: str = Field(...,examples = ['strongpassword123'])
    
class UserDetails(BaseModel):
    id : str = Field(...,examples = ['6769be7156ca61f944fa3f90'])
    username : str = Field(..., examples = ['udayreddy_26'])
    email : str = Field(...,examples = ['uday@zysec.ai'])
    full_name : str = Field(...,examples = ['uday kiran reddy'])

class UpdateUser(BaseModel):
    username: Optional[str] = Field(None, example='udayreddy_26')
    email: Optional[str] = Field(None, example="uday@zysec.ai")
    full_name: Optional[str] = Field(None, example="uday kiran reddy")
    password: Optional[str] = Field(None, example='strongpassword123')






