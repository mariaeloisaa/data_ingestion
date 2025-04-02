from fastapi import APIRouter
from api.v1.endpoints import wilson

api_router = APIRouter()
api_router.include_router(wilson.router, prefix="/wilson", tags=["Wilsons"])