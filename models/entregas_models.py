from datetime import date
from pydantic import BaseModel

class EntIn(BaseModel):
    objetivo: str
    nombre: str
    responsable: str
    descripcion: str
    version: int

class EntOut(BaseModel):
    nombre: str
    responsable: str
    descripcion: str
    fecha: date
    version: int