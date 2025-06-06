from fastapi.routing import APIRouter
from fastapi import Depends, HTTPException
from storage import queryset 
from storage.database import get_db
# from sqlalchemy.orm import Session
from models import event_register 
from schemas.event_schema import RegisterEvent, ResponseEvent

from sqlalchemy.ext.asyncio import AsyncSession


router = APIRouter(tags=['Event Controls'])



@router.get("/events",response_model=list[ResponseEvent])
async def get_all_events(db:AsyncSession = Depends(get_db)):
    data = await queryset.get_all_events(db)
    if data:
        return data
    else:
        raise HTTPException(status_code=400,detail="Something went wrong !")

# @router.get("/events", response_model=list[ResponseEvent])
# async def get_all_events(
#     page: int = 1,
#     page_limit: int = 10,
#     db: AsyncSession = Depends(get_db)):

#     if page < 1 or page_limit < 1:
#         raise HTTPException(status_code=400, detail="Page and page_limit must be >= 1")
    
#     data = await queryset.get_all_events(db, page=page, page_limit=page_limit)
#     if data:
#         return data
#     else:
#         raise HTTPException(status_code=400, detail="Something went wrong!")




@router.post("/events",response_model=ResponseEvent)
async def create_events(request:RegisterEvent,db:AsyncSession = Depends(get_db)):
    duplicate = await queryset.Duplicate_check(db,request)
    if duplicate:
        raise HTTPException(status_code=400,detail="Duplicate Entry")
    
    data = await queryset.post_event(db,request)
    if data:
        return data
    else:
        raise HTTPException(status_code=400,detail="Something went wrong !")
    

