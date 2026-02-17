
from src.business.factory import BusinessFactory

async def get_inference_manager():
    """Get inference manager."""
    return await BusinessFactory.get_inference_manager()

async def get_system_manager():
    """Get system manager."""
    return await BusinessFactory.get_system_manager()

async def get_auth_manager():
    """Get auth manager."""
    return await BusinessFactory.get_basic_auth_manager()

async def get_user_info_manager():
    """Get user info manager."""
    return await BusinessFactory.get_user_info_manager()