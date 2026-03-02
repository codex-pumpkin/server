import datetime
import json

from src.core.dtos import (
    AccountResponse,
    TokenInfo,
    QuotaConfig,
    LLMConfigurationResponse,
    TargetLanguage,
    MessageResponse,
    LLMConfigurationRequest,
    NgspiceCircuitResponse,
    NgspiceSimulationResponse,
    RagDocumentResponse,
    RagDocumentChunkResponse,
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
    ngspice_circuits: Mapped[list["NgspiceCircuitOrm"]] = relationship(
        back_populates="user"
    )

    def to_dto(self) -> AccountResponse:
        """To dto."""
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
    model_name: Mapped[str] = mapped_column()
    url: Mapped[str] = mapped_column()
    api_key: Mapped[str] = mapped_column()

    def to_dto(self) -> LLMConfigurationResponse:
        """To dto."""
        return LLMConfigurationResponse(
            id=self.id,
            name=self.name,
            model_name=self.model_name,
            api_url=self.url,
            api_key_set=True
        )
    
    def to_dto_request(self) -> LLMConfigurationRequest:
        """To dto request."""
        return LLMConfigurationRequest(
            name=self.name,
            api_url=self.url,
            api_key=self.api_key,
            model_name=self.model_name
        )

class ConversationsOrm(Base):
    __tablename__ = "conversations"

    id: Mapped[uuid_pk]
    created_at: Mapped[created_at_type]
    updated_at: Mapped[created_at_type]
    name: Mapped[str] = mapped_column()
    is_pinned: Mapped[bool] = mapped_column(default=False)
    llm_id: Mapped[str | None] = mapped_column(
        ForeignKey("llm_models.id", ondelete="SET NULL"),
        nullable=True
    )
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
    graph: Mapped[str] = mapped_column()
    generation_ms: Mapped[int] = mapped_column()
    conversation_id: Mapped[Optional[str]] = mapped_column(
        ForeignKey("conversations.id", ondelete="SET NULL"),
        nullable=True
    )

    conversation: Mapped[list["ConversationsOrm"]] = relationship(
        back_populates="messages"
    )

    def to_dto(self) -> MessageResponse:
        """To dto."""
        return MessageResponse(
            id=self.id,
            created_at=self.created_at.timestamp(),
            message=self.prompt,
            response=self.response,
            graph=self.graph,
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
        """To dto."""
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
        """To dto."""
        return QuotaConfig(
            admin=self.admin_limit,
            member=self.member_limit
        )


class NgspiceCircuitOrm(Base):
    """Store SPICE netlists and circuit definitions."""
    __tablename__ = "ngspice_circuits"

    id: Mapped[uuid_pk]
    created_at: Mapped[created_at_type]
    updated_at: Mapped[created_at_type]
    name: Mapped[str] = mapped_column()
    netlist: Mapped[str] = mapped_column()  # SPICE netlist content
    description: Mapped[Optional[str]] = mapped_column(nullable=True)
    user_id: Mapped[str] = mapped_column(ForeignKey("users.id"))
    conversation_id: Mapped[Optional[str]] = mapped_column(
        ForeignKey("conversations.id", ondelete="SET NULL"),
        nullable=True
    )

    user: Mapped["UsersOrm"] = relationship(back_populates="ngspice_circuits")
    simulations: Mapped[list["NgspiceSimulationOrm"]] = relationship(
        back_populates="circuit"
    )

    def to_dto(self) -> NgspiceCircuitResponse:
        """Convert ORM to DTO."""
        return NgspiceCircuitResponse(
            id=self.id,
            name=self.name,
            netlist=self.netlist,
            description=self.description,
            created_at=self.created_at.timestamp(),
            updated_at=self.updated_at.timestamp(),
            user_id=self.user_id,
            conversation_id=self.conversation_id,
        )


class NgspiceSimulationOrm(Base):
    """Store ngspice simulation runs and results."""
    __tablename__ = "ngspice_simulations"

    id: Mapped[uuid_pk]
    created_at: Mapped[created_at_type]
    circuit_id: Mapped[str] = mapped_column(ForeignKey("ngspice_circuits.id"))
    sim_type: Mapped[str] = mapped_column()  # transient, ac, dc, etc.
    parameters: Mapped[str] = mapped_column()  # JSON-serialized parameters
    raw_output: Mapped[Optional[str]] = mapped_column(nullable=True)  # Raw simulation output
    success: Mapped[bool] = mapped_column(default=False)
    error_message: Mapped[Optional[str]] = mapped_column(nullable=True)
    execution_time_ms: Mapped[int] = mapped_column(default=0)

    circuit: Mapped["NgspiceCircuitOrm"] = relationship(back_populates="simulations")

    def to_dto(self) -> NgspiceSimulationResponse:
        """Convert ORM to DTO."""
        params = json.loads(self.parameters) if self.parameters else {}
        return NgspiceSimulationResponse(
            id=self.id,
            circuit_id=self.circuit_id,
            sim_type=self.sim_type,
            parameters=params,
            success=self.success,
            raw_output=self.raw_output,
            error_message=self.error_message,
            execution_time_ms=self.execution_time_ms,
            created_at=self.created_at.timestamp(),
        )


class RagDocumentOrm(Base):
    """Store RAG documents for semantic search."""
    __tablename__ = "rag_documents"

    id: Mapped[uuid_pk]
    created_at: Mapped[created_at_type]
    updated_at: Mapped[created_at_type]
    title: Mapped[str] = mapped_column()
    file_path: Mapped[Optional[str]] = mapped_column(nullable=True)
    source_url: Mapped[Optional[str]] = mapped_column(nullable=True)
    content: Mapped[str] = mapped_column()  # Full document content
    file_hash: Mapped[Optional[str]] = mapped_column(nullable=True)  # For deduplication
    doc_type: Mapped[str] = mapped_column(default="text")  # pdf, text, markdown, etc.
    indexed: Mapped[bool] = mapped_column(default=False)  # Whether it's been indexed in Chroma

    chunks: Mapped[list["RagDocumentChunkOrm"]] = relationship(
        back_populates="document"
    )

    def to_dto(self) -> RagDocumentResponse:
        """Convert ORM to DTO."""
        chunk_dtos = [chunk.to_dto() for chunk in self.chunks]
        return RagDocumentResponse(
            id=self.id,
            title=self.title,
            file_path=self.file_path,
            source_url=self.source_url,
            doc_type=self.doc_type,
            indexed=self.indexed,
            created_at=self.created_at.timestamp(),
            updated_at=self.updated_at.timestamp(),
            chunks=chunk_dtos,
        )


class RagDocumentChunkOrm(Base):
    """Store document chunks for RAG retrieval."""
    __tablename__ = "rag_document_chunks"

    id: Mapped[uuid_pk]
    created_at: Mapped[created_at_type]
    document_id: Mapped[str] = mapped_column(ForeignKey("rag_documents.id"))
    chunk_index: Mapped[int] = mapped_column()  # Position in document
    content: Mapped[str] = mapped_column()  # Chunk text
    chroma_id: Mapped[Optional[str]] = mapped_column(nullable=True)  # Reference to Chroma embedding

    document: Mapped["RagDocumentOrm"] = relationship(back_populates="chunks")

    def to_dto(self) -> RagDocumentChunkResponse:
        """Convert ORM to DTO."""
        return RagDocumentChunkResponse(
            id=self.id,
            chunk_index=self.chunk_index,
            content=self.content,
            chroma_id=self.chroma_id,
        )
