
from pydantic import BaseModel, Field

class AnalyticsRequest(BaseModel):
    period_of_days:int = Field(ge=1)
    time_interval_minutes:int = Field(ge=1)