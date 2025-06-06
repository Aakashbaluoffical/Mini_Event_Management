from storage.database import base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Float, Integer, String, Boolean, ForeignKey


class EventRegister(base):
    __tablename__ = "event_register_tbl"
    id = Column(Integer, primary_key=True,index= True)
    status = Column(String, default="not_started",index=True)
    is_active = Column(Boolean, index=True)

    user_id = Column(Integer,ForeignKey("user_tbl.id"), index = True)
    event_id = Column(Integer,ForeignKey("event_tbl.id"), index = True)

    user = relationship("User",back_populates = 'registation')
    event = relationship("EventModel",back_populates = 'registation' )

