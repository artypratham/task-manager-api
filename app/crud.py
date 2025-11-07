from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update , delete
from .models import Task
from .schemas import TaskCreate, TaskUpdate

async def create_task(db: AsyncSession, task: TaskCreate):
    db_task = Task(**task.model_dump())
    db.add(db_task)
    await db.commit()
    await db.refresh(db_task)
    return db_task

async def get_task(db: AsyncSession, task_id: int):
    result = await db.execute(select(Task).where(Task.id == task_id))
    return result.scalar_one_or_none()

async def get_tasks(db: AsyncSession, skip: int = 0, limit: int = 100):
    result = await db.execute(select(Task).offset(skip).limit(limit))
    return result.scalars().all()

async def update_task(db: AsyncSession, task_id: int, task_update: TaskUpdate):
    data = task_update.model_dump(exclude_unset=True)
    if not data:
        return None
    result = await db.execute(
        update(Task).where(Task.id == task_id).values(**data).returning(Task)
    )
    await db.commit()
    return result.scalar_one_or_none()

async def delete_task(db: AsyncSession, task_id: int):
    result = await db.execute(delete(Task).where(Task.id == task_id).returning(Task.id))
    await db.commit()
    return result.scalar_one() is not None


   
    
    
    
    
    
    
    
    
    
    
    
    
    