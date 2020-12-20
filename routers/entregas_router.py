from fastapi import Depends, APIRouter, HTTPException
from db.entregas_db import get_entrega, update_entrega
from models.entregas_models import EntIn, EntOut
from fastapi import HTTPException

router = APIRouter()

@router.get("/entregas/{nombre}")
async def get_lentregas(nombre: str):
    ent_in_db = get_entrega(nombre)
    if ent_in_db == None:
        raise HTTPException(status_code=404, detail="El objetivo no existe")
    ent_out = (EntOut(**ent_in_db.dict()))
    return ent_out

@router.put("/entregas/responsable/")
async def get_lentregas(Ent_ent: EntIn):
    ent_in_db = get_entrega(Ent_ent.objetivo)
    if ent_in_db == None:
        raise HTTPException(status_code=404, detail="El objetivo no existe")
    ent_in_db = update_entrega(Ent_ent)
    ent_out = get_entrega(Ent_ent.objetivo)
    return ent_out
