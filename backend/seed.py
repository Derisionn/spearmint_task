"""
seed.py - Seeds the MongoDB 'spearmint' database with mock product data.
Run once: python seed.py
"""
from pymongo import MongoClient
from dotenv import load_dotenv
import os
import ssl

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017")
MONGODB_DB = os.getenv("MONGODB_DB", "spearmint")

PRODUCTS = [
    {
        "name": "Quantum X Pro Smartphone",
        "price": 899,
        "category": "Phone",
        "brand": "Quantum",
        "description": "Latest 5G smartphone with a stunning OLED display and advanced computational photography features.",
        "features": ["5G", "OLED display", "camera", "fast charging"]
    },
    {
        "name": "Nebula Lite Phone",
        "price": 349,
        "category": "Phone",
        "brand": "Nebula",
        "description": "Affordable smartphone with great battery life and a reliable camera for everyday use.",
        "features": ["camera", "battery", "budget-friendly"]
    },
    {
        "name": "Aura Noise-Canceling Headphones",
        "price": 249,
        "category": "Headphones",
        "brand": "Aura",
        "description": "Premium over-ear headphones with active noise cancellation and 30-hour battery life.",
        "features": ["noise cancelling", "wireless", "battery", "bluetooth"]
    },
    {
        "name": "Zenith Ultrabook 14",
        "price": 1199,
        "category": "Laptop",
        "brand": "Zenith",
        "description": "Sleek and powerful ultrabook perfect for professionals on the go. Features an M2-equivalent chip.",
        "features": ["lightweight", "fast processor", "long battery", "portable"]
    },
    {
        "name": "Atlas Smartwatch Series 5",
        "price": 199,
        "category": "Smartwatch",
        "brand": "Atlas",
        "description": "Fitness and health tracking smartwatch with built-in GPS and heart rate monitoring.",
        "features": ["gps", "heart rate monitor", "fitness tracking", "waterproof"]
    },
    {
        "name": "Echo Portable Bluetooth Speaker",
        "price": 59,
        "category": "Speaker",
        "brand": "Echo",
        "description": "Compact waterproof speaker with surprisingly loud and clear sound.",
        "features": ["waterproof", "bluetooth", "portable", "compact"]
    },
    {
        "name": "Nova 4K Action Camera",
        "price": 149,
        "category": "Camera",
        "brand": "Nova",
        "description": "Capture your adventures in stunning 4K resolution. Waterproof up to 30 meters.",
        "features": ["4K", "waterproof", "camera", "action", "wide-angle"]
    },
    {
        "name": "Lumina Desk Lamp with Wireless Charging",
        "price": 45,
        "category": "Accessories",
        "brand": "Lumina",
        "description": "Modern LED desk lamp with adjustable brightness and a built-in wireless charging pad.",
        "features": ["wireless charging", "LED", "adjustable brightness", "desk"]
    },
    {
        "name": "Pixel Burst Smartphone",
        "price": 479,
        "category": "Phone",
        "brand": "Pixel",
        "description": "Mid-range 5G phone with a triple-lens camera system. Great for photography enthusiasts on a budget.",
        "features": ["5G", "triple camera", "camera", "budget-friendly"]
    },
    {
        "name": "ProBook 15 Laptop",
        "price": 799,
        "category": "Laptop",
        "brand": "ProBook",
        "description": "Business laptop with a full-HD display, powerful AMD processor, and long battery life.",
        "features": ["AMD processor", "Full HD", "long battery", "business"]
    }
]


def seed():
    print(f"[*] Connecting to MongoDB Atlas...")
    # Use tlsAllowInvalidCertificates to work around Python 3.10 OpenSSL issues on Windows
    client = MongoClient(MONGODB_URI, tls=True, tlsAllowInvalidCertificates=True)
    db = client[MONGODB_DB]
    collection = db["products"]

    # Drop existing data to avoid duplicates
    collection.drop()
    print("[*] Dropped existing products collection.")

    result = collection.insert_many(PRODUCTS)
    print(f"[+] Inserted {len(result.inserted_ids)} products into '{MONGODB_DB}.products'.")

    client.close()
    print("[+] Done! MongoDB Atlas seeded successfully.")


if __name__ == "__main__":
    seed()
