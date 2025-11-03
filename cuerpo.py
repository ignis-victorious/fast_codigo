#
#  Import LIBRARIES
from fastapi import Body, FastAPI

#  Import FILES
from models.models import Item, User

#  ...

description: str = "La description de la app"

app = FastAPI(
    title="Un Aplicación Increíble",
    description=description,
    version="0.1.0",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Mi Nombre",
        "ur1": "http://example.com/contact/",
        "email": "mi@email.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)


@app.get(path="/")
async def root() -> dict[str, str]:
    return {"message": "¡Hola, esto es cuerpo.py!"}


# {"item": {"name": "Emme","description": "The usual Emme appliance","price": 110,"tax": 10},"user": {"username": "Raff","full_name": "Raff Rem"}}
@app.post(path="/items/{item_id}")
async def create_item_id(item_id: int, item: Item, user: User) -> dict[str, int | Item | User]:
    return {"item_id": item_id, "item": item, "user": user}


# {"name": "erre", "description": "An item called Erre", "price": 88, "tax": 10}
# {"name": "Monitor", "description": "Pantalla de 24 pulgadas","price": 299.99, "tax": 21.6}
@app.post(path="/items/")
async def create_item(item: Item) -> Item:
    return item


@app.put(
    path="/items/{item_id}",
    summary="Obtener un item específico",
    description="""
        Recupera un item por su ID.
        Esta operación requiere que el item exista en la base de datos.
        """,
    response_description="El item solicitado",
    tags=["items"],
    response_model=Item,
    status_code=200,
    deprecated=False,
)
async def update_item(
    item_id: int,
    item: Item = Body(
        default=...,
        example={
            "name": "Smartphone",
            "description": "Último modelo con cámara de alta resolución",
            "price": 799.99,
            "tax": 13.99,
        },
    ),
) -> dict[str, int | Item]:
    return {"item_id": item_id, "item": item}
