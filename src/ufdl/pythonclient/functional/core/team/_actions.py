from wai.json.object import OptionallyPresent, Absent
from wai.json.raw import RawJSONObject, RawJSONArray

from ....constants import TEAMS_URL
from ....util import partial_kwargs
from ...._UFDLServerContext import UFDLServerContext
from ... import _base_actions
from .. import _mixin_actions


def list(context: UFDLServerContext) -> RawJSONArray:
    return _base_actions.list(context, TEAMS_URL)


def create(context: UFDLServerContext, name: str) -> RawJSONObject:
    return _base_actions.create(context, TEAMS_URL, {"name": name})


def retrieve(context: UFDLServerContext, pk: int) -> RawJSONObject:
    return _base_actions.retrieve(context, TEAMS_URL, pk)


def update(context: UFDLServerContext, pk: int, *,
           name: str) -> RawJSONObject:
    return _base_actions.update(context, TEAMS_URL, pk, {"name": name})


def partial_update(context: UFDLServerContext, pk: int, *, name: OptionallyPresent[str] = Absent) -> RawJSONObject:
    return _base_actions.partial_update(context, TEAMS_URL, pk, partial_kwargs(name=name))


def destroy(context: UFDLServerContext, pk: int) -> RawJSONObject:
    return _base_actions.destroy(context, TEAMS_URL, pk)


def add_membership(context: UFDLServerContext, pk: int, username: str, permissions: str = "R") -> RawJSONObject:
    return _mixin_actions.add_membership(context, TEAMS_URL, pk, username, permissions)


def remove_membership(context: UFDLServerContext, pk: int, username: str) -> RawJSONObject:
    return _mixin_actions.remove_membership(context, TEAMS_URL, pk, username)


def update_membership(context: UFDLServerContext, pk: int, username: str, permissions: str = "R") -> RawJSONObject:
    return _mixin_actions.update_membership(context, TEAMS_URL, pk, username, permissions)


def hard_delete(context: UFDLServerContext, pk: int) -> RawJSONObject:
    return _mixin_actions.hard_delete(context, TEAMS_URL, pk)


def reinstate(context: UFDLServerContext, pk: int) -> RawJSONObject:
    return _mixin_actions.reinstate(context, TEAMS_URL, pk)
