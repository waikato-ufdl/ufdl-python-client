"""
Contains the base implementations of the common actions
for all models.
"""
from wai.common.json import RawJSONObject, RawJSONArray

from ..core import get, post, patch, put, delete
from ._util import detail_url


def list(url: str) -> RawJSONArray:
    return get(url).json()


def create(url: str, **params):
    post(url, params)


def retrieve(url: str, pk: int) -> RawJSONObject:
    return get(detail_url(url, pk)).json()


def update(url: str, pk: int, **params):
    put(detail_url(url, pk), params)


def partial_update(url: str, pk: int, **params):
    patch(detail_url(url, pk), params)


def destroy(url: str, pk: int):
    delete(detail_url(url, pk))
