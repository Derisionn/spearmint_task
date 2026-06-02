import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from services.mongo import connect_db, close_db
from routes.products import router as products_router
from routes.recommendations import router as recommendations_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    await connect_db()
    yield
    # Shutdown
    await close_db()


app = FastAPI(
    title="AI Product Recommender API",
    description="Uses Gemini to extract filters from natural language and queries MongoDB for matching products.",
    version="1.0.0",
    lifespan=lifespan
)

# Allow requests from React dev server and production frontend
origins = [
    "http://localhost:5173", 
    "http://localhost:3000"
]
frontend_url = os.getenv("FRONTEND_URL")
if frontend_url:
    origins.append(frontend_url.rstrip('/'))

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routes
app.include_router(products_router, prefix="/api", tags=["Products"])
app.include_router(recommendations_router, prefix="/api", tags=["Recommendations"])


@app.get("/")
async def root():
    return {
        "message": "AI Product Recommender API is running.",
        "docs": "/docs"
    }
