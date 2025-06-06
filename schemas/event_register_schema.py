from pydantic import BaseModel, Field
from datetime import datetime


class RegisterEventValidation(BaseModel):
    user_id: int 
    event_id :int    
   
class ResponseEventRegister(BaseModel):
    user_id : int = Field(..., alias="user_id")
    User_Email:str = Field(..., alias="email")
    Event_id:int = Field(..., alias="event_id")
    Event_name : str = Field(..., alias="event_name")
    Event_location :str = Field(..., alias="location")
    Event_start_time:datetime = Field(..., alias="start_time")
    Event_end_time:datetime = Field(..., alias="end_time")
    Event_status:str = Field(..., alias="status")
    is_active:bool 




    class Config:
        orm_mode = True
        # from_attributes = True                  # replaces orm_mode
        # validate_by_name = True    