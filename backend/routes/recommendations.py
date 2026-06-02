from fastapi import APIRouter
from utils.models import RecommendationRequest
from services.gemini import extract_filters
from services.mongo import query_products

router = APIRouter()


@router.post("/recommendations")
async def get_recommendations(body: RecommendationRequest):
    """
    1. Accept a natural language query from the frontend.
    2. Send it to Gemini to extract structured filters (category, max_price, brand, feature).
    3. Use those filters to query MongoDB for matching products.
    4. Return the products to the frontend.
    """
    user_query = body.query

    # Step 1: Use Gemini to extract structured filters
    filters = await extract_filters(user_query)

    # Step 2: Query MongoDB with the extracted filters
    products = await query_products(filters)

    return {
        "query": user_query,
        "filters": filters,
        "products": products,
        "count": len(products)
    }
