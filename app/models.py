from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Task(Base):
    __tablename__ = "tasks"
    
    id = Column(Integer, primary_key = True, index = True)
    title = Column(String,index = True, nullable = False)
    description = Column(String, nullable = True)
    created_at = Column(DateTime(timezone = True), server_default = func.now())
    updated_at = Column(DateTime(timezone = True),)   
    