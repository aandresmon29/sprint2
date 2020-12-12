from db.deadline_db import get_deadline
from db.entregas_db import get_entrega, update_entrega
from db.tareas_db import get_tarea
from models.tareas_models import TaskIn, TaskOut
from models.entregas_models import EntIn, EntOut
from models.deadline_models import DlIn, DlOut
import datetime
from fastapi import FastAPI
from fastapi import HTTPException

api = FastAPI()

@api.get("/entregas/{nombre}")
async def get_lentregas(nombre: str):
    task_in_db = get_entrega(nombre)
    dl_in_db = get_tarea(nombre)
    if task_in_db == None:
        raise HTTPException(status_code=404, detail="El objetivo no existe")
    task_out = (EntOut(**task_in_db.dict()) , TaskOut(**dl_in_db.dict()))
    return task_out

@api.put("/entregas/responsable/")
async def get_lentregas(Ent_ent: EntIn):
    task_in_db = get_entrega(Ent_ent.objetivo)
    if task_in_db == None:
        raise HTTPException(status_code=404, detail="El objetivo no existe")
    task_in_db = update_entrega(Ent_ent)
    task_out = get_entrega(Ent_ent.objetivo)
    return task_out