from datetime import datetime
from enum import Enum
from typing import Optional
from pydantic import BaseModel

class pacienteStatus(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    

class paciente(BaseModel):
    #Entidad de dominio : paciente
    id: str
    username: str
    email: str
    status: pacienteStatus=pacienteStatus.ACTIVE
    created_at: datetime

    def activate(self):
        #Comportamiento de dominio,es la de activar usuario
        self.status = pacienteStatus.ACTIVE

    def deactivate(self):
        #comportamiento de dominio,es la de desactivar usuario
        self.status = pacienteStatus.INACTIVE
    
    def is_active(self) -> bool:
        #comportamiento de dominio,es la de verificar si el usuario esta activo
        return self.status == pacienteStatus.ACTIVE

class pacienteCreate(BaseModel):
    username: str
    email: str

class pacienteUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None
    status: Optional[pacienteStatus] = None