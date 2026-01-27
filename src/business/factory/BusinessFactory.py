import asyncio
from typing import Dict, Type, TypeVar

from src.business.interfaces import (
    IBasicAuthManager,
    IInferenceManager,
    IUserInfoManager,
    ISystemManager,
    IPromptManager
)


T = TypeVar("T")


class BusinessFactory:
    _singletons: Dict[Type, object] = {}
    _lock = asyncio.Lock()

    @classmethod
    async def _get_singleton(cls, interface: Type[T], implementation: Type[T]) -> T:
        if interface not in cls._singletons:
            async with cls._lock:
                if interface not in cls._singletons:
                    cls._singletons[interface] = implementation()
        return cls._singletons[interface]  # type: ignore

    # ------------------------
    # Interface-based getters
    # ------------------------

    @classmethod
    async def get_inference_manager(cls) -> IInferenceManager:
        from src.business.impl.inference.InferenceManager import InferenceManager
        return await cls._get_singleton(IInferenceManager, InferenceManager)

    @classmethod
    async def get_system_manager(cls) -> ISystemManager:
        from src.business.impl.system.SystemManager import SystemManager
        return await cls._get_singleton(ISystemManager, SystemManager)

    @classmethod
    async def get_basic_auth_manager(cls) -> IBasicAuthManager:
        from src.business.impl.auth.BasicAuthManager import BasicAuthManager
        return await cls._get_singleton(IBasicAuthManager, BasicAuthManager)

    @classmethod
    async def get_user_info_manager(cls) -> IUserInfoManager:
        from src.business.impl.userinfo.UserInfoManager import UserInfoManager
        return await cls._get_singleton(IUserInfoManager, UserInfoManager)

    @classmethod
    async def get_prompt_manager(cls) -> IPromptManager:
        from src.business.impl.prompt.PromptManager import PromptManager
        return await cls._get_singleton(IPromptManager, PromptManager)
