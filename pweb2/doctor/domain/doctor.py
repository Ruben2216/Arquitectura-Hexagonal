from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class Doctor(BaseModel):
    id: str
    nombre: str
    especialidad: str
    created_at: datetime

class DoctorCreate(BaseModel):
    nombre: str
    especialidad: str

class DoctorUpdate(BaseModel):
    nombre: Optional[str] = None
    especialidad: Optional[str] = None
