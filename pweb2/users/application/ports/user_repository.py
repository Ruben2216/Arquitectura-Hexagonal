from abc import ABC, abstractmethod
from typing import List, Optional
from pweb2.users.domain.usuario import User, UserCreate, UserUpdate


class UserRepository(ABC):
    """Puerto (interfaz) para el repositorio de usuarios"""
    
    @abstractmethod
    def save(self, user_data: UserCreate) -> User:
        """Guardar un nuevo usuario"""
        pass
    
    @abstractmethod
    def find_by_id(self, user_id: str) -> Optional[User]:
        """Buscar usuario por ID"""
        pass
    
    @abstractmethod
    def find_by_email(self, email: str) -> Optional[User]:
        """Buscar usuario por email"""
        pass
    
    @abstractmethod
    def find_all(self) -> List[User]:
        """Obtener todos los usuarios"""
        pass
    
    @abstractmethod
    def update(self, user_id: str, user_update: UserUpdate) -> Optional[User]:
        """Actualizar un usuario"""
        pass
    
    @abstractmethod
    def delete(self, user_id: str) -> bool:
        """Eliminar un usuario"""
        pass
    @abstractmethod
    def find_by_username(self, username: str) -> Optional[User]:
        """Buscar usuario por nombre de usuario"""
        pass
