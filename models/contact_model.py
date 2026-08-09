from core.database import Base
from sqlalchemy import Column,String,Integer,DateTime
from datetime import datetime

class Contact(Base):
    __tablename__="contacts"
    id=Column(Integer,primary_key=True)
    name=Column(String,nullable=False,index=True)
    email=Column(String,nullable=False,unique=True)
    phone=Column(String,nullable=False,unique=True)
    address=Column(String,nullable=True)
    created_at=Column(DateTime,default=datetime.now)
