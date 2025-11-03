#
#  Import LIBRARIES
from fastapi import FastAPI

#  Import FILES
from models.models import Producto

#  ...


app = FastAPI()


@app.get(path="/")
async def root() -> dict[str, str]:
    return {"message": "¡Hola, FastAPI!"}


# {"nombre": "Smartphone","precio": 899.99,"descripcion": "Último modelo con cámara de alta resolución","impuestos": 0.16,"tags": [{"id": 1, "nombre": "electrónica"}, {"id": 2, "nombre": "smartphones"}],"imagenes": [{"url": "https://ejemplo.com/imagen1.jpg","nombre": "Vista frontal"}, {"url": "https://ejemplo.com/imagen2.jpg","nombre": "Vista trasera"}]}
@app.post(path="/productos/")
def crear_producto(producto: Producto) -> dict[str, str | Producto | float]:
    precio_final: float = producto.precio_con_impuestos()
    return {
        "mensaje": "Producto recibido correctamente",
        "producto": producto,
        "precio_con_impuestos": round(number=precio_final, ndigits=2),
    }
