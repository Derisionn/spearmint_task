from fastapi import APIRouter
from services.mongo import get_db

router = APIRouter()


@router.get("/products")
async def get_products():
    """
    Return all products from the MongoDB collection.
    """
    db = get_db()
    collection = db["products"]

    products = []
    async for doc in collection.find({}):
        doc["id"] = str(doc.pop("_id"))
        products.append(doc)

    return products
