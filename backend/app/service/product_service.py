from app.models import Product 
from app.db import PyObjectId
from bson import ObjectId


class ProductService:
    def __init__(self, collection):
        self.collection = collection

    async def get_product_by_id(self, id):
        document = await self.collection.find_one({"_id": ObjectId(id)})
        return Product(**document)

    async def fetch_all_products(self):
        products = []
        cursor = self.collection.find()
        async for document in cursor:
            product = Product(**document)
            products.append(product)
        return products

    async def create_product(self, product):
        result = await self.collection.insert_one(product.model_dump(exclude=["id"]))
        return PyObjectId(result.inserted_id)

    async def remove_product(self, id):
        result = await self.collection.delete_one({"_id": ObjectId(id)})
        return result.deleted_count == 1
