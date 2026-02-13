from typing import List, Optional
from pweb2.pedidos.domain.pedido import Pedido, PedidoCreate, PedidoUpdate
from pweb2.pedidos.application.ports.pedido_repository import PedidoRepository


class PedidoServicio:
    def __init__(self, repository: PedidoRepository):
        self.repository = repository

    def registrarPedido(self, pedidoData: PedidoCreate) -> Pedido:
        if not pedidoData.usuarioId or not pedidoData.descripcion or pedidoData.cantidad is None:
            raise ValueError("Usuario ID, descripcion y cantidad son obligatorios")
        
        if pedidoData.cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor a 0")
        
        return self.repository.save(pedidoData)
    
    def getPedido(self, pedidoId: str) -> Optional[Pedido]:
        return self.repository.findById(pedidoId)
    
    def getAllPedido(self) -> List[Pedido]:
        return self.repository.findAll()
    
    def getPedidosByUsuario(self, usuarioId: str) -> List[Pedido]:
        return self.repository.findByUsuarioId(usuarioId)
    
    def updatePedido(self, pedidoId: str, pedidoUpdate: PedidoUpdate) -> Optional[Pedido]:
        pedido = self.repository.findById(pedidoId)
        
        if not pedido:
            return None
        
        return self.repository.update(pedidoId, pedidoUpdate)
    
    def deletePedido(self, pedidoId: str) -> bool:
        return self.repository.delete(pedidoId)
