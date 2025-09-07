from fastapi import APIRouter, Depends, HTTPException, Request, status
from motor.motor_asyncio import AsyncIOMotorDatabase
from typing import List
import logging
from app2.schemas.bookstore import CreateBookstore, UpdateBookstore, ResponseBookstore
from app2.services.bookstore import BookstoreService
from app2.database import get_database

router = APIRouter(prefix='/bookstore', tags=['bookstore'])

logger = logging.getLogger(__name__)

def bookstore_service(db: AsyncIOMotorDatabase = Depends(get_database)):
    return BookstoreService(db)

@router.get("/get_bookstores", response_model=List[ResponseBookstore])
async def get_bookstores(request: Request, service: BookstoreService = Depends(bookstore_service)):
    logger.info(f"Request path: {request.url.path}")
    try:
        return await service.get_bookstores()
    except HTTPException as e:
        logger.error(f"HTTPException: {e.detail}")
        raise e
    except Exception as e:
        logger.error(f"Exception: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")


@router.post("/create_bookstore", response_model=ResponseBookstore, status_code=status.HTTP_201_CREATED)
async def create_bookstore(request: Request, publisher: CreateBookstore, service: BookstoreService = Depends(bookstore_service)):
    logger.info(f"Request path: {request.url.path}")
    try:
        return await service.create_bookstore(publisher)
    except HTTPException as e:
        logger.error(f"HTTPException: {e.detail}")
        raise e
    except Exception as e:
        logger.error(f"Exception: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")


@router.get("/{bookstore_id}", response_model=ResponseBookstore)
async def get_bookstore(request: Request, bookstore_id: str, service: BookstoreService = Depends(bookstore_service)):
    logger.info(f"Request path: {request.url.path}")
    try:
        publisher = await service.get_bookstore(bookstore_id)
        return publisher
    except HTTPException as e:
        logger.error(f"HTTPException: {e.detail}")
        raise e
    except Exception as e:
        logger.error(f"Exception: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")


@router.put("/{bookstore_id}", response_model=ResponseBookstore)
async def update_bookstore(request: Request, bookstore_id: str, update_bookstr: UpdateBookstore, service: BookstoreService = Depends(bookstore_service)):
    logger.info(f"Request path: {request.url.path}")
    try:
        updated_bookstore = await service.update_bookstore(bookstore_id, update_bookstr)
        return updated_bookstore
    except HTTPException as e:
        logger.error(f"HTTPException: {e.detail}")
        raise e
    except Exception as e:
        logger.error(f"Exception: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")


@router.delete("/{bookstore_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_bookstore(request: Request, bookstore_id: str, service: BookstoreService = Depends(bookstore_service)):
    logger.info(f"Request path: {request.url.path}")
    try:
        await service.delete_bookstore(bookstore_id)
        return f"Bookstore with id {bookstore_id} is Successfully deleted"
    except HTTPException as e:
        logger.error(f"HTTPException: {e.detail}")
        raise e
    except Exception as e:
        logger.error(f"Exception: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")
