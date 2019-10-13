from fastapi import APIRouter
from app.api.api_v1.endpoints import user, login, stats

api_router = APIRouter()
api_router.include_router(user.router, prefix='/user', tags=['user'])
api_router.include_router(login.router, tags=['login'])
api_router.include_router(stats.router, tags=['stats'])