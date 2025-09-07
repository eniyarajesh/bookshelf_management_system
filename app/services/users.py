from bson.objectid import ObjectId
from bson.errors import InvalidId
from motor.motor_asyncio import AsyncIOMotorDatabase
from fastapi import HTTPException, status
from app.models.users import User
from app.schemas.users import CreateUser, UpdateUser, UserDetails
from app.services import BaseService


class UserService(BaseService):
    def __init__(self, db:AsyncIOMotorDatabase):
        super().__init__(db)
        self.collection = db['users']
    
    async def create_user(self, user_data:CreateUser):
        user = user_data.dict()
        string_id = str(ObjectId())
        user['_id'] = string_id
        await self.collection.insert_one(user)
        user = await self.collection.find_one({'_id':string_id})
        return self._to_response(user,UserDetails)
    
    async def get_user(self, user_id: str):
        try:
            user = await self.collection.find_one({'_id': str(ObjectId(user_id))})
        except InvalidId:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid ObjectId")
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        return self._to_response(user, UserDetails)
    
    async def update_user(self, user_id: str, update_data: UpdateUser):
        try:
            result = await self.collection.update_one({'_id': str(ObjectId(user_id))},
                                                      {'$set': update_data.dict(exclude_unset=True)})
        except InvalidId:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid ObjectId")
        if result.matched_count == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        user = await self.collection.find_one({'_id': str(ObjectId(user_id))})
        return self._to_response(user, UserDetails)
    
    async def delete_user(self, user_id: str):
        try:
            result = await self.collection.delete_one({'_id': str(ObjectId(user_id))})
            if result.deleted_count == 0:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        except InvalidId:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid UserID")
        
    async def get_users(self):
        users = await self.collection.find().to_list(None)
        return [self._to_response(user, UserDetails) for user in users]
