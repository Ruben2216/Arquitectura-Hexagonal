from abc import ABC, abstractmethod
from typing import List, Optional
from pweb2.pacientes.domain.paciente import paciente, pacienteCreate, pacienteUpdate


class PacienteRepository(ABC):
    """Puerto (interfaz) para el repositorio de pacientes"""
    
    @abstractmethod
    def save(self, paciente_data: pacienteCreate) -> paciente:
        """Guardar un nuevo paciente"""
        pass
    
    @abstractmethod
    def find_by_id(self, paciente_id: str) -> Optional[paciente]:
        """Buscar paciente por ID"""
        pass
    
    @abstractmethod
    def find_by_email(self, email: str) -> Optional[paciente]:
        """Buscar paciente por email"""
        pass
    
    @abstractmethod
    def find_all(self) -> List[paciente]:
        """Obtener todos los pacientes"""
        pass
    
    @abstractmethod
    def update(self, paciente_id: str, paciente_update: pacienteUpdate) -> Optional[paciente]:
        """Actualizar un paciente"""
        pass
    
    @abstractmethod
    def delete(self, paciente_id: str) -> bool:
        """Eliminar un paciente"""
        pass
    @abstractmethod
    def find_by_username(self, username: str) -> Optional[paciente]:
        """Buscar paciente por nombre de usuario"""
        pass
