from bson.objectid import ObjectId
from bson.errors import InvalidId
from motor.motor_asyncio import AsyncIOMotorDatabase
from fastapi import HTTPException, status
from datetime import datetime
from app2.models.author import author
from app2.schemas.author import CreateAuthor, UpdateAuthor, ResponseAuthor
from app2.services import BaseService


class AuthorService(BaseService):
    def __init__(self, db: AsyncIOMotorDatabase):
        super().__init__(db)
        self.collection = db['author']


    async def get_authors(self):
        results = await self.collection.find().to_list(None)
        authors = []
        for res in results:
            authors.append(self._to_response(res, ResponseAuthor))
        return authors

    async def create_author(self, author_data: CreateAuthor):
        author_dict = author_data.model_dump()
        author_dict["_id"] = str(ObjectId())
        author_dict["created_at"] = author_dict["updated_at"] = datetime.utcnow()
        # author_dict["_id"] = str(ObjectId())
        author_dict["total_reviews"] = 10
        result = await self.collection.insert_one(author_dict)
        author = await self.collection.find_one({'_id': result.inserted_id})
        # existing_author = await self.collection.find_one({'_id': author_dict['isbn']})
        # if existing_author:
        #     raise HTTPException( status_code=status.HTTP_400_BAD_REQUEST, detail=f"author with ISBN {author_dict['isbn']} already exists" )
        return self._to_response(author, ResponseAuthor)
    
    async def get_author(self, author_id: str):
        try:
            result = await self.collection.find_one({'_id': author_id})
        except InvalidId:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid ObjectId")
        if not result:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="author not found")
        return self._to_response(result, ResponseAuthor)
    

    async def update_authors(self, author_id: str, update_data: UpdateAuthor):
        try:
            result = await self.collection.update_one({'_id': author_id},
                                                      {'$set': update_data.dict(exclude_unset=True)})
        except InvalidId:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid ObjectId")
        if result.matched_count == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="author not found")
        result = await self.collection.find_one({'_id': author_id})
        return self._to_response(result, ResponseAuthor)


    async def delete_author(self, author_id: str):
        try:
            result = await self.collection.delete_one({'_id': author_id})
            if result.deleted_count == 0:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="author not found")
        except InvalidId:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid ObjectId")
        return {f"{author_id} is sussussfully deleted"}
    