from wai.json.object import OptionallyPresent, Absent
from wai.json.raw import RawJSONObject, RawJSONArray

from ....constants import LOG_URL
from ... import _base_actions
from ..._util import partial_kwargs


def list() -> RawJSONArray:
    return _base_actions.list(LOG_URL)


def create(level: int, message: str) -> RawJSONObject:
    return _base_actions.create(LOG_URL, {"level": level,
                                          "message": message})


def retrieve(pk: int) -> RawJSONObject:
    return _base_actions.retrieve(LOG_URL, pk)


def update(pk: int, *,
           level: int,
           message: str) -> RawJSONObject:
    return _base_actions.update(LOG_URL, pk, {"level": level,
                                              "message": message})


def partial_update(pk: int, *,
                   level: OptionallyPresent[int] = Absent,
                   message: OptionallyPresent[str] = Absent) -> RawJSONObject:
    return _base_actions.partial_update(LOG_URL, pk, partial_kwargs(level=level,
                                                                    message=message))


def destroy(pk: int) -> RawJSONObject:
    return _base_actions.destroy(LOG_URL, pk)
