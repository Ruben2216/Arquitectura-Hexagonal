from typing import List, Optional
from pweb2.pacientes.domain.paciente import (paciente, pacienteCreate, pacienteUpdate, pacienteStatus)
from pweb2.pacientes.application.ports.paciente_repository import ( PacienteRepository)


class pacienteServicio:
    #Servicio de aplicacion, implementa la logica de negocio en casos de uso
    def __init__(self, repository:PacienteRepository):
        self.repository = repository

    def registrar_paciente (self, paciente_data:pacienteCreate) -> paciente:
        #Caso de uso, registrar un nuevo paciente
        if not paciente_data.username or not paciente_data.email:
            raise ValueError("Usuario y email son requeridos")
        
        #Verificar la unicidad del email
        existing_paciente= self.repository.find_by_email(paciente_data.email)
        if existing_paciente:
            raise ValueError(f"El email {paciente_data.email} ya esta registrado")
        
        #crear paciente
        return self.repository.save(paciente_data)
    

    def get_paciente(self, paciente_id:str) -> Optional[paciente]:
        #Caso de uso, obtener un paciente por su ID
        return self.repository.find_by_id(paciente_id)
    
    def get_all_paciente(self) -> list[paciente]:
        #Caso de uso, obtener todos los pacientes
        return self.repository.find_all()
    
    

    def update_paciente(self, paciente_id: str, paciente_update: pacienteUpdate) -> Optional[paciente]:
        #Caso de uso, actualizar un paciente
        paciente = self.repository.find_by_id(paciente_id)

        if not paciente:
            return None #en caso de no encontrar nada no retorna ningun valor
        
        if paciente_update.email != paciente.email:
            existing_paciente = self.repository.find_by_email(paciente_update.email)
            if existing_paciente:
                raise ValueError(f"El email {paciente_update.email} esta en uso")
        return self.repository.update(paciente_id, paciente_update)
    
    def delete_paciente(self, paciente_id:str) -> bool:
        #Caso de uso, eliminar un paciente por su ID
        return self.repository.delete(paciente_id)
    
    def deactivate_paciente(self, paciente_id: str) -> Optional[paciente]:
        #Caso de uso, desactivar un paciente
        paciente = self.repository.find_by_id(paciente_id)
        if not paciente:
            return None
        
        paciente.deactivate()
        return self.repository.update(paciente_id, pacienteUpdate(status=pacienteStatus.INACTIVE))
    
    def activate_paciente(self, paciente_id: str) -> Optional[paciente]:
        paciente = self.repository.find_by_id(paciente_id)
        if not paciente:
            return None
        paciente.activate()
        return self.repository.update(paciente_id, pacienteUpdate(status=pacienteStatus.ACTIVE))
    
    def get_paciente_stats(self) ->dict:

        pacientes=self.repository.find_all()
        total = len (pacientes)
        activate = len([p for p in pacientes if p.is_active()])

        return {
            "total_pacientes" : total, 
            "activate_pacientes": activate,
            "inactive_pacientes": total - activate
        }
                