from pydantic import BaseModel,EmailStr
from typing import Optional
from datetime import datetime
class CreateContact(BaseModel):
    name:str
    email:EmailStr
    phone:str
    address:Optional[str]=None

class UpdateContact(BaseModel):
    name:Optional[str]=None
    email:Optional[EmailStr]=None
    phone:Optional[str]=None
    address:Optional[str]=None

class ContactResponse(BaseModel):
    id:int
    name:str
    email:str
    phone:str
    address:Optional[str]=None
    created_at:datetime

    class Config:
        from_attributes=True