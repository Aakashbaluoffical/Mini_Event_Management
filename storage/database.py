from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker,declarative_base
from configuration.connections import POSTGRESDB


POSTGRESDB = POSTGRESDB()


DATABASE_URL = f"postgresql+asyncpg://{POSTGRESDB.POSTGRES_USERNAME}:{POSTGRESDB.PASSWORD}@{POSTGRESDB.HOST}/{POSTGRESDB.SCHEMA}"

engine = create_async_engine(DATABASE_URL,pool_size=50,max_overflow=100,pool_recycle=600,echo=True)

AsyncSessionLocal = sessionmaker(bind=engine,class_=AsyncSession, expire_on_commit =False)

base = declarative_base()
print("DATABASE_URL",DATABASE_URL)





async def get_db():
    async with AsyncSessionLocal() as session:
        yield session