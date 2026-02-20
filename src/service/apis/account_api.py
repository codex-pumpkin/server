# coding: utf-8
from io import BytesIO
from typing import Dict, List  # noqa: F401

from src.core.settings import settings
from src.business.interfaces import (
    IUserInfoManager,
    ISystemManager
)


from src.service.dependencies import get_user_info_manager

from fastapi import (  # noqa: F401
    APIRouter,
    Body,
    Cookie,
    Depends,
    Form,
    Header,
    HTTPException,
    Path,
    Query,
    Response,
    Security,
    status,
    UploadFile,
    File,
)

from fastapi.responses import StreamingResponse

from src.core.dtos.extra_models import TokenModel  # noqa: F401
from pydantic import Field, StrictBytes, StrictStr
from typing import Optional, Tuple, Union
from src.core.dtos.account_response import AccountResponse
from src.core.dtos.update_account_request import UpdateAccountRequest
from src.service.security_api import get_token_jwt, get_token_jwt_mandatory
from pathlib import Path


router = APIRouter()


@router.get(
    "/account",
    responses={
        200: {"model": AccountResponse, "description": "Account data retrieved successfully"},
        401: {"description": "User not authenticated"},
    },
    tags=["Account"],
    summary="Get current authenticated user&#39;s account data",
    response_model_by_alias=True,
)
async def account_get(
    token_jwt: TokenModel = Security(
        get_token_jwt_mandatory
    ),
    user_info: IUserInfoManager = Depends(get_user_info_manager)
) -> AccountResponse:
    """
    Return account information for the currently authenticated user.

    @param
        token_jwt (TokenModel): Authenticated user token payload resolved from security dependency.
        user_info (IUserInfoManager): Business manager used to fetch account data.

    @return
        AccountResponse: Account details for the authenticated user.
    """
    return await user_info.get_account_info(token_jwt=token_jwt)


@router.put(
    "/account",
    responses={
        204: {"description": "Account updated successfully"},
        400: {"description": "Invalid request"},
        401: {"description": "User not authenticated"},
        409: {"description": "Email or username already taken"},
    },
    tags=["Account"],
    summary="Update account email and username",
    response_model_by_alias=True,
)
async def account_put(
    update_account_request: UpdateAccountRequest = Body(None, description=""),
    token_jwt: TokenModel = Security(
        get_token_jwt_mandatory
    ),
    user_info: IUserInfoManager = Depends(get_user_info_manager)
) -> None:
    """
    Update authenticated user's email and username.

    @param
        update_account_request (UpdateAccountRequest): Payload with new email and username values.
        token_jwt (TokenModel): Authenticated user token payload resolved from security dependency.
        user_info (IUserInfoManager): Business manager used to apply account updates.

    @return
        None: Persists account updates and triggers reverification flow if email changes.
    """
    await user_info.update_user_name_email(
        token_jwt=token_jwt,
        update_account_request=update_account_request
    )


@router.get(
    "/account/profile-picture",
    responses={
        200: {"description": "Profile picture returned successfully."},
        401: {"description": "User not authenticated"},
    },
    tags=["Account"],
    summary="Get the authenticated user's profile picture",
    response_model=None,
)
async def account_profile_picture_get(
    token_jwt: TokenModel = Security(get_token_jwt_mandatory),
    user_info: IUserInfoManager = Depends(get_user_info_manager)
):
    """
    Returns the profile picture for the authenticated user.
    
    @param token_jwt (TokenModel): Authenticated user token payload resolved from security dependency.
    @param user_info (IUserInfoManager): Business manager used to fetch profile picture data.
    
    @return StreamingResponse: If a profile picture exists, returns it as a JPEG image stream; otherwise returns None.
    
    """
    picture_data = await user_info.get_profile_picture(token_jwt)
    if picture_data is None:
        return None

    return StreamingResponse(
        content=BytesIO(picture_data),
        media_type="image/jpeg",
    )

@router.put(
    "/account/profile-picture",
    responses={
        204: {"description": "Profile Picture updated successfully"},
        400: {"description": "Invalid request"},
        401: {"description": "User not authenticated"},
    },
    tags=["Account"],
    summary="Updates the profile picture of the authenticated user",
    response_model=None
)
async def account_profile_picture_put(
    file: UploadFile = File(...),
    token_jwt: TokenModel = Security(get_token_jwt_mandatory),
    user_info: IUserInfoManager = Depends(get_user_info_manager)
):
    """
    Updates the profile picture of the authenticated user
    
    @param file (UploadFile): Uploaded image file for the new profile picture.
    @param token_jwt (TokenModel): Authenticated user token payload resolved from security dependency.
    @param user_info (IUserInfoManager): Business manager used to update profile picture data.
    
    @return None: Persists the new profile picture for the user.
    """
    image_bytes = await file.read()
    with open(Path(settings.pictures_settings.path) / f"{token_jwt.sub}.jpg", "wb") as f:
        f.write(image_bytes)
    return await user_info.update_profile_picture(token_jwt, image_bytes)
