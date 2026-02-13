from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class Pedido(BaseModel):
    id: str
    usuarioId: str
    descripcion: str
    cantidad: int
    createdAt: datetime

class PedidoCreate(BaseModel):
    usuarioId: str
    descripcion: str
    cantidad: int

class PedidoUpdate(BaseModel):
    usuarioId: Optional[str] = None
    descripcion: Optional[str] = None
    cantidad: Optional[int] = None
