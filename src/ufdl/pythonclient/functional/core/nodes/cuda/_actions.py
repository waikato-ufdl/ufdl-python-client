from typing import Optional

from ufdl.json.core.filter import FilterSpec

from wai.json.object import OptionallyPresent, Absent
from wai.json.raw import RawJSONObject, RawJSONArray

from .....constants import CUDA_URL
from .....util import partial_kwargs
from ....._UFDLServerContext import UFDLServerContext
from .... import _base_actions


def list(context: UFDLServerContext, filter_spec: Optional[FilterSpec] = None) -> RawJSONArray:
    return _base_actions.list(context, CUDA_URL, filter_spec)


def create(context: UFDLServerContext, version: str, full_version: str, min_driver_version: str) -> RawJSONObject:
    return _base_actions.create(context, CUDA_URL, {"version": version,
                                                    "full_version": full_version,
                                                    "min_driver_version": min_driver_version})


def retrieve(context: UFDLServerContext, pk: int) -> RawJSONObject:
    return _base_actions.retrieve(context, CUDA_URL, pk)


def update(context: UFDLServerContext, pk: int, *,
           version: str,
           full_version: str,
           min_driver_version: str) -> RawJSONObject:
    return _base_actions.update(context, CUDA_URL, pk, {"version": version,
                                                        "full_version": full_version,
                                                        "min_driver_version": min_driver_version})


def partial_update(context: UFDLServerContext, pk: int, *,
                   version: OptionallyPresent[str] = Absent,
                   full_version: OptionallyPresent[str] = Absent,
                   min_driver_version: OptionallyPresent[str] = Absent) -> RawJSONObject:
    return _base_actions.partial_update(context, CUDA_URL, pk, partial_kwargs(version=version,
                                                                              full_version=full_version,
                                                                              min_driver_version=min_driver_version))


def destroy(context: UFDLServerContext, pk: int) -> RawJSONObject:
    return _base_actions.destroy(context, CUDA_URL, pk)
