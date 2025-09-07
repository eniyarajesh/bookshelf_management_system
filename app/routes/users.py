from fastapi import APIRouter, Depends, HTTPException, Request, status, Query
from motor.motor_asyncio import AsyncIOMotorDatabase
from typing import List
import logging
from app.schemas.users import CreateUser, UserDetails, UpdateUser
from app.database import get_database
from app.services.users import UserService

router = APIRouter(prefix='/users', tags=['users'])

logger = logging.getLogger(__name__)

def user_service(db: AsyncIOMotorDatabase = Depends(get_database)):
    return UserService(db)

@router.get("", response_model=List[UserDetails])
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

@router.post('',response_model = UserDetails)
async def create_user(request:Request, user : CreateUser, service:UserService=Depends(user_service)):
    logger.info(f"Request path: {request.url.path}")
    try:
        return await service.create_user(user)
    except HTTPException as e:
        logger.error(f"HTTPException: {e.detail}")
        raise e
    except Exception as e:
        logger.error(f"Exception: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")
    
@router.get('/{user_id}',response_model = UserDetails)
async def get_user_details(request:Request, user_id:str, service: UserService = Depends(user_service)):
    logger.info(f"Request path: {request.url.path}")
    try:
        user = await service.get_user(user_id)
        return user
    except HTTPException as e:
        logger.error(f"HTTPException: {e.detail}")
        raise e
    except Exception as e:
        logger.error(f"Exception: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")

@router.put("/{user_id}",response_model = UserDetails)
async def update_user(request:Request, user_id:str, user : UpdateUser, service:UserService = Depends(user_service)):
    logger.info(f"Request path: {request.url.path}")
    try:
        user_update = await service.update_user(user_id,user)
        return user_update
    except HTTPException as e:
        logger.error(f"HTTPException: {e.detail}")
        raise e
    except Exception as e:
        logger.error(f"Exception: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")
    
@router.delete('/{user_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(request : Request, user_id : str, service : UserService = Depends(user_service)):
    logger.info(f"Request path: {request.url.path}")
    try:
        await service.delete_user(user_id)
        return f"user with id {user_id} is successfully deleted"
    except HTTPException as e:
        logger.error(f"HTTPException: {e.detail}")
        raise e
    except Exception as e:
        logger.error(f"Exception: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")
