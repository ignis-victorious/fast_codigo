#
#  Import LIBRARIES
from fastapi import FastAPI

#  Import FILES
#  ...

app = FastAPI(
    title="Mi Primera API",
    description="Aprendiendo FastAPI",
    version="0.1.0",
)


@app.get(path="/")
async def root() -> dict[str, str]:
    return {"message": "¡Hola, FastAPI!"}


# Endpoint GET
@app.get(path="/items/")
async def read_items() -> list[dict[str, str]]:
    return [{"name": "Item 1"}, {"name": "Item 2"}]


# Endpoint GET con ID
@app.get(path="/items/{item_id}")
async def read_item(item_id: int) -> dict[str, int | str]:
    return {"item_id": item_id, "name": f"Item {item_id} "}


# Endpoint POST
@app.post(path="/items/")
async def create_item(name: str) -> dict[str, str | bool]:
    return {"name": name, "created": True}


# Endpoint PUT
@app.put(path="/items/{item_id}")
async def update_item(item_id: int, name: str) -> dict[str, int | str | bool]:
    return {"item_id": item_id, "name": name, "updated": True}


# Endpoint DELETE
@app.delete(path="/items/{item_id}")
async def delete_item(item_id: int) -> dict[str, int | bool]:
    return {"item_id": item_id, "deleted": True}


# # Para ejecutar: uvicorn main:app --reload *---* FOR DEPLOYMENT ONLY
# if __name__ == "__main__":
#     uvicorn.run(app="main:app", host="0.0.0.0", port=8000, reload=True)


#
#  Import LIBRARIES
#  Import FILES
#  ...
