from wai.json.object import OptionallyPresent, Absent
from wai.json.raw import RawJSONObject, RawJSONArray

from .....constants import CUDA_URL
from .... import _base_actions
from ...._util import partial_kwargs


def list() -> RawJSONArray:
    return _base_actions.list(CUDA_URL)


def create(version: str, full_version: str, min_driver_version: str) -> RawJSONObject:
    return _base_actions.create(CUDA_URL, {"version": version,
                                           "full_version": full_version,
                                           "min_driver_version": min_driver_version})


def retrieve(pk: int) -> RawJSONObject:
    return _base_actions.retrieve(CUDA_URL, pk)


def update(pk: int, *,
           version: str,
           full_version: str,
           min_driver_version: str) -> RawJSONObject:
    return _base_actions.update(CUDA_URL, pk, {"version": version,
                                               "full_version": full_version,
                                               "min_driver_version": min_driver_version})


def partial_update(pk: int, *,
                   version: OptionallyPresent[str] = Absent,
                   full_version: OptionallyPresent[str] = Absent,
                   min_driver_version: OptionallyPresent[str] = Absent) -> RawJSONObject:
    return _base_actions.partial_update(CUDA_URL, pk, partial_kwargs(version=version,
                                                                     full_version=full_version,
                                                                     min_driver_version=min_driver_version))


def destroy(pk: int) -> RawJSONObject:
    return _base_actions.destroy(CUDA_URL, pk)
