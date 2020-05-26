"""
Contains the base implementations of the common actions
for all models.
"""
from wai.json.raw import RawJSONObject, RawJSONArray

from ..core import get, post, patch, put, delete
from ._util import detail_url


def list(url: str) -> RawJSONArray:
    return get(url).json()


def create(url: str, params: RawJSONObject) -> RawJSONObject:
    return post(url, params).json()


def retrieve(url: str, pk: int) -> RawJSONObject:
    return get(detail_url(url, pk)).json()


def update(url: str, pk: int, params: RawJSONObject) -> RawJSONObject:
    return put(detail_url(url, pk), params).json()


def partial_update(url: str, pk: int, params: RawJSONObject) -> RawJSONObject:
    return patch(detail_url(url, pk), params).json()


def destroy(url: str, pk: int) -> RawJSONObject:
    return delete(detail_url(url, pk)).json()
