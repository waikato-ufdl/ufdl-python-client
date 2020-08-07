from typing import Optional, Union, IO, Iterator

from ufdl.json.core.filter import FilterSpec

from wai.json.raw import RawJSONObject, RawJSONArray

from .....constants import JOBS_URL
from ....._UFDLServerContext import UFDLServerContext
from .... import _base_actions
from ... import _mixin_actions


def list(context: UFDLServerContext, filter_spec: Optional[FilterSpec] = None) -> RawJSONArray:
    return _base_actions.list(context, JOBS_URL, filter_spec)


def retrieve(context: UFDLServerContext, pk: int) -> RawJSONObject:
    return _base_actions.retrieve(context, JOBS_URL, pk)


def destroy(context: UFDLServerContext, pk: int) -> RawJSONObject:
    return _base_actions.destroy(context, JOBS_URL, pk)


def add_output(context: UFDLServerContext, pk: int, name: str, data: Union[bytes, IO[bytes]]) -> RawJSONObject:
    return _mixin_actions.add_output(context, JOBS_URL, pk, name, data)


def set_output_type(context: UFDLServerContext, pk: int, name: str, type: str) -> RawJSONObject:
    return _mixin_actions.set_output_type(context, JOBS_URL, pk, name, type)


def delete_output(context: UFDLServerContext, pk: int, name: str) -> RawJSONObject:
    return _mixin_actions.delete_output(context, JOBS_URL, pk, name)


def get_output(context: UFDLServerContext, pk: int, name: str) -> Iterator[bytes]:
    return _mixin_actions.get_output(context, JOBS_URL, pk, name)


def hard_delete(context: UFDLServerContext, pk: int) -> RawJSONObject:
    return _mixin_actions.hard_delete(context, JOBS_URL, pk)


def reinstate(context: UFDLServerContext, pk: int) -> RawJSONObject:
    return _mixin_actions.reinstate(context, JOBS_URL, pk)
