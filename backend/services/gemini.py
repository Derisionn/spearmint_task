import os
import json
import re
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel("gemini-1.5-flash")
else:
    model = None
    print("⚠️  No GEMINI_API_KEY found. Falling back to keyword-based filter extraction.")


async def extract_filters(query: str) -> dict:
    """
    Use the Gemini API to extract structured product search filters
    from a natural language user query.

    Returns a dict like:
    {
        "category": "Phone",
        "max_price": 500,
        "brand": null,
        "feature": "camera"
    }
    """
    if not model:
        print("⚠️  Using fallback filter extraction (no Gemini API key).")
        return _fallback_extract(query)

    prompt = f"""
You are a product search assistant. A user has given a natural language query.
Extract the relevant search filters from the query and return ONLY a valid JSON object.
Do not include any explanation, markdown, or extra text — only raw JSON.

Fields to extract (use null if not mentioned):
- "category": The product category (e.g. "Phone", "Laptop", "Headphones", "Smartwatch", "Camera", "Speaker", "Accessories")
- "max_price": Maximum price as a number (e.g. 500). Extract from phrases like "under $500", "less than 300", "budget of 200".
- "brand": Brand name if mentioned (e.g. "Samsung", "Apple"). Use null if not mentioned.
- "feature": A key feature the user wants (e.g. "camera", "noise cancelling", "waterproof", "wireless charging"). Use null if not mentioned.

User query: "{query}"

Respond ONLY with JSON, example:
{{"category": "Phone", "max_price": 500, "brand": null, "feature": "camera"}}
"""

    try:
        response = model.generate_content(prompt)
        raw = response.text.strip()

        # Strip markdown code fences if Gemini wraps the JSON
        raw = re.sub(r"```(?:json)?", "", raw).strip().strip("`").strip()

        filters = json.loads(raw)
        print(f"🤖 Gemini extracted filters: {filters}")
        return filters

    except Exception as e:
        print(f"❌ Gemini extraction failed: {e}. Using fallback.")
        return _fallback_extract(query)


def _fallback_extract(query: str) -> dict:
    """
    Simple keyword-based fallback when no Gemini API key is present.
    """
    q = query.lower()
    filters = {"category": None, "max_price": None, "brand": None, "feature": None}

    # Category
    if any(w in q for w in ["phone", "smartphone", "mobile"]):
        filters["category"] = "Phone"
    elif any(w in q for w in ["laptop", "notebook", "ultrabook"]):
        filters["category"] = "Laptop"
    elif any(w in q for w in ["headphone", "earphone", "earbuds"]):
        filters["category"] = "Headphones"
    elif any(w in q for w in ["watch", "smartwatch", "wearable"]):
        filters["category"] = "Smartwatch"
    elif any(w in q for w in ["speaker", "bluetooth speaker"]):
        filters["category"] = "Speaker"
    elif any(w in q for w in ["camera", "action cam"]):
        filters["category"] = "Camera"

    # Max price: find "under X", "below X", "less than X", "budget X"
    price_match = re.search(r"(?:under|below|less than|budget(?:\s+of)?|max|upto?)\s*\$?\s*(\d+)", q)
    if price_match:
        filters["max_price"] = float(price_match.group(1))

    # Feature
    for feat in ["camera", "noise cancell", "waterproof", "wireless charging", "gps", "battery"]:
        if feat in q:
            filters["feature"] = feat
            break

    print(f"🔑 Fallback extracted filters: {filters}")
    return filters
