from fastapi import FastAPI

app = FastAPI()

# @app.get("/items")
# def root(skip: int = 10, limit: int = 20):
#     return {"skip": skip, "limit": limit}


@app.get("/items/{item_id}")
async def read_Item(item_id: str, q: str | None = None, short: bool = False):
    if q:
        return {"item_id": item_id, "q": q, "short": short}
    return {"item_id", item_id}
