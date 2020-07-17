"""
Contains the base implementations of the common actions
for all models.
"""
from wai.json.raw import RawJSONObject, RawJSONArray

from ..util import detail_url
from .._UFDLServerContext import UFDLServerContext


def list(context: UFDLServerContext, url: str) -> RawJSONArray:
    return context.get(url).json()


def create(context: UFDLServerContext, url: str, params: RawJSONObject) -> RawJSONObject:
    return context.post(url, params).json()


def retrieve(context: UFDLServerContext, url: str, pk: int) -> RawJSONObject:
    return context.get(detail_url(url, pk)).json()


def update(context: UFDLServerContext, url: str, pk: int, params: RawJSONObject) -> RawJSONObject:
    return context.put(detail_url(url, pk), params).json()


def partial_update(context: UFDLServerContext, url: str, pk: int, params: RawJSONObject) -> RawJSONObject:
    return context.patch(detail_url(url, pk), params).json()


def destroy(context: UFDLServerContext, url: str, pk: int):
    context.delete(detail_url(url, pk))
