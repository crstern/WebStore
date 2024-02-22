from typing import Annotated
from fastapi import APIRouter, Body, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from app.models import Product
from app.db import products_collection
from app.service import ProductService

service = ProductService(products_collection)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

router = APIRouter(
    prefix="/products"
)


@router.get("/")
async def get_all_products():
    products = await service.fetch_all_products()
    return {"data": products}

@router.get("/{id}", status_code=status.HTTP_200_OK)
async def get_one_product(id):
    product = await service.get_product_by_id(id)
    return {"data": product}


@router.post(
    "/",
    response_description="Add new product",
    status_code=status.HTTP_201_CREATED
)
async def create_product(token: Annotated[str, Depends(oauth2_scheme)], product: Product = Annotated[Product, Body(embed=True)]):
    """
    Insert a new product record.

    A unique `id` will be created and provided in the response.
    """
    result = await service.create_product(product)
    return {"data": result}

@router.delete("/{id}", response_description="Remove a product by id", status_code=status.HTTP_200_OK)
async def delete_produict(token: Annotated[str, Depends(oauth2_scheme)], id: str):
    product = await service.get_product_by_id(id)
    print(product)
    if not product:
        raise HTTPException(404, "Product not found")
    
    deleted = await service.remove_product(id)
    
    if deleted:
        return "Scuccess"
    raise HTTPException(400, "Something went wrong.")

    