# CodeX Database Schema Extensions

## Overview
This document describes the new database tables added to support ngspice circuit simulations and RAG (Retrieval-Augmented Generation) document storage.

## New ORM Models and Tables

### 1. NgspiceCircuitOrm - `ngspice_circuits` Table
Stores SPICE netlists and circuit definitions for electrical simulations.

**Fields:**
- `id` (UUID, PK): Unique circuit identifier
- `created_at` (DateTime): Creation timestamp
- `updated_at` (DateTime): Last modification timestamp
- `name` (String): Circuit name
- `netlist` (String): SPICE netlist content
- `description` (String, Nullable): Optional circuit description
- `user_id` (String, FK): Reference to Users table
- `conversation_id` (String, FK, Nullable): Reference to Conversations table

**Relationships:**
- `user`: Many-to-One relationship to UsersOrm
- `simulations`: One-to-Many relationship to NgspiceSimulationOrm

**DTO:** `NgspiceCircuitResponse`, `NgspiceCircuitRequest`

---

### 2. NgspiceSimulationOrm - `ngspice_simulations` Table
Stores ngspice simulation runs and their results.

**Fields:**
- `id` (UUID, PK): Unique simulation run ID
- `created_at` (DateTime): Execution timestamp
- `circuit_id` (String, FK): Reference to NgspiceCircuitOrm
- `sim_type` (String): Simulation type (transient, ac, dc, sp, etc.)
- `parameters` (String, JSON-serialized): Simulation parameters (voltage levels, time intervals, frequencies, etc.)
- `raw_output` (String, Nullable): Raw simulation output from ngspice
- `success` (Boolean): Whether simulation completed successfully
- `error_message` (String, Nullable): Error message if simulation failed
- `execution_time_ms` (Integer): Execution time in milliseconds

**Relationships:**
- `circuit`: Many-to-One relationship to NgspiceCircuitOrm

**DTO:** `NgspiceSimulationResponse`, `NgspiceSimulationRequest`

---

### 3. RagDocumentOrm - `rag_documents` Table
Stores RAG documents for semantic search and retrieval.

**Fields:**
- `id` (UUID, PK): Unique document ID
- `created_at` (DateTime): Upload/creation timestamp
- `updated_at` (DateTime): Last modification timestamp
- `title` (String): Document title
- `file_path` (String, Nullable): Source file path
- `source_url` (String, Nullable): Source URL if document is from web
- `content` (String): Full document content
- `file_hash` (String, Nullable): Hash for deduplication
- `doc_type` (String, Default: "text"): Document type (pdf, text, markdown, etc.)
- `indexed` (Boolean, Default: False): Whether indexed in Chroma vector DB

**Relationships:**
- `chunks`: One-to-Many relationship to RagDocumentChunkOrm (cascading)

**DTO:** `RagDocumentResponse`, `RagDocumentRequest`

---

### 4. RagDocumentChunkOrm - `rag_document_chunks` Table
Stores document chunks for semantic search and RAG retrieval.

**Fields:**
- `id` (UUID, PK): Unique chunk ID
- `created_at` (DateTime): Creation timestamp
- `document_id` (String, FK): Reference to RagDocumentOrm
- `chunk_index` (Integer): Position/order within document
- `content` (String): Chunk text content
- `chroma_id` (String, Nullable): Reference to Chroma vector DB embedding ID

**Relationships:**
- `document`: Many-to-One relationship to RagDocumentOrm

**DTO:** `RagDocumentChunkResponse`

---

## Schema Relationships Diagram

```
UsersOrm
├── conversations (1:N) → ConversationsOrm
├── valid_token (1:1) → TokensOrm
└── ngspice_circuits (1:N) → NgspiceCircuitOrm
    └── simulations (1:N) → NgspiceSimulationOrm

ConversationsOrm
├── user (N:1) → UsersOrm
├── llm_model (N:1) → LlmModelsOrm
├── messages (1:N) → MessagesOrm
└── ngspice_circuits (1:N) → NgspiceCircuitOrm (via conversation_id)

RagDocumentOrm
└── chunks (1:N) → RagDocumentChunkOrm
```

---

## Implementation Details

### ORM Model Imports
All new ORM models follow the existing async SQLAlchemy pattern:
- Use `Mapped[type]` annotations for typed columns
- Implement `to_dto()` method for DTO conversions
- Support bidirectional relationships with `back_populates`

### DTO Conversions
- **NgspiceSimulationOrm.to_dto()**: Deserializes JSON parameters using `json.loads()`
- **RagDocumentOrm.to_dto()**: Recursively converts chunks using `chunk.to_dto()`
- All DTOs use Pydantic `BaseModel` with strict field typing

### Table Creation
Tables are automatically created by SQLAlchemy when `Base.metadata.create_all(engine)` is called in:
- `src/persistence/impl/database/orm.py` - Application startup
- Tests (async version via `await conn.run_sync(Base.metadata.create_all)`)

---

## API Endpoints (To Be Implemented)

### Ngspice Circuits
```
POST   /ngspice/circuits              - Create new circuit
GET    /ngspice/circuits              - List user's circuits
GET    /ngspice/circuits/{id}         - Get circuit details
PUT    /ngspice/circuits/{id}         - Update circuit
DELETE /ngspice/circuits/{id}         - Delete circuit

POST   /ngspice/circuits/{id}/simulate - Run simulation
GET    /ngspice/simulations/{id}      - Get simulation results
GET    /ngspice/circuits/{id}/simulations - List circuit simulations
```

### RAG Documents
```
POST   /rag/documents                 - Upload document
GET    /rag/documents                 - List documents
GET    /rag/documents/{id}            - Get document details
DELETE /rag/documents/{id}            - Delete document

POST   /rag/documents/{id}/index      - Index document in Chroma
POST   /rag/search                    - Semantic search
```

---

## Migration Notes

- **No Alembic migrations required**: Tables are created via `Base.metadata.create_all()`
- **Backward compatible**: Existing tables unchanged; new tables added separately
- **Async support**: All models work with async SQLAlchemy engine (`postgresql+asyncpg://`)
- **Test database**: Uses `sqlite+aiosqlite:///:memory:` for async test compatibility

---

## Files Modified

1. **src/persistence/impl/database/models.py**
   - Added: NgspiceCircuitOrm, NgspiceSimulationOrm, RagDocumentOrm, RagDocumentChunkOrm
   - Updated: UsersOrm with `ngspice_circuits` relationship

2. **src/core/dtos/__init__.py**
   - Exported new DTOs: NgspiceCircuitResponse, NgspiceCircuitRequest, NgspiceSimulationResponse, NgspiceSimulationRequest, RagDocumentResponse, RagDocumentRequest, RagDocumentChunkResponse

3. **New DTO files:**
   - src/core/dtos/ngspice_circuit_response.py
   - src/core/dtos/ngspice_simulation_response.py
   - src/core/dtos/rag_document_response.py
