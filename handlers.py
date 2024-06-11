
from elasticsearch import AsyncElasticsearch
from starlette.requests import Request

from log import logger
from mapping import MAPPING_FOR_INDEX
from models import CreatePostRequest


async def ping() -> dict:
    return {"success": True}


async def create_index(request: Request) -> dict:
    elastic_client: AsyncElasticsearch = request.app.state.elastic_client
    await elastic_client.indices.create(
        index="posts", mappings=MAPPING_FOR_INDEX
    )
    return {"success": True}


async def delete_index(request: Request) -> dict:
    elastic_client: AsyncElasticsearch = request.app.state.elastic_client
    await elastic_client.indices.delete(index="posts")
    return {"success": True}


async def create_post(request: Request, body: CreatePostRequest) -> dict:
    elastic_client: AsyncElasticsearch = request.app.state.elastic_client
    # работает, но выдает ошибку сериализации ответа
    res = await elastic_client.index(index="posts", document=body.model_dump())
    logger.info(res)
    return {"success": True, "result": res}


async def get_all_posts(request: Request):
    elastic_client: AsyncElasticsearch = request.app.state.elastic_client
    res = await elastic_client.search(index="posts", query={"match_all": {}})
    return {"success": True, "result": res}
