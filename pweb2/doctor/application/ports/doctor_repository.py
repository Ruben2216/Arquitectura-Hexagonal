from abc import ABC, abstractmethod
from typing import List, Optional
from pweb2.doctor.domain.doctor import Doctor, DoctorCreate, DoctorUpdate


class DoctorRepository(ABC):
    
    @abstractmethod
    def save(self, doctor_data: DoctorCreate) -> Doctor:
        pass
    
    @abstractmethod
    def find_by_id(self, doctor_id: str) -> Optional[Doctor]:
        pass
    
    @abstractmethod
    def find_by_nombre(self, nombre: str) -> Optional[Doctor]:
        pass
    
    @abstractmethod
    def find_all(self) -> List[Doctor]:
        pass
    
    @abstractmethod
    def update(self, doctor_id: str, doctor_update: DoctorUpdate) -> Optional[Doctor]:
        pass
    
    @abstractmethod
    def delete(self, doctor_id: str) -> bool:
        pass
