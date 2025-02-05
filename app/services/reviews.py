from bson.objectid import ObjectId
from bson.errors import InvalidId
from motor.motor_asyncio import AsyncIOMotorDatabase
from fastapi import HTTPException, status
from app.services import BaseService
from motor.motor_asyncio import AsyncIOMotorDatabase
from app.models.reviews import Review
from app.schemas.reviews import ReviewResponse, WriteReview, UpdatReview
from typing import List


class ReviewService(BaseService):
    def __init__(self, db:AsyncIOMotorDatabase):
        super().__init__(db)
        self.collection = db['reviews']
    
    async def write_review(self,user_review:WriteReview):
        review = Review(**user_review.dict())
        result = await self.collection.insert_one(review.dict())
        review = await self.collection.find_one({'_id':result.inserted_id})
        return self._to_response(review,ReviewResponse)
    
    async def get_reviews(self, book_id: str):
        try:
            reviews = await self.collection.find({'book_id': book_id}).to_list(length=None)
        except InvalidId:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid ObjectId")
        if not reviews:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No reviews for the selected book.")
        return [self._to_response(review, ReviewResponse) for review in reviews]
    
    async def update_review(self,review_id:str,update_review:UpdatReview):
        try:
            review = await self.collection.update_one({'_id':ObjectId(review_id)},
                                                      {"$set":update_review.dict(exclude_unset = True)})
        
        except InvalidId:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid ObjectId")
        
        if review.matched_count == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Review not found")
        
        review_ = await self.collection.find_one({'_id': ObjectId(review_id)})

        return self._to_response(review_,ReviewResponse)
    
    async def delete_review(self, review_id: str):
        try:
            result = await self.collection.delete_one({'_id': ObjectId(review_id)})
            if result.deleted_count == 0:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
            else:
                return f"Review with id {review_id} is successfully deleted!!"
        except InvalidId:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid UserID")
        
    

    

        
    



    
