from fastapi import APIRouter, HTTPException
from models.producto_models import Producto
from services.producto_service import obtener_productos, obtener_producto_por_id, insertar_producto, actualizar_producto

router = APIRouter()

#Start api is available
@router.get("/productos-start/")
def start_productos():
    return {"message": "Welcome to productos services into de global API"}

#Get all products
@router.get("/productos", response_model=list)
async def obtener_productos_endpoint():
    productos = obtener_productos()
    return productos

#Get product by id
@router.get("/productos/{producto_id}", response_model=Producto)
def obtener_producto(producto_id: str):
    producto = obtener_producto_por_id(producto_id)
    if producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto

#Create product
@router.post("/productos/")
async def crear_producto(producto: Producto):
    return insertar_producto(producto)

#Update product
@router.put("/productos/{producto_id}")
async def editar_producto(producto_id: str, producto: Producto):
    return actualizar_producto(producto_id, producto)