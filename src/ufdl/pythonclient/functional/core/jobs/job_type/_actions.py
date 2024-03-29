from typing import Optional

from ufdl.json.core.filter import FilterSpec

from wai.json.object import OptionallyPresent, Absent
from wai.json.raw import RawJSONObject, RawJSONArray

from .....constants import JOB_TYPES_URL
from .....util import partial_kwargs
from ....._UFDLServerContext import UFDLServerContext
from .... import _base_actions
from ... import _mixin_actions


def list(context: UFDLServerContext, filter_spec: Optional[FilterSpec] = None) -> RawJSONArray:
    return _base_actions.list(context, JOB_TYPES_URL, filter_spec)


def create(context: UFDLServerContext, name: str, pkg: str, cls: str) -> RawJSONObject:
    return _base_actions.create(context, JOB_TYPES_URL, {"name": name, "pkg": pkg, "cls": cls})


def retrieve(context: UFDLServerContext, pk: int) -> RawJSONObject:
    return _base_actions.retrieve(context, JOB_TYPES_URL, pk)


def update(context: UFDLServerContext, pk: int, *,
           name: str,
           pkg: str,
           cls: str
           ) -> RawJSONObject:
    return _base_actions.update(context, JOB_TYPES_URL, pk, {"name": name, "pkg": pkg, "cls": cls})


def partial_update(context: UFDLServerContext, pk: int, *,
                   name: OptionallyPresent[str] = Absent,
                   pkg: OptionallyPresent[str] = Absent,
                   cls: OptionallyPresent[str] = Absent
                   ) -> RawJSONObject:
    return _base_actions.partial_update(context, JOB_TYPES_URL, pk, partial_kwargs(name=name, pkg=pkg, cls=cls))


def destroy(context: UFDLServerContext, pk: int) -> RawJSONObject:
    return _base_actions.destroy(context, JOB_TYPES_URL, pk)


def get_all_values_of_type(context: UFDLServerContext, type_string: str) -> RawJSONArray:
    return _mixin_actions.get_all_values_of_type(context, JOB_TYPES_URL, type_string)
