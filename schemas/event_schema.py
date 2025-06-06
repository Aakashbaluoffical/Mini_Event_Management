from pydantic import BaseModel,Field
from datetime import datetime

class RegisterEvent(BaseModel):
   
    name :str
    location :str
    start_time : datetime = Field(description="Format: YYYY-MM-DD HH:MM:SS")
    end_time : datetime = Field(description="Format: YYYY-MM-DD HH:MM:SS")
    max_capacity :int  = Field(gt=0, description="Max Capacity must be greater than zero")  # Ensures value > 0
    
   
    
   
class ResponseEvent(BaseModel):
    
    Event_id: int = Field(..., alias="id")
    Event_name: str = Field(..., alias="name")
    Event_location: str = Field(..., alias="location")
    Event_start_time:  datetime  = Field(..., alias="start_time")
    Event_end_time:  datetime  = Field(..., alias="end_time")
    max_capacity:int
    is_active:bool


        
    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        # from_attributes = True                  # replaces orm_mode
        # validate_by_name = True    
