#
#  Import LIBRARIES
from fastapi import FastAPI

#  Import FILES
from models.models import Usuario

#  ...


app = FastAPI()


@app.get(path="/")
async def root() -> dict[str, str]:
    return {"message": "¡Hola, FastAPI!"}


@app.post(path="/registro/")
async def registrar_usuario(usuario: Usuario) -> dict[str, str | Usuario]:
    # Aquí guardaríamos el usuario en la base de datos
    return {"mensaje": "Usuario registrado correctamente", "usuario": usuario}
