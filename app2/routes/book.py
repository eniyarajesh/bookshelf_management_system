from fastapi import APIRouter, Depends, HTTPException, Request, status
from motor.motor_asyncio import AsyncIOMotorDatabase
import logging
from app2.schemas.book import CreateBook, UpdateBook, ResponseBook
from app2.services.book import BookService
from app2.database import get_database
from typing import List

router = APIRouter(prefix="/book", tags=["book"])

logger = logging.getLogger(__name__)

def book_service(db: AsyncIOMotorDatabase = Depends(get_database)):
    return BookService(db)

@router.get("/get_book", response_model=List[ResponseBook])
async def get_books(request: Request, service: BookService = Depends(book_service)):
    logger.info(f"Request path: {request.url.path}")
    try:
        return await service.get_books()
    except HTTPException as e:
        logger.error(f"HTTPException: {e.detail}")
        raise e
    except Exception as e:
        logger.error(f"Exception: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")

@router.post("/create_book", response_model=ResponseBook)
async def create_book(request: Request, book: CreateBook, service: BookService = Depends(book_service)):
    logger.info(f"Request path: {request.url.path}")
    try:
        return await service.create_book(book)
    except HTTPException as e:
        logger.error(f"HTTPException: {e.detail}")
        raise e
    except Exception as e:
        logger.error(f"Exception: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")

@router.get("/{book_id}", response_model=ResponseBook)
async def get_book(book_id: str, request: Request, service: BookService = Depends(book_service)):
    logger.info(f"Request path: {request.url.path}")
    try:
        return await service.get_book(book_id)
    except HTTPException as e:
        logger.error(f"HTTPException: {e.detail}")
        raise e
    except Exception as e:
        logger.error(f"Exception: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")

@router.put("/{book_id}", response_model=ResponseBook)
async def update_books(request: Request, book_id: str, book_data: UpdateBook, service: BookService = Depends(book_service)):
    logger.info(f"Request path: {request.url.path}")
    try:
        updated_book =  await service.update_books(book_id, book_data)
        return updated_book
    except HTTPException as e:
        logger.error(f"HTTPException: {e.detail}")
        raise e
    except Exception as e:
        logger.error(f"Exception: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")
    
@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: str, request: Request, service: BookService = Depends(book_service)):
    logger.info(f"Request path: {request.url.path}")
    try:
        return await service.delete_book(book_id)
    except HTTPException as e:
        logger.error(f"HTTPException: {e.detail}")
        raise e
    except Exception as e:
        logger.error(f"Exception: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")