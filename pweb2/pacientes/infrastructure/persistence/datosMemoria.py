from typing import Dict, List, Optional
from datetime import datetime
from uuid import uuid4

from pweb2.pacientes.domain.paciente import paciente, pacienteCreate, pacienteUpdate
from pweb2.pacientes.application.ports.paciente_repository import PacienteRepository


class InMemoryPacienteRepository(PacienteRepository):
    """Implementación del repositorio en memoria """
    
    def __init__(self):
        self._pacientes: Dict[str, paciente] = {}
    
    def save(self, paciente_data: pacienteCreate) -> paciente:
        """Guardar un nuevo paciente en memoria"""
        paciente_id = str(uuid4())
        new_paciente = paciente(
            id=paciente_id,
            username=paciente_data.username,
            email=paciente_data.email,
            created_at=datetime.now()
        )
        self._pacientes[paciente_id] = new_paciente
        return new_paciente
    
    def find_by_id(self, paciente_id: str) -> Optional[paciente]:
        """Buscar usuario por ID"""
        return self._pacientes.get(paciente_id)
    
    def find_by_email(self, email: str) -> Optional[paciente]:
        """Buscar usuario por email"""
        for paciente in self._pacientes.values():
            if paciente.email == email:
                return paciente
        return None
    
    def find_all(self) -> List[paciente]:
        """Obtener todos los usuarios"""
        return list(self._pacientes.values())
    
    def update(self, paciente_id: str, paciente_update: pacienteUpdate) -> Optional[paciente]:
        """Actualizar un usuario"""
        paciente = self._pacientes.get(paciente_id)
        if not paciente:
            return None
        
        # Actualizar solo los campos que se enviaron
        if paciente_update.username is not None:
            paciente.username = paciente_update.username
        if paciente_update.email is not None:
            paciente.email = paciente_update.email
        if paciente_update.status is not None:
            paciente.status = paciente_update.status
        
        return paciente
    
    def delete(self, paciente_id: str) -> bool:
        """Eliminar un paciente"""
        if paciente_id in self._pacientes:
            del self._pacientes[paciente_id]
            return True
        return False

    def find_by_username(self, username: str) -> Optional[paciente]:
        """Buscar paciente por nombre de usuario"""
        for paciente in self._pacientes.values():
            if paciente.username == username:
                return paciente
        return None
