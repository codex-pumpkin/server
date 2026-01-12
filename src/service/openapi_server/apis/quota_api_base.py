# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from typing import Any
from service.openapi_server.models.quota_config import QuotaConfig
from service.openapi_server.security_api import get_token_JWT

class BaseQuotaApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseQuotaApi.subclasses = BaseQuotaApi.subclasses + (cls,)
    async def quota_get(
        self,
    ) -> QuotaConfig:
        """Returns the current quota configuration."""
        ...


    async def quota_put(
        self,
        quota_config: QuotaConfig,
    ) -> QuotaConfig:
        """Updates the quota limits for members and admins. Only for admins."""
        ...
