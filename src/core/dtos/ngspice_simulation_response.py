from pydantic import BaseModel, Field, StrictStr, StrictBool
from typing import Optional, Dict, Any
from uuid import UUID


class NgspiceSimulationResponse(BaseModel):
    """Response DTO for ngspice simulation run."""
    id: UUID = Field(description="Simulation ID")
    circuit_id: UUID = Field(description="Associated circuit ID")
    sim_type: StrictStr = Field(description="Simulation type (transient, ac, dc, etc.)")
    parameters: Dict[str, Any] = Field(description="Simulation parameters")
    success: StrictBool = Field(description="Whether simulation completed successfully")
    raw_output: Optional[StrictStr] = Field(default=None, description="Raw simulation output")
    error_message: Optional[StrictStr] = Field(default=None, description="Error message if simulation failed")
    execution_time_ms: int = Field(description="Execution time in milliseconds")
    created_at: float = Field(description="Creation timestamp")


class NgspiceSimulationRequest(BaseModel):
    """Request DTO for running ngspice simulation."""
    circuit_id: UUID = Field(description="Circuit to simulate")
    sim_type: StrictStr = Field(description="Simulation type (transient, ac, dc, etc.)")
    parameters: Dict[str, Any] = Field(description="Simulation parameters")
