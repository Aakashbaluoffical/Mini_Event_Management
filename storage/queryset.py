from models.event_model import EventModel 
from models.user_model import User
from models.event_register import EventRegister
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update
from sqlalchemy import and_



#===================================
#            Event Tracking
#===================================
async def get_booking(db,event_id):
    stmt = (
        select(
            User.id.label("user_id"),
            User.email,
            EventModel.id.label("event_id"),
            EventModel.name.label("event_name"),
            EventModel.location,
            EventModel.start_time,
            EventModel.end_time,
            EventRegister.status,
            EventRegister.is_active
        )
        .select_from(EventRegister)
        .join(EventModel, EventRegister.event_id == EventModel.id, isouter=True)
        .join(User, EventRegister.user_id == User.id, isouter=True)
        .where(EventRegister.is_active == True,EventModel.id==event_id)
    )

    result = await db.execute(stmt)
    columns = result.keys()
    rows = result.all()
    items = [dict(zip(columns, row)) for row in rows]
    return items





async def post_event_registration(db,data):
    data = EventRegister(**data.dict(),status = 'not_started', is_active = True)
    db.add(data)
    await db.commit()
    await db.refresh(data)
    
 
    stmt = (
        update(EventModel)
        .where(EventModel.id == data.event_id)
        .values(max_capacity=EventModel.max_capacity - 1) 
        .execution_options(synchronize_session="fetch")
    )

    await db.execute(stmt)
    await db.commit()
    return data



   
async def check_event_active(db,event_id):
    stmt = select(EventModel).where(
        and_(
            EventModel.id == event_id,
            EventModel.is_active == True,
            EventModel.max_capacity > 0
        )
    )
    result = await db.execute(stmt)
    items = result.scalars().all()
    return items


async def check_duplicate(db,data):
    stmt = select(EventModel).where(
        and_(
            EventRegister.event_id == data.event_id,
            EventRegister.user_id == data.user_id,
        )
    )
    result = await db.execute(stmt)
    items = result.scalars().all()
    return items




#===================================
#            Event Management
#===================================

async def post_event(db,data):
    data = EventModel(**data.dict(), is_active = True)
    db.add(data)
    await db.commit()
    await db.refresh(data)
    return data


async def Duplicate_check(db,data):
    
    stmt = select(EventModel).where(
        and_(
            EventModel.name == data.name,
            EventModel.location == data.location,
            EventModel.start_time == data.start_time,
            EventModel.end_time == data.end_time,
            EventModel.is_active == True,
        )
    )
    result = await db.execute(stmt)
    items = result.scalars().all()
    return items



async def get_all_events(db):
    stmt = select(EventModel).where(EventModel.is_active == True,EventModel.max_capacity>0)
    result = await db.execute(stmt)
    items = result.scalars().all()
    return items

# async def get_all_events(db: AsyncSession, page: int, page_limit: int):
#     offset = (page - 1) * page_limit
#     stmt = (
#         select(EventModel)
#         .where(EventModel.is_active == True, EventModel.max_capacity > 0)
#         .offset(offset)
#         .limit(page_limit)
#     )
#     result = await db.execute(stmt)
#     items = result.scalars().all()
#     return items



#===================================
#            Logins
#===================================


async def is_validated(db: AsyncSession, data):
    stmt = select(User).where(
        and_(
            User.username == data.username,
            User.password == data.password,
            User.is_active == True
        )
    )
    result = await db.execute(stmt)
    user = result.scalars().all()  
    return user


async def create_user(db,data):
   
    data = User(**data.dict(), is_active = True)
    db.add(data)
    await db.commit()
    await db.refresh(data)
    return data



async def Duplicate_User(db,data):
    stmt = select(User).where(
        and_(
                User.username == data.username,
                User.is_active == True
        )
    )
    result = await db.execute(stmt)
    username = result.scalars().all()



    stmt = select(User).where(
        and_(
                User.username == data.email,
                User.is_active == True
        )
    )
    result = await db.execute(stmt)
    email = result.scalars().all()
    if any([username,email]):
        return True
    
    return False