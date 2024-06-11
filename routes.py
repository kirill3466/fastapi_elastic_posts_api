from fastapi.routing import APIRoute

from handlers import (create_index, create_post, delete_index, get_all_posts,
                      ping)

routes = [
    APIRoute(path="/ping", endpoint=ping, methods=["GET"]),
    APIRoute(path="/create_index", endpoint=create_index, methods=["GET"]),
    APIRoute(path="/delete_index", endpoint=delete_index, methods=["GET"]),
    APIRoute(path="/create_post", endpoint=create_post, methods=["POST"]),
    APIRoute(path="/get_all_posts", endpoint=get_all_posts, methods=["GET"])
]
