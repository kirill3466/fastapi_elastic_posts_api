import asyncio

from elasticsearch import AsyncElasticsearch, RequestError

from mapping import MAPPING_FOR_INDEX


post_1 = {
    "username": "ivan_p",
    "content": "Introduction to Python",
    "date": "2022-09-15",
    "views": 150
    }

post_2 = {
    "username": "anna_l",
    "content": "How to dance Salsa",
    "date": "2022-08-20",
    "views": 305
    }

post_3 = {
    "username": "petr99",
    "content": "Latest tech trends",
    "date": "2022-07-05",
    "views": 220
    }

post_4 = {
    "username": "sergey86",
    "content": "Fitness routines for beginners",
    "date": "2022-06-18",
    "views": 180
    }

post_5 = {
    "username": "kseniiap",
    "content": "Advanced Java concepts",
    "date": "2022-10-01",
    "views": 195
    }

post_list = [post_1, post_2, post_3, post_4, post_5]


async def main():
    elastic_client = AsyncElasticsearch("http://localhost:9200")
    try:
        # можно пропустить
        await elastic_client.indices.create(
            index="posts", mappings=MAPPING_FOR_INDEX
        )
    except RequestError as err:
        print(err)
    for document in post_list:
        await elastic_client.index(index="posts", document=document)


asyncio.run(main())
