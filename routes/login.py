from fastapi.routing import APIRouter
from fastapi import Depends, HTTPException 
from storage import queryset 
from storage.database import get_db
# from sqlalchemy.orm import Session
from models import event_register 
from schemas.login_schema import RegisterUser, ResponseUser , ValidateUser
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession


router = APIRouter(tags=['Login'])


@router.post("/login",response_model=list[ResponseUser])
async def login_user(request:ValidateUser,db:AsyncSession = Depends(get_db)):
    user = await queryset.is_validated(db, request)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return user
    



@router.post("/register",response_model=ResponseUser)
async def create_user(request:RegisterUser,db:AsyncSession = Depends(get_db)):
     
    duplicate = await queryset.Duplicate_User(db,request)
    if duplicate:
        raise HTTPException(status_code=400,detail="User already existed !")
    
    data = await queryset.create_user(db,request)
    if data:
        return JSONResponse(status_code=201, content={"message": "User created successfully"})
    else:
        raise HTTPException(status_code=400,detail="Something went wrong !")