from pydantic import BaseModel
from typing import Optional

class Producto(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
