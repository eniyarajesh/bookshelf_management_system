from bson.objectid import ObjectId
from bson.errors import InvalidId
from motor.motor_asyncio import AsyncIOMotorDatabase
from fastapi import HTTPException, status
from app.services import BaseService
from motor.motor_asyncio import AsyncIOMotorDatabase
from app.models.reviews import Review
from app.schemas.reviews import ReviewResponse, CreateReview,UpdateReview
from typing import List


class ReviewService(BaseService):
    def __init__(self, db:AsyncIOMotorDatabase):
        super().__init__(db)
        self.collection = db['reviews']
    
    async def create_review(self, book_id: str, user_review: CreateReview):
        book_exists = await self.db['books'].find_one({"_id": book_id})
        if not book_exists:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
        review = user_review.dict()
        string_id = str(ObjectId())
        review['_id'] = string_id
        review['book_id'] = book_id
        await self.collection.insert_one(review)
        review = await self.collection.find_one({'_id':string_id})
        return self._to_response(review,ReviewResponse)
    
    async def get_reviews(self, book_id: str):
        try:
            reviews = await self.collection.find({'book_id': book_id}).to_list(length=None)
        except InvalidId:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid ObjectId")
        if not reviews:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No reviews for the selected book.")
        return [self._to_response(review, ReviewResponse) for review in reviews]
    
    async def update_review(self,book_id:str,review_id:str,update_review:UpdateReview):
        try:
            book_exists = await self.db['books'].find_one({"_id": book_id})
            if not book_exists:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
            
            review_exists = await self.collection.find_one({"_id": review_id, "book_id": book_id})
            if not review_exists:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Review not found for the specified book")
        

            update_fields = {}
            if update_review.content is not None:
                update_fields['content'] = update_review.content
            if update_review.rating is not None:
                update_fields['rating'] = update_review.rating
            if not update_fields:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No valid fields to update")

            # Step 5: Perform the update
            result = await self.collection.update_one(
                {"_id": review_id, "book_id": book_id},
                {"$set": update_fields}
            )

            if result.modified_count == 0:
                raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Failed to update review")

            # Step 5: Return updated review
            updated_review = await self.collection.find_one({"_id": review_id})
            return self._to_response(updated_review, ReviewResponse)

        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")
        
    async def delete_review(self, review_id: str):
        try:
            result = await self.collection.delete_one({'_id': str(ObjectId(review_id))})
            if result.deleted_count == 0:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
            else:
                return f"Review with id {review_id} is successfully deleted!!"
        except InvalidId:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid UserID")
        
    async def get_review(self):
        reviews = await self.collection.find().to_list(None)
        return [self._to_response(review, ReviewResponse) for review in reviews]
        
    



    
