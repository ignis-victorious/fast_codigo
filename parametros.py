#
#  Import LIBRARIES
from fastapi import FastAPI, Path, Query

#  Import FILES
from models.models import Item

#  ...

app = FastAPI()


@app.get(path="/")
async def root() -> dict[str, str]:
    return {"message": "¡Hola, FastAPI!"}


@app.get(path="/items/")
async def read_items(skip: int = 0, limit: int = 10, q: str | None = None) -> dict[str, int | str]:
    results: dict[str, int | str] = {"skip": skip, "limit": limit}
    if q is not None:
        results["q"] = q
    return results


@app.get(path="/items/{item_id}")
async def read_item(
    item_id: int = Path(default=..., title="ID del item", ge=1),
    q: str | None = Query(default=None, min_length=3, max_length=50),
    size: float | None = Query(default=None, gt=0, lt=100),
) -> dict[str, int | str | float]:
    results: dict[str, int | str | float] = {"item_id": item_id}
    if q is not None:
        results["q"] = q
        # results.update({"q": q})
    if size is not None:
        results["size"] = size
        # results.update({"size": size})
    return results


# {"name": "erre", "description": "An item called Erre", "price": 88, "tax": 10}
@app.post(path="/items/")
async def create_item(item: Item) -> Item:
    return item


# Endpoint GET con ID
@app.get(path="/users/{user_id}")
async def read_user(user_id: int) -> dict[str, int]:
    return {"user_id": user_id}
