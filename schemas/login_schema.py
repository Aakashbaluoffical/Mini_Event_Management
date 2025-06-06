from pydantic import BaseModel, validator




class RegisterUser(BaseModel):
    username:str 
    password:str 
    email:str 

    @validator('password')
    def password_length(cls, v):
        if len(v) <= 8:
            raise ValueError('Password must be longer than 8 characters')
        return v

    @validator('username', 'email')
    def must_have_gmail_and_length(cls, v):
        if '@gmail' not in v or len(v) < 5:
            raise ValueError('Must contain "@gmail" and be at least 5 characters long')
        return v
    
class ResponseUser(BaseModel):
    id:int
    email:str
    is_active:bool




class ValidateUser(BaseModel):
    username:str
    password:str

    @validator('username')
    def must_have_gmail_and_length(cls, v):
        if '@gmail' not in v or len(v) < 5:
            raise ValueError('Must contain "@gmail" and be at least 5 characters long')
        return v