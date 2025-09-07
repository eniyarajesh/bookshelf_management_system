import os
from motor.motor_asyncio import AsyncIOMotorClient


async def get_database():
    # mongo_url = os.getenv('MONGO_URL')
    client = AsyncIOMotorClient('mongodb://localhost:27017')
    db = client['<DB_Collection_name>']
    yield db
    client.close()
    