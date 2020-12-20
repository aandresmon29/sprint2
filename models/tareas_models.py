from datetime import date
from pydantic import BaseModel

class TaskIn(BaseModel):
    objetivo: str
    nombre: str
    urgencia: str
    importancia: str
    deadline: date

class TaskOut(BaseModel):
    nombre: str
    urgencia: str
    importancia: str
    deadline: date