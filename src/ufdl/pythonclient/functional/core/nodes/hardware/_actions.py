from typing import Optional

from ufdl.json.core.filter import FilterSpec

from wai.json.object import Absent, OptionallyPresent
from wai.json.raw import RawJSONObject, RawJSONArray

from .....constants import HARDWARE_URL
from .....util import partial_kwargs
from ....._UFDLServerContext import UFDLServerContext
from .... import _base_actions


def list(context: UFDLServerContext, filter_spec: Optional[FilterSpec] = None) -> RawJSONArray:
    return _base_actions.list(context, HARDWARE_URL, filter_spec)


def create(context: UFDLServerContext, generation: str, compute_capability: str) -> RawJSONObject:
    return _base_actions.create(context, HARDWARE_URL, {"generation": generation,
                                                        "compute_capability": compute_capability})


def retrieve(context: UFDLServerContext, pk: int) -> RawJSONObject:
    return _base_actions.retrieve(context, HARDWARE_URL, pk)


def update(context: UFDLServerContext, pk: int, *,
           generation: str,
           compute_capability: str) -> RawJSONObject:
    return _base_actions.update(context, HARDWARE_URL, pk, {"generation": generation,
                                                            "compute_capability": compute_capability})


def partial_update(context: UFDLServerContext, pk: int, *,
                   generation: OptionallyPresent[str] = Absent,
                   compute_capability: OptionallyPresent[str] = Absent) -> RawJSONObject:
    return _base_actions.partial_update(context, HARDWARE_URL, pk, partial_kwargs(generation=generation,
                                                                                  compute_capability=compute_capability))


def destroy(context: UFDLServerContext, pk: int) -> RawJSONObject:
    return _base_actions.destroy(context, HARDWARE_URL, pk)