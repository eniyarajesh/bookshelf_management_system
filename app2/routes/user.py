from fastapi import APIRouter, Depends, HTTPException, Request, status
from motor.motor_asyncio import AsyncIOMotorDatabase
import logging
from app2.schemas.user import CreateUser, UpdateUser, ResponseUser
from app2.services.user import UserService
from app2.database import get_database
from typing import List

router = APIRouter(prefix="/users", tags=["Users"])

logger = logging.getLogger(__name__)

def user_service(db: AsyncIOMotorDatabase = Depends(get_database)):
    return UserService(db)

@router.get("/get_users", response_model=List[ResponseUser])
async def get_users(request: Request, service: UserService = Depends(user_service)):
    logger.info(f"Request path: {request.url.path}")
    try:
        return await service.get_users()
    except HTTPException as e:
        logger.error(f"HTTPException: {e.detail}")
        raise e
    except Exception as e:
        logger.error(f"Exception: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")

@router.post("/create_users", response_model=ResponseUser)
async def create_user(request: Request, user: CreateUser, service: UserService = Depends(user_service)):
    logger.info(f"Request path: {request.url.path}")
    try:
        return await service.create_user(user)
    except HTTPException as e:
        logger.error(f"HTTPException: {e.detail}")
        raise e
    except Exception as e:
        logger.error(f"Exception: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")

@router.get("/{user_id}", response_model=ResponseUser)
async def get_user(user_id: str, request: Request, service: UserService = Depends(user_service)):
    logger.info(f"Request path: {request.url.path}")
    try:
        return await service.get_user(user_id)
    except HTTPException as e:
        logger.error(f"HTTPException: {e.detail}")
        raise e
    except Exception as e:
        logger.error(f"Exception: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")

@router.put("/{user_id}", response_model=ResponseUser)
async def update_user(request: Request, user_id: str, user_data: UpdateUser, service: UserService = Depends(user_service)):
    logger.info(f"Request path: {request.url.path}")
    try:
        updated_user =  await service.update_user(user_id, user_data)
        return updated_user
    except HTTPException as e:
        logger.error(f"HTTPException: {e.detail}")
        raise e
    except Exception as e:
        logger.error(f"Exception: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")
    
@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: str, request: Request, service: UserService = Depends(user_service)):
    logger.info(f"Request path: {request.url.path}")
    try:
        return await service.delete_user(user_id)
    except HTTPException as e:
        logger.error(f"HTTPException: {e.detail}")
        raise e
    except Exception as e:
        logger.error(f"Exception: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")