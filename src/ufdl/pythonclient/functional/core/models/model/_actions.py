from typing import Optional, Union, IO, Iterator

from ufdl.json.core.filter import FilterSpec

from wai.json.object import Absent, OptionallyPresent
from wai.json.raw import RawJSONObject, RawJSONArray

from .....constants import MODELS_URL
from .....util import partial_kwargs
from ....._UFDLServerContext import UFDLServerContext
from .... import _base_actions
from ... import _mixin_actions


def list(context: UFDLServerContext, filter_spec: Optional[FilterSpec] = None) -> RawJSONArray:
    return _base_actions.list(context, MODELS_URL, filter_spec)


def create(context: UFDLServerContext,
           framework: int,
           domain: str,
           licence: str) -> RawJSONObject:
    return _base_actions.create(context, MODELS_URL, {"framework": framework,
                                                      "domain": domain,
                                                      "licence": licence})


def retrieve(context: UFDLServerContext, pk: int) -> RawJSONObject:
    return _base_actions.retrieve(context, MODELS_URL, pk)


def update(context: UFDLServerContext, pk: int, *,
           framework: int,
           domain: str,
           licence: str) -> RawJSONObject:
    return _base_actions.update(context, MODELS_URL, pk, {"framework": framework,
                                                          "domain": domain,
                                                          "licence": licence})


def partial_update(context: UFDLServerContext, pk: int, *,
                   framework: OptionallyPresent[int] = Absent,
                   domain: OptionallyPresent[str] = Absent,
                   licence: OptionallyPresent[str] = Absent) -> RawJSONObject:
    return _base_actions.partial_update(context, MODELS_URL, pk, partial_kwargs(framework=framework,
                                                                                domain=domain,
                                                                                licence=licence))


def destroy(context: UFDLServerContext, pk: int) -> RawJSONObject:
    return _base_actions.destroy(context, MODELS_URL, pk)


def set_file(context: UFDLServerContext, pk: int, data: Union[bytes, IO[bytes]]) -> RawJSONObject:
    return _mixin_actions.set_file(context, MODELS_URL, pk, data)


def delete_file(context: UFDLServerContext, pk: int) -> RawJSONObject:
    return _mixin_actions.delete_file_sf(context, MODELS_URL, pk)


def download(context: UFDLServerContext, pk: int) -> Iterator[bytes]:
    return _mixin_actions.download(context, MODELS_URL, pk, "data")


def hard_delete(context: UFDLServerContext, pk: int) -> RawJSONObject:
    return _mixin_actions.hard_delete(context, MODELS_URL, pk)


def reinstate(context: UFDLServerContext, pk: int) -> RawJSONObject:
    return _mixin_actions.reinstate(context, MODELS_URL, pk)
