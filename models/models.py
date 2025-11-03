#
#  Import LIBRARIES
import re
from datetime import date

from pydantic import BaseModel, EmailStr, Field, HttpUrl, field_validator

#  Import FILES
#  ...


class DireccionEntrega(BaseModel):
    calle: str
    ciudad: str
    codigo_postal: str
    pais: str

    @field_validator(" codigo_postal")
    def validar_codigo_postal(cls, v: str) -> str:
        if not re.match(pattern=r"^\d{5)$", string=v):
            raise ValueError("El código postal debe tener 5 dígitos")
        return v


class Tarjeta(BaseModel):
    numero: str
    vencimiento: date
    cvv: str

    @field_validator("numero")
    def validar_numero_tarjeta(cls, v: str):
        # Eliminar espacios y guiones
        v = v.replace(" ", "").replace("-", "")
        if not v.isdigit() or len(v) not in [15, 16]:
            raise ValueError("Número de tarjeta inválido")
        return v


class Imagen(BaseModel):
    url: HttpUrl
    nombre: str

    @field_validator("nombre")
    def nombre_no_muy_largo(cls, v: str) -> str:
        if len(v) > 100:
            raise ValueError("El nombre de la imagen no puede tener más de 100 caracteres")
        return v


class Tag(BaseModel):
    id: int
    nombre: str


class Producto(BaseModel):
    nombre: str
    precio: float
    descripcion: str | None = None
    impuestos: float | None = None
    tags: list[Tag] = []
    imagenes: list[Imagen] = []

    def precio_con_impuestos(self) -> float:
        if self.impuestos is None:
            return self.precio
        return self.precio * (1 + self.impuestos)


class Usuario(BaseModel):
    nombre: str = Field(..., min_length=3)
    email: EmailStr
    telefono: str | None = None
    premium: bool = False
    direcciones: list[DireccionEntrega] = []
    metodo_pago: Tarjeta | None = None

    @field_validator("telefono")
    def validar_telefono(cls, v: str | None) -> None | str:
        if v is not None and not re.match(pattern=r"^\+\d{1,3}\d{9}$", string=v):
            raise ValueError("Formato de teléfono inválido (ej: +34123456789) ")
        return v


# class Usuario(BaseModel):
#     nombre: str = Field(default=..., min_length=3, max_length=50)
#     email: EmailStr
#     edad: int = Field(default=..., gt=0, lt=120)
#     codigo_postal: str

#     @field_validator("codigo_postal")
#     def validar_codigo_postal(cls, v: str) -> str:
#         if not re.match(pattern=r"^\d{5}$", string=v):
#             raise ValueError("El código postal debe tener 5 dígitos")
#         return v


# class Producto(BaseModel):
#     nombire: str
#     precio: float
#     disponible: bool = True
#     tags: list[str] = []
#     descripcion: str | None = None


# class Usuario(BaseModel):
#     nombre: str
#     edad: int
#     email: str
#     activo: bool = True
#     descripcion: str | None = None


# class Item(BaseModel):
#     name: str = Field(default=..., examples=["Smartphone"])
#     description: str | None = Field(default=None, examples=["Ultimo modelo con camara 12 pixels"])
#     price: float = Field(default=..., examples=[799.99])
#     tax: float | None = None

#     class Config:
#         schema_extra: dict[str, dict[str, str | float]] = {
#             "example": {"name": "Laptop", "description": "Potente laptop", "price": 1299.99}
#         }


# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None


class User(BaseModel):
    username: str
    full_name: str | None = None
