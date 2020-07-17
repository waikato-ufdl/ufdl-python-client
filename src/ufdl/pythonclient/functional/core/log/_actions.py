from wai.json.object import OptionallyPresent, Absent
from wai.json.raw import RawJSONObject, RawJSONArray

from ....constants import LOG_URL
from ....util import partial_kwargs
from ...._UFDLServerContext import UFDLServerContext
from ... import _base_actions


def list(context: UFDLServerContext) -> RawJSONArray:
    return _base_actions.list(context, LOG_URL)


def create(context: UFDLServerContext, level: int, message: str) -> RawJSONObject:
    return _base_actions.create(context, LOG_URL, {"level": level,
                                                   "message": message})


def retrieve(context: UFDLServerContext, pk: int) -> RawJSONObject:
    return _base_actions.retrieve(context, LOG_URL, pk)


def update(context: UFDLServerContext, pk: int, *,
           level: int,
           message: str) -> RawJSONObject:
    return _base_actions.update(context, LOG_URL, pk, {"level": level,
                                                       "message": message})


def partial_update(context: UFDLServerContext, pk: int, *,
                   level: OptionallyPresent[int] = Absent,
                   message: OptionallyPresent[str] = Absent) -> RawJSONObject:
    return _base_actions.partial_update(context, LOG_URL, pk, partial_kwargs(level=level,
                                                                             message=message))


def destroy(context: UFDLServerContext, pk: int) -> RawJSONObject:
    return _base_actions.destroy(context, LOG_URL, pk)
