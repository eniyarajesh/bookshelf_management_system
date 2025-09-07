from bson.objectid import ObjectId
from bson.errors import InvalidId
from motor.motor_asyncio import AsyncIOMotorDatabase

from fastapi import HTTPException, status
from app2.models.category import Category
from app2.schemas.category import CreateCategory, UpdateCategory, ResponseCategory
from app2.services import BaseService

class CategoryService(BaseService):
    def __init__(self, db: AsyncIOMotorDatabase):
        super().__init__(db)
        self.collection = db['category']

    async def get_categories(self):
        results = await self.collection.find().to_list(None)
        Categories = []
        for res in results:
            Categories.append(self._to_response(res, ResponseCategory))
        return Categories

    async def create_category(self, category_data: CreateCategory):
        category_dict = category_data.model_dump()
        category_dict["_id"] = str(ObjectId())
        result = await self.collection.insert_one(category_dict)
        category = await self.collection.find_one({'_id': result.inserted_id})
        return self._to_response(category, ResponseCategory)

   
    async def get_category(self, category_id: str):
        try:
            result = await self.collection.find_one({'_id': category_id})
        except InvalidId:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid ObjectId")
        if not result:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
        return self._to_response(result, ResponseCategory)
    

    async def update_category(self, category_id: str, update_data: UpdateCategory):
        try:
            result = await self.collection.update_one({'_id': category_id},
                                                      {'$set': update_data.dict(exclude_unset=True)})
        except InvalidId:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid ObjectId")
        if result.matched_count == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
        result = await self.collection.find_one({'_id': category_id})
        return self._to_response(result, ResponseCategory)


    async def delete_category(self, category_id: str):
        try:
            result = await self.collection.delete_one({'_id': category_id})
            if result.deleted_count == 0:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
        except InvalidId:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid ObjectId")
        return {f"{category_id} is sussussfully deleted"}
    
