from datetime import datetime
from enum import Enum
from typing import Optional
from pydantic import BaseModel

class UserStatus(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    

class User(BaseModel):
    #Entidad de dominio : user
    id: str
    username: str
    email: str
    status: UserStatus=UserStatus.ACTIVE
    created_at: datetime

    def activate(self):
        #Comportamiento de dominio,es la de activar usuario
        self.status = UserStatus.ACTIVE

    def deactivate(self):
        #comportamiento de dominio,es la de desactivar usuario
        self.status = UserStatus.INACTIVE
    
    def is_active(self) -> bool:
        #comportamiento de dominio,es la de verificar si el usuario esta activo
        return self.status == UserStatus.ACTIVE

class UserCreate(BaseModel):
    username: str
    email: str

class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None
    status: Optional[UserStatus] = None