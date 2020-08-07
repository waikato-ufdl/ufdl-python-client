from typing import Optional

from ufdl.json.core.filter import FilterSpec

from wai.json.object import Absent, OptionallyPresent
from wai.json.raw import RawJSONObject, RawJSONArray

from .....constants import NODES_URL
from .....util import partial_kwargs
from ....._UFDLServerContext import UFDLServerContext
from .... import _base_actions


def list(context: UFDLServerContext, filter_spec: Optional[FilterSpec] = None) -> RawJSONArray:
    return _base_actions.list(context, NODES_URL, filter_spec)


def create(context: UFDLServerContext,
           ip: str,
           driver_version: str,
           hardware_generation: str,
           gpu_mem: int,
           cpu_mem: int) -> RawJSONObject:
    return _base_actions.create(context, NODES_URL, {"ip": ip,
                                                     "driver_version": driver_version,
                                                     "hardware_generation": hardware_generation,
                                                     "gpu_mem": gpu_mem,
                                                     "cpu_mem": cpu_mem})


def retrieve(context: UFDLServerContext, pk: int) -> RawJSONObject:
    return _base_actions.retrieve(context, NODES_URL, pk)


def update(context: UFDLServerContext, pk: int, *,
           ip: str,
           driver_version: str,
           hardware_generation: str,
           gpu_mem: int,
           cpu_mem: int) -> RawJSONObject:
    return _base_actions.update(context, NODES_URL, pk, {"ip": ip,
                                                         "driver_version": driver_version,
                                                         "hardware_generation": hardware_generation,
                                                         "gpu_mem": gpu_mem,
                                                         "cpu_mem": cpu_mem})


def partial_update(context: UFDLServerContext, pk: int, *,
                   ip: OptionallyPresent[str] = Absent,
                   driver_version: OptionallyPresent[str] = Absent,
                   hardware_generation: OptionallyPresent[str] = Absent,
                   gpu_mem: OptionallyPresent[int] = Absent,
                   cpu_mem: OptionallyPresent[int] = Absent) -> RawJSONObject:
    return _base_actions.partial_update(context, NODES_URL, pk, partial_kwargs(ip=ip,
                                                                               driver_version=driver_version,
                                                                               hardware_generation=hardware_generation,
                                                                               gpu_mem=gpu_mem,
                                                                               cpu_mem=cpu_mem))


def destroy(context: UFDLServerContext, pk: int) -> RawJSONObject:
    return _base_actions.destroy(context, NODES_URL, pk)
