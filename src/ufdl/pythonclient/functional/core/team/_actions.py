from typing import Optional

from wai.common.json import RawJSONObject, RawJSONArray

from ....constants import TEAMS_URL
from ... import _base_actions, _mixin_actions
from ..._util import partial_kwargs


def list() -> RawJSONArray:
    return _base_actions.list(TEAMS_URL)


def create(name: str):
    _base_actions.create(TEAMS_URL,
                         name=name)


def retrieve(pk: int) -> RawJSONObject:
    return _base_actions.retrieve(TEAMS_URL, pk)


def update(pk: int, *,
           name: str):
    _base_actions.update(TEAMS_URL, pk,
                         name=name)


def partial_update(pk: int, *, name: Optional[str] = None):
    _base_actions.partial_update(TEAMS_URL, pk, **partial_kwargs(name=name))


def destroy(pk: int):
    _base_actions.destroy(TEAMS_URL, pk)


def add_member(pk: int, username: str, permissions: Optional[str] = "R"):
    return _mixin_actions.add_member(TEAMS_URL, pk, username, permissions)
