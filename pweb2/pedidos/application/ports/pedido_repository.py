from abc import ABC, abstractmethod
from typing import List, Optional
from pweb2.pedidos.domain.pedido import Pedido, PedidoCreate, PedidoUpdate


class PedidoRepository(ABC):
    
    @abstractmethod
    def save(self, pedidoData: PedidoCreate) -> Pedido:
        pass
    
    @abstractmethod
    def findById(self, pedidoId: str) -> Optional[Pedido]:
        pass
    
    @abstractmethod
    def findByUsuarioId(self, usuarioId: str) -> List[Pedido]:
        pass
    
    @abstractmethod
    def findAll(self) -> List[Pedido]:
        pass
    
    @abstractmethod
    def update(self, pedidoId: str, pedidoUpdate: PedidoUpdate) -> Optional[Pedido]:
        pass
    
    @abstractmethod
    def delete(self, pedidoId: str) -> bool:
        pass
