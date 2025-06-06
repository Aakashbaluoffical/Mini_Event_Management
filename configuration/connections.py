from dotenv import load_dotenv
from pydantic_settings import BaseSettings
import os

load_dotenv()




class POSTGRESDB(BaseSettings):
    POSTGRES_USERNAME:str = os.environ["POSTGRES_USERNAME"]
    PASSWORD :str = os.environ["POSTGRES_PASSWORD"]
    HOST:str = os.environ["POSTGRES_HOST"]
    SCHEMA:str = os.environ["POSTGRES_SCHEMA"]


