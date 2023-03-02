import datetime
from dataclasses import dataclass

from django.db import models


@dataclass
class Author:
    name: str
    image: str


# Create your models here.
@dataclass
class Blog:
    pk: int
    image: str
    title: str
    preview: str
    text: str
    category: str
    author: Author
    date: datetime.date
