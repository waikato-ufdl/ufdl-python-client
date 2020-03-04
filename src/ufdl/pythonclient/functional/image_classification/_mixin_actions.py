from typing import List

from wai.json.raw import RawJSONObject

from ...core import get, post, delete
from .._util import detail_url

# ================= #
# CategoriesViewSet #
# ================= #


def get_categories(url: str, pk: int) -> RawJSONObject:
    return get(detail_url(url, pk) + "categories").json()


def add_categories(url: str, pk: int, images: List[str], categories: List[str]) -> RawJSONObject:
    return post(detail_url(url, pk) + "categories", {"images": images, "categories": categories}).json()


def remove_categories(url: str, pk: int, images: List[str], categories: List[str]) -> RawJSONObject:
    return delete(detail_url(url, pk) + "categories", {"images": images, "categories": categories}).json()
