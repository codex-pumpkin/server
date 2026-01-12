# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from typing import Any
from service.openapi_server.models.analytics_response import AnalyticsResponse
from service.openapi_server.security_api import get_token_JWT

class BaseAnalyticsApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseAnalyticsApi.subclasses = BaseAnalyticsApi.subclasses + (cls,)
    async def analytics_get(
        self,
    ) -> AnalyticsResponse:
        """Returns the analytics. Only for Admins."""
        ...
