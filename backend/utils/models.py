from pydantic import BaseModel, Field
from typing import Optional
from bson import ObjectId


class Product(BaseModel):
    id: Optional[str] = None
    name: str
    price: float
    category: str
    description: str
    brand: Optional[str] = None
    features: Optional[list[str]] = []

    class Config:
        # Allow populating from MongoDB _id field
        populate_by_name = True


class RecommendationRequest(BaseModel):
    query: str = Field(..., description="Natural language user preference, e.g. 'I want a phone under $500'")


class GeminiFilters(BaseModel):
    category: Optional[str] = None
    max_price: Optional[float] = None
    brand: Optional[str] = None
    feature: Optional[str] = None
