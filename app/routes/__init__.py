from fastapi import APIRouter

from app.routes.users import router as users_router


api_routes = APIRouter(prefix="/api")


api_routes.include_router(users_router)