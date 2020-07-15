from wai.json.object import OptionallyPresent, Absent
from wai.json.raw import RawJSONObject, RawJSONArray

from ....constants import TEAMS_URL
from ... import _base_actions
from .. import _mixin_actions
from ..._util import partial_kwargs


def list() -> RawJSONArray:
    return _base_actions.list(TEAMS_URL)


def create(name: str) -> RawJSONObject:
    return _base_actions.create(TEAMS_URL, {"name": name})


def retrieve(pk: int) -> RawJSONObject:
    return _base_actions.retrieve(TEAMS_URL, pk)


def update(pk: int, *,
           name: str) -> RawJSONObject:
    return _base_actions.update(TEAMS_URL, pk, {"name": name})


def partial_update(pk: int, *, name: OptionallyPresent[str] = Absent) -> RawJSONObject:
    return _base_actions.partial_update(TEAMS_URL, pk, partial_kwargs(name=name))


def destroy(pk: int) -> RawJSONObject:
    return _base_actions.destroy(TEAMS_URL, pk)


def add_membership(pk: int, username: str, permissions: str = "R") -> RawJSONObject:
    return _mixin_actions.add_membership(TEAMS_URL, pk, username, permissions)


def remove_membership(pk: int, username: str) -> RawJSONObject:
    return _mixin_actions.remove_membership(TEAMS_URL, pk, username)


def update_membership(pk: int, username: str, permissions: str = "R") -> RawJSONObject:
    return _mixin_actions.update_membership(TEAMS_URL, pk, username, permissions)


def hard_delete(pk: int) -> RawJSONObject:
    return _mixin_actions.hard_delete(TEAMS_URL, pk)


def reinstate(pk: int) -> RawJSONObject:
    return _mixin_actions.reinstate(TEAMS_URL, pk)
