from datetime import date
from pydantic import BaseModel

class TaskIn(BaseModel):
    nombre: str

class TaskOut(BaseModel):
    nombre: str
    urgencia: str
    importancia: str
    deadline: date