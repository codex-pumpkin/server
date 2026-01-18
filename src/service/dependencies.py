
from src.business.factory import BusinessFactory

def get_inference_manager():
    return BusinessFactory.get_inference_manager()

def get_system_manager():
    return BusinessFactory.get_system_manager()

def get_auth_manager():
    return BusinessFactory.get_basic_auth_manager()

def get_user_info_manager():
    return BusinessFactory.get_user_info_manager()