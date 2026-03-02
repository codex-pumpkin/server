from pydantic import BaseModel, Field, StrictStr
from typing import Optional
from uuid import UUID


class NgspiceCircuitResponse(BaseModel):
    """Response DTO for ngspice circuit."""
    id: UUID = Field(description="Circuit ID")
    name: StrictStr = Field(description="Circuit name")
    netlist: StrictStr = Field(description="SPICE netlist content")
    description: Optional[StrictStr] = Field(default=None, description="Circuit description")
    created_at: float = Field(description="Creation timestamp")
    updated_at: float = Field(description="Last update timestamp")
    user_id: UUID = Field(description="User who owns this circuit")
    conversation_id: Optional[UUID] = Field(default=None, description="Associated conversation ID")


class NgspiceCircuitRequest(BaseModel):
    """Request DTO for creating/updating ngspice circuit."""
    name: StrictStr = Field(description="Circuit name")
    netlist: StrictStr = Field(description="SPICE netlist content")
    description: Optional[StrictStr] = Field(default=None, description="Circuit description")
    conversation_id: Optional[UUID] = Field(default=None, description="Associated conversation ID")
