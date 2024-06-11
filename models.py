from datetime import date
from typing import Optional

from pydantic import BaseModel


class CreatePostRequest(BaseModel):
    username: str
    content: str
    date: date
    views: int
