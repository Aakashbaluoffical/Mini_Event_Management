from storage.database import base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Float, Integer, String, Boolean, ForeignKey


class User(base):
    __tablename__ = "user_tbl"
    id = Column(Integer, primary_key=True,index= True)
    username = Column(String, index=True, unique=True)
    password = Column(String, index=True)
    email = Column(String,index=True,unique= True)
    is_active = Column(Boolean,index=True,default=True)
    is_superuser = Column(Boolean,index=True,default=False)
    

    registation = relationship("EventRegister",back_populates='user')