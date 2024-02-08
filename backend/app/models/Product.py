from pydantic import BaseModel

class Product(BaseModel):
    name: str
    description: str | None = None
    price: float | None = None
    