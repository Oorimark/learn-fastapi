from typing import Annotated, Union
from fastapi import FastAPI, Query

app = FastAPI()


# @app.get("/items/")
# async def read_items(
#     q: Annotated[
#         str | None, Query(min_length=3, max_length=50, pattern="^fixedquery$")
#         # str, Query(min_length=3, max_length=50, pattern="^fixedquery$")
#     ] = None
# ):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results


# Having multiple querys


@app.get("/items/")
async def read_items_2(
    q: Annotated[
        list,
        Query(
            alias="item-query",
            title="Query string",
            description="Query string for the items to search in the database that have a good match",
            min_length=3,
            max_length=50,
            pattern="^fixedquery$",
            deprecated=True,
        ),
    ] = ["foo", "bar"],
):
    query_items = {"q": q}
    return query_items
