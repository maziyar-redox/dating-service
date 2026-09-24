from pydantic import BaseModel

from datetime import date

class FinalizeListRequestSchema(BaseModel):
    phase_one: int
    phase_two: int
    phase_date: date