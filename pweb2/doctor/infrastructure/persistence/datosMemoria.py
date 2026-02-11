from typing import Dict, List, Optional
from datetime import datetime
from uuid import uuid4

from pweb2.doctor.domain.doctor import Doctor, DoctorCreate, DoctorUpdate
from pweb2.doctor.application.ports.doctor_repository import DoctorRepository


class InMemoryDoctorRepository(DoctorRepository):
    
    def __init__(self):
        self._doctores: Dict[str, Doctor] = {}
    
    def save(self, doctor_data: DoctorCreate) -> Doctor:
        doctor_id = str(uuid4())
        doctor = Doctor(
            id=doctor_id,
            nombre=doctor_data.nombre,
            especialidad=doctor_data.especialidad,
            created_at=datetime.now()
        )
        self._doctores[doctor_id] = doctor
        return doctor
    
    def find_by_id(self, doctor_id: str) -> Optional[Doctor]:
        return self._doctores.get(doctor_id)
    
    def find_by_nombre(self, nombre: str) -> Optional[Doctor]:
        for doctor in self._doctores.values():
            if doctor.nombre == nombre:
                return doctor
        return None
    
    def find_all(self) -> List[Doctor]:
        return list(self._doctores.values())
    
    def update(self, doctor_id: str, doctor_update: DoctorUpdate) -> Optional[Doctor]:
        doctor = self._doctores.get(doctor_id)
        if not doctor:
            return None
        
        if doctor_update.nombre is not None:
            doctor.nombre = doctor_update.nombre
        if doctor_update.especialidad is not None:
            doctor.especialidad = doctor_update.especialidad
        
        return doctor
    
    def delete(self, doctor_id: str) -> bool:
        if doctor_id in self._doctores:
            del self._doctores[doctor_id]
            return True
        return False
