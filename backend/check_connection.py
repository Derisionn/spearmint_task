"""
check_connection.py - Tests MongoDB Atlas connectivity
Run: python check_connection.py
"""
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI", "")
MONGODB_DB = os.getenv("MONGODB_DB", "spearmint")

print(f"[*] Attempting to connect to Atlas...")
print(f"[*] URI: {MONGODB_URI[:50]}...")

try:
    client = MongoClient(
        MONGODB_URI,
        tls=True,
        tlsAllowInvalidCertificates=True,
        serverSelectionTimeoutMS=10000  # 10 second timeout
    )
    # Force an actual connection attempt
    result = client.admin.command("ping")
    print(f"[+] SUCCESS! MongoDB Atlas connected. Ping response: {result}")
    
    # List databases
    dbs = client.list_database_names()
    print(f"[+] Databases available: {dbs}")
    
    client.close()

except Exception as e:
    print(f"[-] FAILED to connect: {type(e).__name__}")
    print(f"[-] Error: {e}")
