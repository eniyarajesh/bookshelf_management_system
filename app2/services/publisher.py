from bson.objectid import ObjectId
from bson.errors import InvalidId
from motor.motor_asyncio import AsyncIOMotorDatabase

from fastapi import HTTPException, status
from app2.models.publisher import Publisher
from app2.schemas.publisher import CreatePublisher, UpdatePublisher, ResponsePublisher
from app2.services import BaseService

class PublisherService(BaseService):
    def __init__(self, db: AsyncIOMotorDatabase):
        super().__init__(db)
        self.collection = db['publisher']

    async def get_publishers(self):
        results = await self.collection.find().to_list(None)
        publishers = []
        for res in results:
            publishers.append(self._to_response(res, ResponsePublisher))
        return publishers
        # return [self._to_response(res, ResponsePublisher) for res in results]


    async def create_publisher(self, publisher_data: CreatePublisher):
        publisher_dict = publisher_data.model_dump()
        publisher_dict["_id"] = str(ObjectId())
        
        result = await self.collection.insert_one(publisher_dict)
        publisher = await self.collection.find_one({'_id': result.inserted_id})
        return self._to_response(publisher, ResponsePublisher)

   
    async def get_publisher(self, publisher_id: str):
        try:
            result = await self.collection.find_one({'_id': publisher_id})
        except InvalidId:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid ObjectId")
        if not result:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Publisher not found")
        return self._to_response(result, ResponsePublisher)
    

    async def update_publisher(self, publisher_id: str, update_data: UpdatePublisher):
        try:
            result = await self.collection.update_one({'_id': publisher_id},
                                                      {'$set': update_data.dict(exclude_unset=True)})
        except InvalidId:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid ObjectId")
        if result.matched_count == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
        result = await self.collection.find_one({'_id': publisher_id})
        return self._to_response(result, ResponsePublisher)


    async def delete_publisher(self, publisher_id: str):
        try:
            result = await self.collection.delete_one({'_id': publisher_id})
            # logger.info(f"Request path: {request.url.path}")
            if result.deleted_count == 0:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Publisher not found")
        except InvalidId:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid ObjectId")
        return {f"{publisher_id} is sussussfully deleted"}
    
