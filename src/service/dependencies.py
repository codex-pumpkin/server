
from src.business.factory import BusinessFactory

async def get_inference_manager():
    return await BusinessFactory.get_inference_manager()

async def get_system_manager():
    return await BusinessFactory.get_system_manager()

async def get_auth_manager():
    return await BusinessFactory.get_basic_auth_manager()

async def get_user_info_manager():
    return await BusinessFactory.get_user_info_manager()