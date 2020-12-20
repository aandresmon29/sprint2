from datetime import date
from pydantic import BaseModel

class DlIn(BaseModel):
    objetivo: str
    deadline: date

class DlOut(BaseModel):
    deadline: date