from wai.json.object import OptionallyPresent, Absent
from wai.json.raw import RawJSONObject, RawJSONArray

from ....constants import PROJECTS_URL
from ... import _base_actions
from ..._util import partial_kwargs
from .. import _mixin_actions


def list() -> RawJSONArray:
    return _base_actions.list(PROJECTS_URL)


def create(name: str,
           team: int) -> RawJSONObject:
    return _base_actions.create(PROJECTS_URL, {"name": name,
                                               "team": team})


def retrieve(pk: int) -> RawJSONObject:
    return _base_actions.retrieve(PROJECTS_URL, pk)


def update(pk: int, *,
           name: str,
           team: int) -> RawJSONObject:
    return _base_actions.update(PROJECTS_URL, pk, {"name": name,
                                                   "team": team})


def partial_update(pk: int, *,
                   name: OptionallyPresent[str] = Absent,
                   team: OptionallyPresent[int] = Absent) -> RawJSONObject:
    return _base_actions.partial_update(PROJECTS_URL, pk, partial_kwargs(name=name,
                                                                         team=team))


def destroy(pk: int) -> RawJSONObject:
    return _base_actions.destroy(PROJECTS_URL, pk)


def hard_delete(pk: int) -> RawJSONObject:
    return _mixin_actions.hard_delete(PROJECTS_URL, pk)


def reinstate(pk: int) -> RawJSONObject:
    return _mixin_actions.reinstate(PROJECTS_URL, pk)
