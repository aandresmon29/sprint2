from datetime import date
from typing import Dict
from pydantic import BaseModel

class TaskInDB(BaseModel):
    nombre: str
    urgencia: str
    importancia: str
    deadline: date

database_tareas= Dict[str , TaskInDB]

database_tareas={
   "Objetivo1" : TaskInDB(**{"nombre" : "tarea1",
                        "urgencia" : "alta",
                        "importancia" : "media",
                        "deadline" : "2020-12-11"}),
   "Objetivo2" : TaskInDB(**{"nombre" : "tarea2",
                        "urgencia" : "media",
                        "importancia" : "alta",
                        "deadline" : "2020-12-12"}),
}

def get_tarea(nombre: str):
    if nombre in database_tareas.keys():
        return database_tareas[nombre]
    else:
        return None

def update_tarea(task_in_db: TaskInDB):
    database_tareas[task_in_db.objetivo] = task_in_db
    return task_in_db

def delete_tarea(nombre: str):
    database_tareas.__delitem__(nombre)
    return "Tarea Eliminada"