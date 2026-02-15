

from .authentication_api import router as authentication_router
from .conversations_api import  router as conversation_router
from .quota_api import router as quota_router
from .llm_api import router as llm_router
from .analytics_api import router as analytics_router
from .account_api import router as account_router

from fastapi import (
    APIRouter
)

main_router = APIRouter()

main_router.include_router(authentication_router)
main_router.include_router(conversation_router)
main_router.include_router(quota_router)
main_router.include_router(llm_router)
main_router.include_router(analytics_router)
main_router.include_router(account_router)

__all__ = [
    "main_router"
]
