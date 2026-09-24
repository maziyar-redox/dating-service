from pydantic import BaseModel

from datetime import date

class FinalizeListResponseSchema(BaseModel):
    status: bool
    date: date