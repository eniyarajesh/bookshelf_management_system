from fastapi import APIRouter, Depends, HTTPException, Request, status, Query
from motor.motor_asyncio import AsyncIOMotorDatabase
from typing import List
import logging
from app.schemas.reviews import CreateReview, ReviewResponse, UpdateReview
from app.database import get_database
from app.services.reviews import ReviewService


router = APIRouter(prefix='', tags=['reviews'])
logger = logging.getLogger(__name__)

def review_service(db: AsyncIOMotorDatabase = Depends(get_database)):
    return ReviewService(db)

@router.get('/reviews',response_model = List[ReviewResponse])
async def get_review(request:Request, service: ReviewService = Depends(review_service)):
    logger.info(f"Request path: {request.url.path}")
    try:
        reviews = await service.get_review()
        return reviews
    except HTTPException as e:
        logger.error(f"HTTPException: {e.detail}")
        raise e
    except Exception as e:
        logger.error(f"Exception: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")

@router.post('/books/{book_id}/review',response_model = ReviewResponse)
async def create_review(request:Request, book_id: str, review : CreateReview, service:ReviewService=Depends(review_service)):
    logger.info(f"Request path: {request.url.path}")
    try:
        return await service.create_review(book_id, review)
    except HTTPException as e:
        logger.error(f"HTTPException: {e.detail}")
        raise e
    except Exception as e:
        logger.error(f"Exception: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")
    

@router.get('/books/{book_id}/reviews',response_model = List[ReviewResponse])
async def get_all_reviews(request:Request, book_id:str, service: ReviewService = Depends(review_service)):
    logger.info(f"Request path: {request.url.path}")
    try:
        reviews = await service.get_reviews(book_id)
        return reviews
    except HTTPException as e:
        logger.error(f"HTTPException: {e.detail}")
        raise e
    except Exception as e:
        logger.error(f"Exception: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")

@router.put("/books/{book_id}/reviews/{review_id}",response_model = ReviewResponse)
async def update_review(request:Request, book_id:str, review_id : str, update_review : UpdateReview, service:ReviewService = Depends(review_service)):
    logger.info(f"Request path: {request.url.path}")
    try:
        review_update = await service.update_review(book_id,review_id,update_review)
        return review_update
    except HTTPException as e:
        logger.error(f"HTTPException: {e.detail}")
        raise e
    except Exception as e:
        logger.error(f"Exception: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")


@router.get("/books/{book_id}/reviews/{review_id}", response_model=ReviewResponse)
async def get_review_by_book_and_id( request: Request, book_id: str, review_id: str, service: ReviewService = Depends(review_service) ):
    logger.info(f"Request path: {request.url.path}")
    try:
        # Check if book exists
        book = await service.db['books'].find_one({"_id": book_id})
        if not book:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
        
        # Find review with the given review_id and book_id
        review = await service.collection.find_one({"_id": review_id, "book_id": book_id})
        if not review:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Review not found")

        return service._to_response(review, ReviewResponse)

    except HTTPException as e:
        logger.error(f"HTTPException: {e.detail}")
        raise e
    except Exception as e:
        logger.error(f"Exception: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal Server Error"
        )

@router.delete("/books/{book_id}/reviews/{review_id}")
async def delete_review(request:Request,review_id:str,service:ReviewService = Depends(review_service)):
    logger.info(f"Request path: {request.url.path}")
    try:
        result = await service.delete_review(review_id)
        return result
    except HTTPException as e:
        logger.error(f"HTTPException: {e.detail}")
        raise e
    except Exception as e:
        logger.error(f"Exception: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")


