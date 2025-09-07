from fastapi import APIRouter, Depends, HTTPException, Request, status
from motor.motor_asyncio import AsyncIOMotorDatabase
from typing import List
import logging
from app2.schemas.category import CreateCategory, UpdateCategory, ResponseCategory
from app2.services.category import CategoryService
from app2.database import get_database

router = APIRouter(prefix='/category', tags=['category'])

logger = logging.getLogger(__name__)

def category_service(db: AsyncIOMotorDatabase = Depends(get_database)):
    return CategoryService(db)

@router.get("/get_categories", response_model=List[ResponseCategory])
async def get_categories(request: Request, service: CategoryService = Depends(category_service)):
    logger.info(f"Request path: {request.url.path}")
    try:
        return await service.get_categories()
    except HTTPException as e:
        logger.error(f"HTTPException: {e.detail}")
        raise e
    except Exception as e:
        logger.error(f"Exception: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")


@router.post("/create_category", response_model=ResponseCategory, status_code=status.HTTP_201_CREATED)
async def create_category(request: Request, category: CreateCategory, service: CategoryService = Depends(category_service)):
    logger.info(f"Request path: {request.url.path}")
    try:
        return await service.create_category(category)
    except HTTPException as e:
        logger.error(f"HTTPException: {e.detail}")
        raise e
    except Exception as e:
        logger.error(f"Exception: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")


@router.get("/{category_id}", response_model=ResponseCategory)
async def get_category(request: Request, category_id: str, service: CategoryService = Depends(category_service)):
    logger.info(f"Request path: {request.url.path}")
    try:
        category = await service.get_category(category_id)
        return category
    except HTTPException as e:
        logger.error(f"HTTPException: {e.detail}")
        raise e
    except Exception as e:
        logger.error(f"Exception: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")


@router.put("/{category_id}", response_model=ResponseCategory)
async def update_category(request: Request, category_id: str, update_category: UpdateCategory, service: CategoryService = Depends(category_service)):
    logger.info(f"Request path: {request.url.path}")
    try:
        updated_category = await service.update_category(category_id, update_category)
        return updated_category
    except HTTPException as e:
        logger.error(f"HTTPException: {e.detail}")
        raise e
    except Exception as e:
        logger.error(f"Exception: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")


@router.delete("/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_category(request: Request, category_id: str, service: CategoryService = Depends(category_service)):
    logger.info(f"Request path: {request.url.path}")
    try:
        await service.delete_category(category_id)
        return f"category with id {category_id} is Successfully deleted"
    except HTTPException as e:
        logger.error(f"HTTPException: {e.detail}")
        raise e
    except Exception as e:
        logger.error(f"Exception: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")
