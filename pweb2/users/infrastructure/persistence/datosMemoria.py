from typing import Dict, List, Optional
from datetime import datetime
from uuid import uuid4

from pweb2.users.domain.usuario import User, UserCreate, UserUpdate
from pweb2.users.application.ports.user_repository import UserRepository


class InMemoryUserRepository(UserRepository):
    """Implementación del repositorio en memoria """
    
    def __init__(self):
        self._users: Dict[str, User] = {}
    
    def save(self, user_data: UserCreate) -> User:
        """Guardar un nuevo usuario en memoria"""
        user_id = str(uuid4())
        user = User(
            id=user_id,
            username=user_data.username,
            email=user_data.email,
            created_at=datetime.now()
        )
        self._users[user_id] = user
        return user
    
    def find_by_id(self, user_id: str) -> Optional[User]:
        """Buscar usuario por ID"""
        return self._users.get(user_id)
    
    def find_by_email(self, email: str) -> Optional[User]:
        """Buscar usuario por email"""
        for user in self._users.values():
            if user.email == email:
                return user
        return None
    
    def find_all(self) -> List[User]:
        """Obtener todos los usuarios"""
        return list(self._users.values())
    
    def update(self, user_id: str, user_update: UserUpdate) -> Optional[User]:
        """Actualizar un usuario"""
        user = self._users.get(user_id)
        if not user:
            return None
        
        # Actualizar solo los campos que se enviaron
        if user_update.username is not None:
            user.username = user_update.username
        if user_update.email is not None:
            user.email = user_update.email
        if user_update.status is not None:
            user.status = user_update.status
        
        return user
    
    def delete(self, user_id: str) -> bool:
        """Eliminar un usuario"""
        if user_id in self._users:
            del self._users[user_id]
            return True
        return False

    def find_by_username(self, username: str) -> Optional[User]:
        """Buscar usuario por nombre de usuario"""
        for user in self._users.values():
            if user.username == username:
                return user
        return None
