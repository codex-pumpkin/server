from fastapi import FastAPI, Security
from fastapi.testclient import TestClient
from types import SimpleNamespace
from unittest.mock import AsyncMock
from uuid import uuid4
import datetime
from typing import List

from src.service.apis.conversations_api import router as conv_router
from src.service.dependencies import get_inference_manager
from src.service.security_api import get_token_jwt_mandatory, get_token_jwt
from src.core.dtos import TokenModel, ConversationResponse, ConversationRequest, MessageRequest, MessageResponse


def _dummy_token():
    return TokenModel(sub=uuid4(), is_admin=False, exp=datetime.datetime.now(), toc=datetime.datetime.now())


def setup_conv_app():
    app = FastAPI()
    app.include_router(conv_router)

    # create a stub inference manager with async methods returning predictable values
    def override_inference_manager():
        mgr = SimpleNamespace()
        mgr.get_conversations_by_user = AsyncMock(return_value=[])
        mgr.start_conversation = AsyncMock(return_value=ConversationResponse(
            id=uuid4(), name="c", pinned=None, llm_model_config_id=None,
            created_at=0, updated_at=0, target_language="spice_netlist", user_id=uuid4(), messages=[]
        ))
        mgr.update_conversation = AsyncMock(return_value=None)
        mgr.remove_conversation = AsyncMock(return_value=None)
        mgr.message_regeneration = AsyncMock(return_value=MessageResponse(
            id=str(uuid4()), message="msg", generation_millis=0, response="resp", graph="", created_at=0
        ))
        mgr.post_message_to_conversation = AsyncMock(return_value=MessageResponse(
            id=str(uuid4()), message="msg2", generation_millis=0, response="resp2", graph="", created_at=0
        ))
        return mgr

    app.dependency_overrides[get_inference_manager] = override_inference_manager
    app.dependency_overrides[get_token_jwt_mandatory] = lambda: _dummy_token()
    app.dependency_overrides[get_token_jwt] = lambda: _dummy_token()
    return app


app = setup_conv_app()
client = TestClient(app)


def test_get_conversations_empty():
    resp = client.get("/conversations")
    assert resp.status_code == 200
    assert resp.json() == []


def test_post_conversation():
    body = {"message": "hello", "llm_model_config_id": str(uuid4()), "target_language": "spice_netlist", "name": "test"}
    resp = client.post("/conversations", json=body)
    assert resp.status_code == 200
    data = resp.json()
    assert data["name"] == "c"


def test_update_conversation():
    cid = str(uuid4())
    resp = client.put(f"/conversations/{cid}", json={"name": "new", "pinned": True})
    assert resp.status_code == 200


def test_delete_conversation():
    cid = str(uuid4())
    resp = client.delete(f"/conversations/{cid}")
    assert resp.status_code == 200 or resp.status_code == 204


def test_regenerate_message():
    cid = str(uuid4())
    resp = client.put(f"/conversations/{cid}/messages", json={"message": "retry"})
    assert resp.status_code == 200
    assert resp.json()["message"] == "msg"


def test_post_message():
    cid = str(uuid4())
    resp = client.post(f"/conversations/{cid}/messages", json={"message": "next"})
    assert resp.status_code == 200
    assert resp.json()["message"] == "msg2"
