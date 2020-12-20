from fastapi import Depends, APIRouter, HTTPException
from db.deadline_db import get_deadline, update_deadline
from models.deadline_models import DlIn, DlOut
from fastapi import HTTPException

router = APIRouter()

@router.get("/deadline/{nombre}")
async def get_ldeadline(nombre: str):
    dl_in_db = get_deadline(nombre)
    if dl_in_db == None:
        raise HTTPException(status_code=404, detail="El objetivo no existe")
    dl_out = (DlOut(**dl_in_db.dict()))
    return dl_out

@router.put("/deadline/actualizar/")
async def get_ltareas(Dl_ent: DlIn):
    dl_in_db = get_deadline(Dl_ent.objetivo)
    if dl_in_db == None:
        raise HTTPException(status_code=404, detail="El objetivo no existe")
    dl_in_db = update_deadline(Dl_ent)
    dl_out = get_deadline(Dl_ent.objetivo)
    return dl_out