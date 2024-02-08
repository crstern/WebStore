from fastapi import APIRouter
from app.models import Product


router = APIRouter(
    prefix="/products"
)

@router.get("/")
async def read_root():
    p = Product(name="Ceva produs nush")
    return {"prod": p}
