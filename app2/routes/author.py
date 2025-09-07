from fastapi import APIRouter, Depends, HTTPException, Request, status
from motor.motor_asyncio import AsyncIOMotorDatabase
import logging
from app2.schemas.author import CreateAuthor, UpdateAuthor, ResponseAuthor
from app2.services.author import AuthorService
from app2.database import get_database
from typing import List

router = APIRouter(prefix="/author", tags=["author"])

logger = logging.getLogger(__name__)

def author_service(db: AsyncIOMotorDatabase = Depends(get_database)):
    return AuthorService(db)

@router.get("/get_author", response_model=List[ResponseAuthor])
async def get_authors(request: Request, service: AuthorService = Depends(author_service)):
    logger.info(f"Request path: {request.url.path}")
    try:
        return await service.get_authors()
    except HTTPException as e:
        logger.error(f"HTTPException: {e.detail}")
        raise e
    except Exception as e:
        logger.error(f"Exception: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")

@router.post("/create_author", response_model=ResponseAuthor)
async def create_author(request: Request, author: CreateAuthor, service: AuthorService = Depends(author_service)):
    logger.info(f"Request path: {request.url.path}")
    try:
        return await service.create_author(author)
    except HTTPException as e:
        logger.error(f"HTTPException: {e.detail}")
        raise e
    except Exception as e:
        logger.error(f"Exception: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")

@router.get("/{author_id}", response_model=ResponseAuthor)
async def get_author(author_id: str, request: Request, service: AuthorService = Depends(author_service)):
    logger.info(f"Request path: {request.url.path}")
    try:
        return await service.get_author(author_id)
    except HTTPException as e:
        logger.error(f"HTTPException: {e.detail}")
        raise e
    except Exception as e:
        logger.error(f"Exception: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")

@router.put("/{author_id}", response_model=ResponseAuthor)
async def update_authors(request: Request, author_id: str, author_data: UpdateAuthor, service: AuthorService = Depends(author_service)):
    logger.info(f"Request path: {request.url.path}")
    try:
        updated_author =  await service.update_authors(author_id, author_data)
        return updated_author
    except HTTPException as e:
        logger.error(f"HTTPException: {e.detail}")
        raise e
    except Exception as e:
        logger.error(f"Exception: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")
    
@router.delete("/{author_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_author(author_id: str, request: Request, service: AuthorService = Depends(author_service)):
    logger.info(f"Request path: {request.url.path}")
    try:
        return await service.delete_author(author_id)
    except HTTPException as e:
        logger.error(f"HTTPException: {e.detail}")
        raise e
    except Exception as e:
        logger.error(f"Exception: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")