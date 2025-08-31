from beanie import init_beanie
from pymongo import AsyncMongoClient

from src.models.product import Product

from .config import MONGO_URI


async def connect_to_database():
    client = AsyncMongoClient(MONGO_URI)
    await init_beanie(database=client.conforambot, document_models=[Product])
    print("Database initialized with Beanie and MongoDB")
