"""
Contains the base implementations of the common actions
for all models.
"""
from typing import Optional

from ufdl.json.core.filter import FilterSpec

from wai.json.raw import RawJSONObject, RawJSONArray

from .._UFDLServerContext import UFDLServerContext


def list(context: UFDLServerContext, url: str, filter_spec: Optional[FilterSpec] = None) -> RawJSONArray:
    return context.get(url, json=None if filter_spec is None else filter_spec.to_raw_json()).json()


def create(context: UFDLServerContext, url: str, params: RawJSONObject) -> RawJSONObject:
    return context.post(url, params).json()


def retrieve(context: UFDLServerContext, url: str, pk: int) -> RawJSONObject:
    return context.get(f"{url}/{pk}").json()


def update(context: UFDLServerContext, url: str, pk: int, params: RawJSONObject) -> RawJSONObject:
    return context.put(f"{url}/{pk}", params).json()


def partial_update(context: UFDLServerContext, url: str, pk: int, params: RawJSONObject) -> RawJSONObject:
    return context.patch(f"{url}/{pk}", params).json()


def destroy(context: UFDLServerContext, url: str, pk: int):
    context.delete(f"{url}/{pk}")
