from db.deadline_db import get_deadline
from db.entregas_db import get_entrega, update_entrega
from db.tareas_db import get_tarea
from models.tareas_models import TaskIn, TaskOut
from models.entregas_models import EntIn, EntOut
from models.deadline_models import DlIn, DlOut
import datetime
from fastapi import FastAPI
from fastapi import HTTPException
from routers.entregas_router import router as router_entregas
from routers.tareas_router import router as router_tareas
from routers.deadline_router import router as router_deadline


api = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost.tiangolo.com", "https://localhost.tiangolo.com","https://sprint2-g3m4-9.herokuapp.com",
    "http://localhost", "http://localhost:8080","https://proyectopyme-g3m4-9.herokuapp.com",
]
api.add_middleware(
    CORSMiddleware, allow_origins=origins,
    allow_credentials=True, allow_methods=["*"], allow_headers=["*"],
)

api.include_router(router_entregas)
api.include_router(router_tareas)
api.include_router(router_deadline)
