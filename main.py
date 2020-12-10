from db.deadline_db import get_deadline
from db.entregas_db import get_entrega
from db.tareas_db import get_tarea
from models.tareas_models import TaskIn, TaskOut
from models.entregas_models import EntIn, EntOut
from models.deadline_models import DlIn, DlOut
import datetime
from fastapi import FastAPI
from fastapi import HTTPException

api = FastAPI()

@api.get("/objetivo/tareas/{nombre}")
async def get_ltareas(nombre: str):
    task_in_db = get_deadline(nombre)
    if task_in_db == None:
        raise HTTPException(status_code=404, detail="El objetivo no existe")
    task_out = DlOut(**task_in_db.dict())
    return task_out