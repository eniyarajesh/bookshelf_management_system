from fastapi import APIRouter, Depends, HTTPException, Request, status
from motor.motor_asyncio import AsyncIOMotorDatabase
from typing import List
import logging
from app2.schemas.publisher import CreatePublisher, UpdatePublisher, ResponsePublisher
from app2.services.publisher import PublisherService
from app2.database import get_database

router = APIRouter(prefix='/publisher', tags=['publisher'])

logger = logging.getLogger(__name__)

def publisher_service(db: AsyncIOMotorDatabase = Depends(get_database)):
    return PublisherService(db)

@router.get("/get_publishers", response_model=List[ResponsePublisher])
async def get_publishers(request: Request, service: PublisherService = Depends(publisher_service)):
    logger.info(f"Request path: {request.url.path}")
    try:
        return await service.get_publishers()
    except HTTPException as e:
        logger.error(f"HTTPException: {e.detail}")
        raise e
    except Exception as e:
        logger.error(f"Exception: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")


@router.post("/create_publisher", response_model=ResponsePublisher, status_code=status.HTTP_201_CREATED)
async def create_publisher(request: Request, publisher: CreatePublisher, service: PublisherService = Depends(publisher_service)):
    logger.info(f"Request path: {request.url.path}")
    try:
        return await service.create_publisher(publisher)
    except HTTPException as e:
        logger.error(f"HTTPException: {e.detail}")
        raise e
    except Exception as e:
        logger.error(f"Exception: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")


@router.get("/{publisher_id}", response_model=ResponsePublisher)
async def get_publisher(request: Request, publisher_id: str, service: PublisherService = Depends(publisher_service)):
    logger.info(f"Request path: {request.url.path}")
    try:
        publisher = await service.get_publisher(publisher_id)
        return publisher
    except HTTPException as e:
        logger.error(f"HTTPException: {e.detail}")
        raise e
    except Exception as e:
        logger.error(f"Exception: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")


@router.put("/{publisher_id}", response_model=ResponsePublisher)
async def update_publisher(request: Request, publisher_id: str, update_publisher: UpdatePublisher, service: PublisherService = Depends(publisher_service)):
    logger.info(f"Request path: {request.url.path}")
    try:
        updated_publisher = await service.update_publisher(publisher_id, update_publisher)
        return updated_publisher
    except HTTPException as e:
        logger.error(f"HTTPException: {e.detail}")
        raise e
    except Exception as e:
        logger.error(f"Exception: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")


@router.delete("/{publisher_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_publisher(request: Request, publisher_id: str, service: PublisherService = Depends(publisher_service)):
    logger.info(f"Request path: {request.url.path}")
    try:
        await service.delete_publisher(publisher_id)
        return f"Publisher with id {publisher_id} is Successfully deleted"
    except HTTPException as e:
        logger.error(f"HTTPException: {e.detail}")
        raise e
    except Exception as e:
        logger.error(f"Exception: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")
