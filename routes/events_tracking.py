from fastapi.routing import APIRouter, HTTPException , Response
from fastapi.responses import JSONResponse
from fastapi import Depends
from storage import queryset 
from storage.database import get_db
from schemas.event_register_schema import  ResponseEventRegister , RegisterEventValidation
from sqlalchemy.ext.asyncio import AsyncSession




router = APIRouter(tags=['Event Actions'])


@router.get("/events/{event_id}/attendees",response_model=list[ResponseEventRegister])
async def get_all_booked_events(event_id:int = None,db:AsyncSession = Depends(get_db)):
    if event_id is None:
        raise HTTPException(status_code= 400, detail=f"Event_id is {event_id}")
     
    data = await queryset.get_booking(db,event_id)
    
    if data:
        return data
    else:
        raise HTTPException(status_code=404, detail="No attendees found")
   


@router.post("events/{event_id}/register",)
async def book_events(request:RegisterEventValidation,event_id:int=None, db:AsyncSession = Depends(get_db)):
    if event_id is None:
        raise HTTPException(status_code= 400, detail=f"Event_id is {event_id}")
    
    
    event = await queryset.check_event_active(db,event_id)
    if not event:
        raise HTTPException(status_code= 400, detail=" Event is full. Maximum capacity reached or Event is inactive")
    
    event = await queryset.check_duplicate(db,request)
    if event:
        raise HTTPException(status_code= 400, detail="Event already booked")
    

    data = await queryset.post_event_registration(db,request)
    if data:
        return Response(content="Registation sucessfull", status_code=200)
    else:
        raise HTTPException(status_code= 400, detail="Event is Full")

   