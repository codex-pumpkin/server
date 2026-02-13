import datetime

from src.core.dtos import (
    AccountResponse,
    TokenInfo,
    QuotaConfig,
    LLMConfigurationResponse,
    TargetLanguage,
    MessageResponse,
)
from src.persistence.impl.database.database import Base
from src.persistence.impl.database.model_types import (
    uuid_pk,
    created_at_type,
    verification_code,
)
import enum
from sqlalchemy import ForeignKey, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional
import uuid

class UsersOrm(Base):
    __tablename__ = "users"

    id: Mapped[uuid_pk]
    created_at: Mapped[created_at_type]
    username: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str] = mapped_column(unique=True)
    hashed_password: Mapped[str] = mapped_column()
    is_admin: Mapped[bool] = mapped_column(default=False)
    is_verified: Mapped[bool] = mapped_column(default=False)
    google_id: Mapped[Optional[str]] = mapped_column(default=None)

    conversations: Mapped[list["ConversationsOrm"]] = relationship(
        back_populates="user"
    )
    valid_token: Mapped["TokensOrm"] = relationship(
        back_populates="user",
        primaryjoin=(
            "and_("
            "UsersOrm.id == TokensOrm.user_id, "
            "TokensOrm.valid == True, "
            "TokensOrm.expires_at > func.now()"
            ")"
        ),
    )

    def to_dto(self) -> AccountResponse:
        return AccountResponse(
            id=self.id,
            email=self.email,
            username=self.username,
            is_admin=self.is_admin,
            is_verified=self.is_verified,
            created_at=self.created_at.timestamp(),
            auth_via_google=True if self.google_id else False,
        )


class LlmModelsOrm(Base):
    __tablename__ = "llm_models"

    id: Mapped[uuid_pk]
    name: Mapped[str] = mapped_column()
    url: Mapped[str] = mapped_column()
    api_key: Mapped[str] = mapped_column()

    def to_dto(self) -> LLMConfigurationResponse:
        return LLMConfigurationResponse(
            id=self.id,
            name=self.name,
            api_url=self.url,
            api_key_set=True
        )

class ConversationsOrm(Base):
    __tablename__ = "conversations"

    id: Mapped[uuid_pk]
    created_at: Mapped[created_at_type]
    updated_at: Mapped[created_at_type]
    name: Mapped[str] = mapped_column()
    is_pined: Mapped[bool] = mapped_column(default=False)
    llm_id: Mapped[str] = mapped_column(ForeignKey("llm_models.id"))
    target_language: Mapped[TargetLanguage] = mapped_column(default=TargetLanguage.SPICE_NETLIST)
    user_id: Mapped[str] = mapped_column(ForeignKey("users.id"))

    user: Mapped["UsersOrm"] = relationship(
        back_populates="conversations"
    )
    messages: Mapped[list["MessagesOrm"]] = relationship(
        back_populates="conversation"
    )



class MessagesOrm(Base):
    __tablename__ = "messages"

    id: Mapped[uuid_pk]
    created_at: Mapped[created_at_type]
    prompt: Mapped[str] = mapped_column()
    response: Mapped[str] = mapped_column()
    generation_ms: Mapped[int] = mapped_column()
    conversation_id: Mapped[Optional[str]] = mapped_column(
        ForeignKey("conversations.id", ondelete="SET NULL"),
        nullable=True
    )

    conversation: Mapped[list["ConversationsOrm"]] = relationship(
        back_populates="messages"
    )

    def to_dto(self) -> MessageResponse:
        return MessageResponse(
            id=self.id,
            created_at=self.created_at,
            message=self.prompt,
            response=self.response,
            response_secondary=self.response,
            generation_millis=self.generation_ms
        )

class TokenType(enum.Enum):
    REFRESH="refresh"
    EMAIL="email"
    PASSWORD="password"


class TokensOrm(Base):
    __tablename__ = "tokens"

    id: Mapped[uuid_pk]
    type: Mapped[TokenType] = mapped_column(Enum(TokenType), nullable=False)
    valid: Mapped[bool] = mapped_column(default=True)
    created_at: Mapped[created_at_type]
    expires_at: Mapped[datetime.datetime] = mapped_column()
    user_id: Mapped[str] = mapped_column(ForeignKey("users.id"))

    user: Mapped["UsersOrm"] = relationship(
        back_populates="valid_token"
    )

    def to_dto(self) -> TokenInfo:
        return TokenInfo(
            id=uuid.UUID(self.id),
            created_at=self.created_at,
            expires_at=self.expires_at,
            valid=self.valid,
            user_id=uuid.UUID(self.user_id),
            token_type=self.type.value
        )

class QuotaOrm(Base):
    __tablename__ = "quota_config"

    id: Mapped[uuid_pk]
    admin_limit: Mapped[int]
    member_limit: Mapped[int]

    def to_dto(self) -> QuotaConfig:
        return QuotaConfig(
            admin=self.admin_limit,
            member=self.member_limit
        )