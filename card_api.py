from fastapi import FastAPI, status, Response
app = FastAPI()

@app.get("/")
async def home():
    return {"Greeting": "Welcome to the My Hero Academia Card Game API! This is a fan-made API that any developer is free to use. The only thing I ask is that you give me some credit when you use it, and/or buy me a coffee. This carbon-based lifeform needs Java installed..."}

@app.get("/card-list")
async def card_list():
    return {"cards": []}


# / root with api explaination
# /card-names
# /cards-by-index/{index}
# /get-random-card
# /add-card
# /get-card-by-name?{}