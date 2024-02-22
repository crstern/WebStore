from app.models import Product 

class ProductService:
    def __init__(self, collection):
        self.collection = collection

    async def fetch_one_product_by_name(self, id):
        document = await self.collection.find_one({"id": id})
        return document

    async def fetch_all_products(self):
        products = []
        cursor = self.collection.find()
        async for document in cursor:
            product = Product(**document)
            products.append(product)
        return products

    async def create_product(self, product):
        result = await self.collection.insert_one(product.model_dump(exclude=["id"]))
        return {"inserted_id": result.inserted_id}

    async def remove_product(self, id):
        pass