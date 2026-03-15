from pydantic import BaseModel, Field, StrictStr, StrictBool
from typing import Optional, List
from uuid import UUID


class RagDocumentChunkResponse(BaseModel):
    """Response DTO for a RAG document chunk."""
    id: UUID = Field(description="Chunk ID")
    chunk_index: int = Field(description="Index position in the document")
    content: StrictStr = Field(description="Chunk text content")
    chroma_id: Optional[StrictStr] = Field(default=None, description="Reference to Chroma embedding ID")


class RagDocumentResponse(BaseModel):
    """Response DTO for RAG document."""
    id: UUID = Field(description="Document ID")
    title: StrictStr = Field(description="Document title")
    file_path: Optional[StrictStr] = Field(default=None, description="Source file path")
    source_url: Optional[StrictStr] = Field(default=None, description="Source URL")
    doc_type: StrictStr = Field(description="Document type (pdf, text, markdown, etc.)")
    indexed: StrictBool = Field(description="Whether document is indexed in Chroma")
    created_at: float = Field(description="Creation timestamp")
    updated_at: float = Field(description="Last update timestamp")
    chunks: List[RagDocumentChunkResponse] = Field(default_factory=list, description="Document chunks")


class RagDocumentRequest(BaseModel):
    """Request DTO for uploading RAG document."""
    title: StrictStr = Field(description="Document title")
    file_path: Optional[StrictStr] = Field(default=None, description="Source file path")
    source_url: Optional[StrictStr] = Field(default=None, description="Source URL")
    content: StrictStr = Field(description="Document content")
    doc_type: StrictStr = Field(default="text", description="Document type (pdf, text, markdown, etc.)")
