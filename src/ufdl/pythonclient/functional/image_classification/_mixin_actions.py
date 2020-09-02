from typing import List

from wai.json.raw import RawJSONObject

from ..._UFDLServerContext import UFDLServerContext

# ================= #
# CategoriesViewSet #
# ================= #


def get_categories(context: UFDLServerContext, url: str, pk: int) -> RawJSONObject:
    return context.get(f"{url}/{pk}/categories").json()


def add_categories(context: UFDLServerContext, url: str, pk: int, images: List[str], categories: List[str]) -> RawJSONObject:
    return context.patch(f"{url}/{pk}/categories", {"method": "add", "images": images, "categories": categories}).json()


def remove_categories(context: UFDLServerContext, url: str, pk: int, images: List[str], categories: List[str]) -> RawJSONObject:
    return context.patch(f"{url}/{pk}/categories", {"method": "remove", "images": images, "categories": categories}).json()
