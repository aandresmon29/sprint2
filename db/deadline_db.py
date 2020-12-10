from datetime import date
from typing import Dict
from pydantic import BaseModel

class DlInDB(BaseModel):
    deadline: date

database_deadline= Dict[str , DlInDB]

database_deadline={
   "Objetivo1" : DlInDB(**{"deadline" : 2020-12-12
                        }),
   "Objetivo2" : DlInDB(**{"deadline" : 2020-12-13
                        }),
}

def get_deadline(nombre: str):
    if nombre in database_deadline.keys():
        return database_deadline[nombre]
    else:
        return None