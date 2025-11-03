#
#  Import LIBRARIES
from fastapi import FastAPI

#  Import FILES
from models.models import Producto, Usuario

#  ...


app = FastAPI()


@app.get(path="/")
async def root() -> dict[str, str]:
    return {"message": "¡Hola, FastAPI!"}


#  {"nombre": "Emme Manny","email": "Emme@example.com","edad": 88,"codigo_postal": "12345"}
@app.post(path="/usuarios/")
def crear_usuario(usuario: Usuario) -> dict[str, str | Usuario]:
    # Aquí ya llega el objeto validado
    return {"mensaje": "Usuario creado exitosamente", "datos": usuario}


# {"nombire": "Laptop","precio": 999.99,"tags": ["electrónica", "computadoras"]}
# {"nombire": "TV","precio": 999.99,"disponible": true,"tags": ["TV", "Domestic Appliance"],"descripcion": "A standard TV for the whole family to watch"}
@app.post(path="/productos/")
async def crear_producto(producto: Producto) -> dict[str, str | Producto]:
    # Aquí normalmente guardaríamos el producto en una base de datos
    return {"mensaje": "Producto creado", "producto": producto}
