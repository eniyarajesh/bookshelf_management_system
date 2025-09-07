from bson import ObjectId
from bson.errors import InvalidId
from fastapi import HTTPException, status
from motor.motor_asyncio import AsyncIOMotorDatabase
from datetime import datetime
from app2.schemas.base_schema import BaseSchema, BasicSchema
from app2.schemas.user import CreateUser, UpdateUser, ResponseUser
from app2.services import BaseService

class UserService(BaseService):
    def __init__(self, db: AsyncIOMotorDatabase):
        super().__init__(db)
        self.collection = db['users']

    async def get_users(self):
        results = await self.collection.find().to_list(None)
        users = []
        for res in results:
            users.append(self._to_response(res,ResponseUser))
        return users

    async def create_user(self, user_data: CreateUser):
        user_dict = user_data.model_dump()
        user_dict["created_at"] = user_dict["updated_at"] = datetime.utcnow()
        user_dict["_id"] = str(ObjectId())
        user_dict["total_reviews"] = 10

        result = await self.collection.insert_one(user_dict)
        user = await self.collection.find_one({"_id": result.inserted_id})
        return self._to_response(user, ResponseUser)
    
    async def get_user(self, user_id: str):
        try:
            result = await self.collection.find_one({'_id': user_id})
        except InvalidId:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid ObjectId")
        if not result:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        return self._to_response(result, ResponseUser)

    async def update_user(self, user_id: str, update_data: UpdateUser):
        try:
            result = await self.collection.update_one({'_id': user_id},
                                                      {'$set': update_data.dict(exclude_unset=True)})
        except InvalidId:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid ObjectId")
        if result.matched_count == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
        result = await self.collection.find_one({'_id': user_id})
        return self._to_response(result, ResponseUser)

    async def delete_user(self, user_id: str):
        try:
            result = await self.collection.delete_one({'_id': user_id})
            if result.deleted_count == 0:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        except InvalidId:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid ObjectId")
        return {f"{user_id} successfully deleted"}


