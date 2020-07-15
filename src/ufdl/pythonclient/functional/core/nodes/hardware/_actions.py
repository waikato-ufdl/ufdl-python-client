from wai.json.object import Absent, OptionallyPresent
from wai.json.raw import RawJSONObject, RawJSONArray

from .....constants import HARDWARE_URL
from .... import _base_actions
from ...._util import partial_kwargs


def list() -> RawJSONArray:
    return _base_actions.list(HARDWARE_URL)


def create(generation: str, compute_capability: str) -> RawJSONObject:
    return _base_actions.create(HARDWARE_URL, {"generation": generation,
                                               "compute_capability": compute_capability})


def retrieve(pk: int) -> RawJSONObject:
    return _base_actions.retrieve(HARDWARE_URL, pk)


def update(pk: int, *,
           generation: str,
           compute_capability: str) -> RawJSONObject:
    return _base_actions.update(HARDWARE_URL, pk, {"generation": generation,
                                                   "compute_capability": compute_capability})


def partial_update(pk: int, *,
                   generation: OptionallyPresent[str] = Absent,
                   compute_capability: OptionallyPresent[str] = Absent) -> RawJSONObject:
    return _base_actions.partial_update(HARDWARE_URL, pk, partial_kwargs(generation=generation,
                                                                         compute_capability=compute_capability))


def destroy(pk: int) -> RawJSONObject:
    return _base_actions.destroy(HARDWARE_URL, pk)
