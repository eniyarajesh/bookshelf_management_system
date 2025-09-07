from bson.objectid import ObjectId
from bson.errors import InvalidId
from motor.motor_asyncio import AsyncIOMotorDatabase

from fastapi import HTTPException, status
from app2.models.bookstore import bookstore
from app2.schemas.bookstore import CreateBookstore, UpdateBookstore, ResponseBookstore
from app2.services import BaseService

class BookstoreService(BaseService):
    def __init__(self, db: AsyncIOMotorDatabase):
        super().__init__(db)
        self.collection = db['bookstore']

    async def get_bookstores(self):
        results = await self.collection.find().to_list(None)
        bookstore = []
        for res in results:
            bookstore.append(self._to_response(res, ResponseBookstore))
        return bookstore
        # return [self._to_response(res, ResponseBookstore) for res in results]


    async def create_bookstore(self, bookstore_data: CreateBookstore):
        bookstore_dict = bookstore_data.model_dump()
        bookstore_dict["_id"] = str(ObjectId())
        result = await self.collection.insert_one(bookstore_dict)
        bookstored = await self.collection.find_one({'_id': result.inserted_id})
        return self._to_response(bookstored, ResponseBookstore)
    
   
    async def get_bookstore(self, bookstore_id: str):
        try:
            result = await self.collection.find_one({'_id': bookstore_id})
        except InvalidId:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid ObjectId")
        if not result:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
        return self._to_response(result, ResponseBookstore)
    
    

    async def update_bookstore(self, bookstore_id: str, update_data: UpdateBookstore):
        try:
            result = await self.collection.update_one({'_id': bookstore_id},
                                                      {'$set': update_data.dict(exclude_unset=True)})
        except InvalidId:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid ObjectId")
        if result.matched_count == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
        result = await self.collection.find_one({'_id': bookstore_id})
        return self._to_response(result, ResponseBookstore)


    async def delete_bookstore(self, bookstore_id: str):
        try:
            result = await self.collection.delete_one({'_id': bookstore_id})
            if result.deleted_count == 0:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
        except InvalidId:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid ObjectId")
        return {f"{bookstore_id} is sussussfully deleted"}
    
