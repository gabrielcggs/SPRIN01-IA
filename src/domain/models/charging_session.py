from pydantic import BaseModel


class ChargingSession(BaseModel):

    user_id: int
    duration_minutes: int
    energy_kwh: float
    total_cost: float
