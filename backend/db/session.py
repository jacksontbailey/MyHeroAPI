from motor.motor_asyncio import AsyncIOMotorClient

client = AsyncIOMotorClient('localhost', 27017)
database = client.carddb
card_collection = database.card
user_collection = database.user


