from typing import List, Union

from wai.json.object import OptionallyPresent, Absent
from wai.json.raw import RawJSONObject, RawJSONArray

from ....constants import LICENCES_URL
from ... import _base_actions
from ..._util import partial_kwargs
from .. import _mixin_actions


def list() -> RawJSONArray:
    return _base_actions.list(LICENCES_URL)


def create(name: str, url: str) -> RawJSONObject:
    return _base_actions.create(LICENCES_URL, {"name": name,
                                               "url": url})


def retrieve(pk: int) -> RawJSONObject:
    return _base_actions.retrieve(LICENCES_URL, pk)


def update(pk: int, *,
           name: str,
           url: str) -> RawJSONObject:
    return _base_actions.update(LICENCES_URL, pk, {"name": name,
                                                   "url": url})


def partial_update(pk: int, *,
                   name: OptionallyPresent[str] = Absent,
                   url: OptionallyPresent[str] = Absent) -> RawJSONObject:
    return _base_actions.partial_update(LICENCES_URL, pk, partial_kwargs(name=name,
                                                                         url=url))


def destroy(pk: int) -> RawJSONObject:
    return _base_actions.destroy(LICENCES_URL, pk)


def add_subdescriptors(pk: int, type: str, names: List[Union[int, str]]) -> RawJSONObject:
    return _mixin_actions.add_subdescriptors(LICENCES_URL, pk, type, names)


def remove_subdescriptors(pk: int, type: str, names: List[Union[int, str]]) -> RawJSONObject:
    return _mixin_actions.remove_subdescriptors(LICENCES_URL, pk, type, names)
