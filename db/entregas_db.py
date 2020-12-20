from datetime import date
from typing import Dict
from pydantic import BaseModel

class EntInDB(BaseModel):
    nombre: str
    responsable: str
    descripcion: str
    fecha: date
    version: int

database_entregas= Dict[str , EntInDB]

database_entregas={
   "Objetivo1" : EntInDB(**{"nombre" : "entregable1",
                            "responsable" : "persona1",
                            "descripcion" : "Entrega para sprint #2",
                            "fecha" : "2020-12-11",
                            "version" : 1
                        }),
   "Objetivo2" : EntInDB(**{"nombre" : "entregable2",
                            "responsable" : "persona2",
                            "descripcion" : "Entrega final para sprint #2",
                            "fecha" : "2020-12-10",
                            "version" : 1
                        }),
}

def get_entrega(nombre: str):
    if nombre in database_entregas.keys():
        return database_entregas[nombre]
    else:
        return None

def update_entrega(ent_in_db: EntInDB):
    database_entregas[ent_in_db.objetivo] = ent_in_db
    return ent_in_db

def delete_entrega(nombre: str):
    database_entregas.__delitem__(nombre)
    return "Entrega Eliminada"