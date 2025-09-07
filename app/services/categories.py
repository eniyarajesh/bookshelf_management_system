from bson.objectid import ObjectId
from bson.errors import InvalidId
from motor.motor_asyncio import AsyncIOMotorDatabase
from fastapi import HTTPException, status
from app.models.categories import Category
from app.schemas.categories import CategoryResponse, CreateCategory, UpdateCategory
from app.services import BaseService


class CategoryService(BaseService):
    def __init__(self, db:AsyncIOMotorDatabase):
        super().__init__(db)
        self.collection = db['categories']
    
    async def create_category(self,category_data:CreateCategory):
        category = Category(**category_data.dict())
        result = await self.collection.insert_one(category.dict())
        cat = await self.collection.find_one({"_id":result.inserted_id})
        return self._to_response(cat,CategoryResponse)
    
    async def get_categories(self):
        try:
            categories = await self.collection.find().to_list(length=None)
        except InvalidId:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid ObjectId")
        if not categories:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
        return [self._to_response(category, CategoryResponse) for category in categories]
    
    async def update_category(self,category_id:str,update_cat:UpdateCategory):
        try:
            update  = await self.collection.update_one({"_id": ObjectId(category_id)},
                                                       {"$set":update_cat.dict(exclude_unset = True)})
        except InvalidId:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid ObjectId")
        
        if update.matched_count == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
        
        updated = await self.collection.find_one({'_id':ObjectId(category_id)})
        return self._to_response(updated,CategoryResponse)
    
    async def delete_category(self,category_id:str):
        try:
            result = await self.collection.delete_one({"_id":ObjectId(category_id)})
            if result.deleted_count == 0:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
            else:
                return f"Review with id {category_id} deleted successfully!!!!"
        except InvalidId:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid ReviewID")   
    
    
            
