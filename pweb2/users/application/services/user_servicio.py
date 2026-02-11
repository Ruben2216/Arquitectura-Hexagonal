from typing import List, Optional
from pweb2.users.domain.usuario import (User, UserCreate, UserUpdate, UserStatus)
from pweb2.users.application.ports.user_repository import ( UserRepository)


class UserServicio:
    #Servicio de aplicacion, implementa la logica de negocio en casos de uso
    def __init__(self, repository:UserRepository):
        self.repository = repository

    def registrar_User (self, user_data:UserCreate) -> User:
        #Caso de uso, registrar un nuevo usuario
        if not user_data.username or not user_data.email:
            raise ValueError("Usuario y email son requeridos")
        
        #Verificar la unicidad del email
        existing_user= self.repository.find_by_email(user_data.email)
        if existing_user:
            raise ValueError(f"El email {user_data.email} ya esta registrado")
        
        #crear usuario
        return self.repository.save(user_data)
    

    def get_user(self, user_id:str) -> Optional[User]:
        #Caso de uso, obtener un usuario por su ID
        return self.repository.find_by_id(user_id)
    
    def get_all_user(self) -> list[User]:
        #Caso de uso, obtener todos los usuarios
        return self.repository.find_all()
    
    

    def update_user(self, user_id: str, user_update: UserUpdate) -> Optional[User]:
        #Caso de uso, obtener todos los usuarios
        user = self.repository.find_by_id(user_id)

        if not user:
            return None #en caso de no encontrar nada no retorna ningun valor
        
        if user_update.email != user.email:
            existing_user = self.repository.find_by_email(user_update.email)
            if existing_user:
                raise ValueError(f"El email {user_update.email} esta en uso")
        return self.repository.update(user_id, user_update)
    
    def delete_user(self, user_id:str) -> bool:
        #Caso de uso, eliminar un usuario por su ID
        return self.repository.delete(user_id)
    
    def deactivate_user(self, user_id: str) -> Optional[User]:
        #Caso de uso, desactivar un usuario
        user = self.repository.find_by_id(user_id)
        if not user:
            return None
        
        user.deactivate()
        return self.repository.update(user_id, UserUpdate(status=UserStatus.INACTIVE))
    
    def activate_user(self, user_id: str) -> Optional[User]:
        user = self.repository.find_by_id(user_id)
        if not user:
            return None
        user.activate()
        return self.repository.update(user_id, UserUpdate(status=UserStatus.ACTIVE))
    
    def get_user_stats(self) ->dict:

        users=self.repository.find_all()
        total = len (users)
        activate = len([u for u in users if u.is_active()])

        return {
            "total_users" : total, 
            "activate_users": activate,
            "inactive_users": total - activate
        }
                