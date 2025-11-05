from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str
    secret_key: str

    class Config:
        env_file = '.env'

#Load Settings
settings = Settings()

#Create async engine
engine = create_async_engine(settings.database_url, echo=True)

#Session factory
AsyncSessionLocal = sessionmaker(engine, class_ =AsyncSession, expire_on_commit = False)

#Dependency to get DB session
async def get_db() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session



























