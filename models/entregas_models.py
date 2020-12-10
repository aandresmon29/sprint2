from datetime import date
from pydantic import BaseModel

class EntIn(BaseModel):
    nombre: str

class EntOut(BaseModel):
    nombre: str
    responsable: str
    descripcion: str
    fecha: date
    version: int