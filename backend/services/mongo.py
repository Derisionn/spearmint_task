import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import certifi

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017")
MONGODB_DB = os.getenv("MONGODB_DB", "spearmint")

client: AsyncIOMotorClient = None


def get_db():
    return client[MONGODB_DB]


async def connect_db():
    global client
    client = AsyncIOMotorClient(
        MONGODB_URI,
        tls=True,
        tlsAllowInvalidCertificates=True
    )
    print(f"Connected to MongoDB Atlas: {MONGODB_URI[:50]}...")


async def close_db():
    global client
    if client:
        client.close()
        print("MongoDB connection closed.")


async def query_products(filters: dict) -> list[dict]:
    """
    Build a MongoDB query from the extracted Gemini filters and return matching products.
    """
    db = get_db()
    collection = db["products"]

    mongo_query = {}

    if filters.get("category"):
        mongo_query["category"] = {"$regex": filters["category"], "$options": "i"}

    if filters.get("max_price") is not None:
        mongo_query["price"] = {"$lte": filters["max_price"]}

    if filters.get("brand"):
        mongo_query["brand"] = {"$regex": filters["brand"], "$options": "i"}

    if filters.get("feature"):
        mongo_query["features"] = {"$elemMatch": {"$regex": filters["feature"], "$options": "i"}}

    print(f"🔍 MongoDB query: {mongo_query}")

    cursor = collection.find(mongo_query)
    products = []
    async for doc in cursor:
        doc["id"] = str(doc.pop("_id"))
        products.append(doc)

    # If no specific filters matched anything, return all products
    if not products and not mongo_query:
        cursor = collection.find({})
        async for doc in cursor:
            doc["id"] = str(doc.pop("_id"))
            products.append(doc)

    return products
