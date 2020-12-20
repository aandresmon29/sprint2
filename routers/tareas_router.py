from fastapi import Depends, APIRouter, HTTPException
from db.tareas_db import delete_tarea, get_tarea, update_tarea
from models.tareas_models import TaskIn, TaskOut
from fastapi import HTTPException

router = APIRouter()

@router.get("/tareas/{nombre}")
async def get_ltareas(nombre: str):
    task_in_db = get_tarea(nombre)
    if task_in_db == None:
        raise HTTPException(status_code=404, detail="El objetivo no existe")
    task_out = (TaskOut(**task_in_db.dict()))
    return task_out

@router.put("/tareas/actualizar/")
async def put_ltareas(Task_ent: TaskIn):
    task_in_db = get_tarea(Task_ent.objetivo)
    if task_in_db == None:
        raise HTTPException(status_code=404, detail="El objetivo no existe")
    task_in_db = update_tarea(Task_ent)
    task_out = get_tarea(Task_ent.objetivo)
    return task_out

@router.delete("/tareas/eliminar/{nombre}")
async def del_ltareas(nombre: str):
    task_in_db = get_tarea(nombre)
    if task_in_db == None:
        raise HTTPException(status_code=404, detail="El objetivo no existe")
    task_in_db = delete_tarea(nombre)
    return task_in_db
