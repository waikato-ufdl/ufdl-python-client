from typing import Optional

from ufdl.json.core.filter import FilterSpec

from wai.json.object import Absent, OptionallyPresent
from wai.json.raw import RawJSONObject, RawJSONArray

from .....constants import FRAMEWORKS_URL
from .....util import partial_kwargs
from ....._UFDLServerContext import UFDLServerContext
from .... import _base_actions


def list(context: UFDLServerContext, filter_spec: Optional[FilterSpec] = None) -> RawJSONArray:
    return _base_actions.list(context, FRAMEWORKS_URL, filter_spec)


def create(context: UFDLServerContext, name: str, version: str) -> RawJSONObject:
    return _base_actions.create(context, FRAMEWORKS_URL, {"name": name,
                                                          "version": version})


def retrieve(context: UFDLServerContext, pk: int) -> RawJSONObject:
    return _base_actions.retrieve(context, FRAMEWORKS_URL, pk)


def update(context: UFDLServerContext, pk: int, *,
           name: str,
           version: str) -> RawJSONObject:
    return _base_actions.update(context, FRAMEWORKS_URL, pk, {"name": name,
                                                              "version": version})


def partial_update(context: UFDLServerContext, pk: int, *,
                   name: OptionallyPresent[str] = Absent,
                   version: OptionallyPresent[str] = Absent) -> RawJSONObject:
    return _base_actions.partial_update(context, FRAMEWORKS_URL, pk, partial_kwargs(name=name,
                                                                                    version=version))


def destroy(context: UFDLServerContext, pk: int) -> RawJSONObject:
    return _base_actions.destroy(context, FRAMEWORKS_URL, pk)
