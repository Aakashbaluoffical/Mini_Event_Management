from storage.database import base
from sqlalchemy import Integer, String,DateTime, Boolean, Column, ForeignKey
from sqlalchemy.orm import relationship



class EventModel(base):
    __tablename__ = "event_tbl"
    id = Column(Integer, primary_key=True,index= True)
    name = Column(String,index= True)
    location = Column(String,index= True)
    start_time = Column(DateTime(timezone=True))  
    end_time = Column(DateTime(timezone=True))  
    max_capacity = Column(Integer,index= True)
    is_active = Column(Boolean,index= True)
    
    registation = relationship("EventRegister",back_populates='event')



