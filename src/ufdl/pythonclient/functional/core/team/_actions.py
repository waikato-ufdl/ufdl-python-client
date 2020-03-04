from typing import Optional

from wai.json.raw import RawJSONObject, RawJSONArray

from ....constants import TEAMS_URL
from ... import _base_actions
from .. import _mixin_actions
from ..._util import partial_kwargs


def list() -> RawJSONArray:
    return _base_actions.list(TEAMS_URL)


def create(name: str) -> RawJSONObject:
    return _base_actions.create(TEAMS_URL,
                                name=name)


def retrieve(pk: int) -> RawJSONObject:
    return _base_actions.retrieve(TEAMS_URL, pk)


def update(pk: int, *,
           name: str) -> RawJSONObject:
    return _base_actions.update(TEAMS_URL, pk,
                                name=name)


def partial_update(pk: int, *, name: Optional[str] = None) -> RawJSONObject:
    return _base_actions.partial_update(TEAMS_URL, pk, **partial_kwargs(name=name))


def destroy(pk: int) -> RawJSONObject:
    return _base_actions.destroy(TEAMS_URL, pk)


def add_member(pk: int, username: str, permissions: Optional[str] = "R") -> RawJSONObject:
    return _mixin_actions.add_member(TEAMS_URL, pk, username, permissions)
