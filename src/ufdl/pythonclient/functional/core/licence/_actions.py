from typing import List, Union

from wai.json.object import OptionallyPresent, Absent
from wai.json.raw import RawJSONObject, RawJSONArray

from ....constants import LICENCES_URL
from ....util import partial_kwargs
from ...._UFDLServerContext import UFDLServerContext
from ... import _base_actions
from .. import _mixin_actions


def list(context: UFDLServerContext) -> RawJSONArray:
    return _base_actions.list(context, LICENCES_URL)


def create(context: UFDLServerContext, name: str, url: str) -> RawJSONObject:
    return _base_actions.create(context, LICENCES_URL, {"name": name,
                                                        "url": url})


def retrieve(context: UFDLServerContext, pk: int) -> RawJSONObject:
    return _base_actions.retrieve(context, LICENCES_URL, pk)


def update(context: UFDLServerContext, pk: int, *,
           name: str,
           url: str) -> RawJSONObject:
    return _base_actions.update(context, LICENCES_URL, pk, {"name": name,
                                                            "url": url})


def partial_update(context: UFDLServerContext, pk: int, *,
                   name: OptionallyPresent[str] = Absent,
                   url: OptionallyPresent[str] = Absent) -> RawJSONObject:
    return _base_actions.partial_update(context, LICENCES_URL, pk, partial_kwargs(name=name,
                                                                                  url=url))


def destroy(context: UFDLServerContext, pk: int) -> RawJSONObject:
    return _base_actions.destroy(context, LICENCES_URL, pk)


def add_subdescriptors(context: UFDLServerContext, pk: int, type: str, names: List[Union[int, str]]) -> RawJSONObject:
    return _mixin_actions.add_subdescriptors(context, LICENCES_URL, pk, type, names)


def remove_subdescriptors(context: UFDLServerContext, pk: int, type: str, names: List[Union[int, str]]) -> RawJSONObject:
    return _mixin_actions.remove_subdescriptors(context, LICENCES_URL, pk, type, names)
