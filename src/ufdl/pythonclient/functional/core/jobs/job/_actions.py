from typing import Optional, Union, IO, Iterator

from ufdl.json.core.filter import FilterSpec

from wai.json.object import OptionallyPresent, Absent
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


def add_output(context: UFDLServerContext, pk: int, name: str, type: str, data: Union[bytes, IO[bytes]]) -> RawJSONObject:
    return _mixin_actions.add_output(context, JOBS_URL, pk, name, type, data)


def delete_output(context: UFDLServerContext, pk: int, name: str, type: str) -> RawJSONObject:
    return _mixin_actions.delete_output(context, JOBS_URL, pk, name, type)


def get_output(context: UFDLServerContext, pk: int, name: str, type: str) -> Iterator[bytes]:
    return _mixin_actions.get_output(context, JOBS_URL, pk, name, type)


def hard_delete(context: UFDLServerContext, pk: int) -> RawJSONObject:
    return _mixin_actions.hard_delete(context, JOBS_URL, pk)


def reinstate(context: UFDLServerContext, pk: int) -> RawJSONObject:
    return _mixin_actions.reinstate(context, JOBS_URL, pk)


def acquire_job(context: UFDLServerContext, pk: int) -> RawJSONObject:
    return _mixin_actions.acquire_job(context, JOBS_URL, pk)


def release_job(context: UFDLServerContext, pk: int) -> RawJSONObject:
    return _mixin_actions.release_job(context, JOBS_URL, pk)


def start_job(context: UFDLServerContext, pk: int, send_notification: str) -> RawJSONObject:
    return _mixin_actions.start_job(context, JOBS_URL, pk, send_notification)


def finish_job(context: UFDLServerContext, pk: int,
               success: bool,
               send_notification: str,
               error: OptionallyPresent[str] = Absent) -> RawJSONObject:
    return _mixin_actions.finish_job(context, JOBS_URL, pk, success, send_notification, error)


def reset_job(context: UFDLServerContext, pk: int) -> RawJSONObject:
    return _mixin_actions.reset_job(context, JOBS_URL, pk)


def abort_job(context: UFDLServerContext, pk: int) -> RawJSONObject:
    return _mixin_actions.reset_job(context, JOBS_URL, pk)
