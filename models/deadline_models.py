from datetime import date
from pydantic import BaseModel

class DlIn(BaseModel):
    deadline: date

class DlOut(BaseModel):
    deadline: date