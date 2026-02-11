from typing import List, Optional
from pweb2.doctor.domain.doctor import Doctor, DoctorCreate, DoctorUpdate
from pweb2.doctor.application.ports.doctor_repository import DoctorRepository


class DoctorServicio:
    def __init__(self, repository: DoctorRepository):
        self.repository = repository

    def registrar_doctor(self, doctor_data: DoctorCreate) -> Doctor:
        if not doctor_data.nombre or not doctor_data.especialidad:
            raise ValueError("Nombre y especialidad son requeridos")
        
        existing_doctor = self.repository.find_by_nombre(doctor_data.nombre)
        if existing_doctor:
            raise ValueError(f"El doctor {doctor_data.nombre} ya esta registrado")
        
        return self.repository.save(doctor_data)
    
    def get_doctor(self, doctor_id: str) -> Optional[Doctor]:
        return self.repository.find_by_id(doctor_id)
    
    def get_all_doctor(self) -> List[Doctor]:
        return self.repository.find_all()
    
    def update_doctor(self, doctor_id: str, doctor_update: DoctorUpdate) -> Optional[Doctor]:
        doctor = self.repository.find_by_id(doctor_id)
        
        if not doctor:
            return None
        
        if doctor_update.nombre and doctor_update.nombre != doctor.nombre:
            existing_doctor = self.repository.find_by_nombre(doctor_update.nombre)
            if existing_doctor:
                raise ValueError(f"El doctor {doctor_update.nombre} ya existe")
        
        return self.repository.update(doctor_id, doctor_update)
    
    def delete_doctor(self, doctor_id: str) -> bool:
        return self.repository.delete(doctor_id)
