from typing import Optional

from ufdl.json.core.filter import FilterSpec

from wai.json.object import OptionallyPresent, Absent
from wai.json.raw import RawJSONObject, RawJSONArray

from ....constants import PROJECTS_URL
from ....util import partial_kwargs
from ...._UFDLServerContext import UFDLServerContext
from ... import _base_actions
from .. import _mixin_actions


def list(context: UFDLServerContext, filter_spec: Optional[FilterSpec] = None) -> RawJSONArray:
    return _base_actions.list(context, PROJECTS_URL, filter_spec)


def create(context: UFDLServerContext,
           name: str,
           team: int) -> RawJSONObject:
    return _base_actions.create(context, PROJECTS_URL, {"name": name,
                                                        "team": team})


def retrieve(context: UFDLServerContext, pk: int) -> RawJSONObject:
    return _base_actions.retrieve(context, PROJECTS_URL, pk)


def update(context: UFDLServerContext, pk: int, *,
           name: str,
           team: int) -> RawJSONObject:
    return _base_actions.update(context, PROJECTS_URL, pk, {"name": name,
                                                            "team": team})


def partial_update(context: UFDLServerContext, pk: int, *,
                   name: OptionallyPresent[str] = Absent,
                   team: OptionallyPresent[int] = Absent) -> RawJSONObject:
    return _base_actions.partial_update(context, PROJECTS_URL, pk, partial_kwargs(name=name,
                                                                                  team=team))


def destroy(context: UFDLServerContext, pk: int) -> RawJSONObject:
    return _base_actions.destroy(context, PROJECTS_URL, pk)


def hard_delete(context: UFDLServerContext, pk: int) -> RawJSONObject:
    return _mixin_actions.hard_delete(context, PROJECTS_URL, pk)


def reinstate(context: UFDLServerContext, pk: int) -> RawJSONObject:
    return _mixin_actions.reinstate(context, PROJECTS_URL, pk)
