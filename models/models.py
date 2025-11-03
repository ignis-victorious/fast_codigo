#
#  Import LIBRARIES
from pydantic import BaseModel, Field

#  Import FILES
#  ...


class Item(BaseModel):
    name: str = Field(default=..., examples=["Smartphone"])
    description: str | None = Field(default=None, examples=["Ultimo modelo con camara 12 pixels"])
    price: float = Field(default=..., examples=[799.99])
    tax: float | None = None

    class Config:
        schema_extra: dict[str, dict[str, str | float]] = {
            "example": {"name": "Laptop", "description": "Potente laptop", "price": 1299.99}
        }


# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None


class User(BaseModel):
    username: str
    full_name: str | None = None
