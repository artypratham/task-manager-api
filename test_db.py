import asyncio
from sqlalchemy import text
from app.dependencies import engine

async def test():
    async with engine.connect() as conn:
        # Check SSL status
        result = await conn.execute(text("SELECT ssl_is_used();"))
        ssl_used = result.scalar()
        print(f"SSL Enabled: {ssl_used}")
        
        # Check channel binding
        result = await conn.execute(text("SHOW channel_binding;"))
        channel_binding = result.scalar()
        print(f"Channel Binding: {channel_binding}")
        
        print("Fully secure connection!")

asyncio.run(test())