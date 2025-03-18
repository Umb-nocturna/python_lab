from db.database import database
from bson import ObjectId
from models.producto_models import Producto

#Obtener toos los productos
def obtener_productos():
    collection = database.get_collection("productos")  # Selecciona la colección "productos"
    productos = list(collection.find({}, {"_id": 0}))  # Excluye "_id"
    return productos

#Obtener producto por id
def obtener_producto_por_id(producto_id: str):
    collection = database.get_collection("productos")
    try:
        obj_id = ObjectId(producto_id)
    except:
        return None

    producto = collection.find_one({"_id": obj_id})

    if producto:
        return Producto(
            id=str(producto["_id"]),
            name=producto["name"],
            description=str(producto["description"]),
            price=producto["price"]
        )
    return None

#Insertar producto
def insertar_producto(producto: Producto):
    collection = database.get_collection("productos")
    # Convertimos el modelo Pydantic a un diccionario
    producto_dict = producto.dict()
    resultado = collection.insert_one(producto_dict)
    return {"id": str(resultado.inserted_id), "mensaje": "Producto insertado correctamente"}

#Actualizar producto
def actualizar_producto(producto_id: str, producto: Producto):
    collection = database.get_collection("productos")
    update_data = {}
    # Convertir el modelo en diccionario y eliminar valores `None`
    #update_data = {k: v for k, v in producto.dict().items() if v is not None}
    # Agregar solo los campos que no sean None
    producto_dict = producto.dict()
    for key, value in producto_dict.items():
        if value is not None:
            update_data[key] = value

    if not update_data:
        return {"mensaje": "No hay datos para actualizar"}

    # Buscar y actualizar el documento
    resultado = collection.update_one({"_id": ObjectId(producto_id)}, {"$set": update_data})
    print(resultado)

    if resultado.matched_count == 0:
        return {"mensaje": "Producto no encontrado"}
    
    return {"mensaje": "Producto actualizado correctamente"}