from fastapi import FastAPI,Depends
from routes import events_tracking, events_management , login
import uvicorn 
from storage.database import get_db
from sqlalchemy.orm import Session

app = FastAPI(title='Mini Event Management API',description='FastAPI and PostgreSQL',version='0.1')




#===============================================
#            Automatic Model base Tbl Creation
#================================================
# event_model.base.metadata.create_all(bind=engine)
# event_register.base.metadata.create_all(bind=engine)
# user_model.base.metadata.create_all(bind=engine)



#===================================
#            API Routings
#===================================
app.include_router(events_management.router,prefix='/api/v1')
app.include_router(events_tracking.router,prefix='/api/v1')
app.include_router(login.router,prefix='/api/v1')




@app.get("/")
def index(db:Session = Depends(get_db)):
    return {"data":"Welcome to Mini Event Management"}


#===================================
#            Staring Point
#===================================

if __name__ == "__main__":
    print("Start Project")
    # uvicorn.run(app,host="localhost",port='5200')