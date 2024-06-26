from typing import Annotated
from fastapi import FastAPI, Query, Path

app = FastAPI()


@app.get("/items/{item_id}")
def get_items(
    item_id: Annotated[int, Path(title="The ID of the item to get")],
    q: Annotated[str | None, Query(alias="item-query")] = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results
