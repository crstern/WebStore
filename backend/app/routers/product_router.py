from typing import Annotated
from fastapi import APIRouter, Body, status
from app.models import Product
from app.db import products_collection
from app.service import ProductService

service = ProductService(products_collection)

router = APIRouter(
    prefix="/products"
)


@router.get("/")
async def get_all_products():
    products = await service.fetch_all_products()
    return {"prod": products}


@router.post(
    "/",
    response_description="Add new product",
    status_code=status.HTTP_201_CREATED,
    response_model_by_alias=False,
)
async def create_product(product: Product = Annotated[Product, Body(embed=True)]):
    """
    Insert a new product record.

    A unique `id` will be created and provided in the response.
    """
    created_product = await service.create_product(product)
    return create_product