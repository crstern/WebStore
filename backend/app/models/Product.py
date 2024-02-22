from pydantic import BaseModel, Field
from bson import ObjectId
from app.db import PyObjectId

class Product(BaseModel):
    name: str
    description: str | None = None
    price: float | None = None
    id: PyObjectId | None = Field(default_factory=PyObjectId, alias="_id")
    