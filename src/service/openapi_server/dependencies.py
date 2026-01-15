from fastapi import Depends
from src.business.factory.ObjectHandler import ObjectHandler



def get_inference_manager():
    return ObjectHandler.get_inference_manager()

def get_system_manager():
    return ObjectHandler.get_system_manager()

def get_auth_manager():
    return ObjectHandler.get__basic_auth_manager()

def get_system_manager():
    return ObjectHandler.get_system_manager()

def get_user_info_manager():
    return ObjectHandler.get_user_info_manager()