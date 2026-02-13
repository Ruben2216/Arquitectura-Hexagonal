from typing import Dict, List, Optional
from datetime import datetime
from uuid import uuid4

from pweb2.pedidos.domain.pedido import Pedido, PedidoCreate, PedidoUpdate
from pweb2.pedidos.application.ports.pedido_repository import PedidoRepository


class InMemoryPedidoRepository(PedidoRepository):
    
    def __init__(self):
        self._pedidos: Dict[str, Pedido] = {}
    
    def save(self, pedidoData: PedidoCreate) -> Pedido:
        pedidoId = str(uuid4())
        pedido = Pedido(
            id=pedidoId,
            usuarioId=pedidoData.usuarioId,
            descripcion=pedidoData.descripcion,
            cantidad=pedidoData.cantidad,
            createdAt=datetime.now()
        )
        self._pedidos[pedidoId] = pedido
        return pedido
    
    def findById(self, pedidoId: str) -> Optional[Pedido]:
        return self._pedidos.get(pedidoId)
    
    def findByUsuarioId(self, usuarioId: str) -> List[Pedido]:
        return [p for p in self._pedidos.values() if p.usuarioId == usuarioId]
    
    def findAll(self) -> List[Pedido]:
        return list(self._pedidos.values())
    
    def update(self, pedidoId: str, pedidoUpdate: PedidoUpdate) -> Optional[Pedido]:
        pedido = self._pedidos.get(pedidoId)
        if not pedido:
            return None
        
        if pedidoUpdate.usuarioId is not None:
            pedido.usuarioId = pedidoUpdate.usuarioId
        if pedidoUpdate.descripcion is not None:
            pedido.descripcion = pedidoUpdate.descripcion
        if pedidoUpdate.cantidad is not None:
            pedido.cantidad = pedidoUpdate.cantidad
        
        return pedido
    
    def delete(self, pedidoId: str) -> bool:
        if pedidoId in self._pedidos:
            del self._pedidos[pedidoId]
            return True
        return False
