from typing import Optional

from wai.json.object import OptionallyPresent, Absent
from wai.json.raw import RawJSONObject, RawJSONArray

from .....constants import DOCKER_URL
from .... import _base_actions
from ...._util import partial_kwargs


def list() -> RawJSONArray:
    return _base_actions.list(DOCKER_URL)


def create(name: str,
           version: str,
           url: str,
           registry_url: str,
           registry_username: Optional[str],
           registry_password: Optional[str],
           cuda_version: str,
           framework: str,
           framework_version: str,
           domain: str,
           task: str,
           min_hardware_generation: str) -> RawJSONObject:
    return _base_actions.create(DOCKER_URL, {"name": name,
                                             "version": version,
                                             "url": url,
                                             "registry_url": registry_url,
                                             "registry_username": registry_username,
                                             "registry_password": registry_password,
                                             "cuda_version": cuda_version,
                                             "framework": framework,
                                             "framework_version": framework_version,
                                             "domain": domain,
                                             "task": task,
                                             "min_hardware_generation": min_hardware_generation})


def retrieve(pk: int) -> RawJSONObject:
    return _base_actions.retrieve(DOCKER_URL, pk)


def update(pk: int, *,
           name: str,
           version: str,
           url: str,
           registry_url: str,
           registry_username: Optional[str],
           registry_password: Optional[str],
           cuda_version: str,
           framework: str,
           framework_version: str,
           domain: str,
           task: str,
           min_hardware_generation: str) -> RawJSONObject:
    return _base_actions.update(DOCKER_URL, pk, {"name": name,
                                                 "version": version,
                                                 "url": url,
                                                 "registry_url": registry_url,
                                                 "registry_username": registry_username,
                                                 "registry_password": registry_password,
                                                 "cuda_version": cuda_version,
                                                 "framework": framework,
                                                 "framework_version": framework_version,
                                                 "domain": domain,
                                                 "task": task,
                                                 "min_hardware_generation": min_hardware_generation})


def partial_update(pk: int, *,
                   name: OptionallyPresent[str] = Absent,
                   version: OptionallyPresent[str] = Absent,
                   url: OptionallyPresent[str] = Absent,
                   registry_url: OptionallyPresent[str] = Absent,
                   registry_username: OptionallyPresent[Optional[str]] = Absent,
                   registry_password: OptionallyPresent[Optional[str]] = Absent,
                   cuda_version: OptionallyPresent[str] = Absent,
                   framework: OptionallyPresent[str] = Absent,
                   framework_version: OptionallyPresent[str] = Absent,
                   domain: OptionallyPresent[str] = Absent,
                   task: OptionallyPresent[str] = Absent,
                   min_hardware_generation: OptionallyPresent[str] = Absent) -> RawJSONObject:
    return _base_actions.partial_update(DOCKER_URL, pk, partial_kwargs(name=name,
                                                                       version=version,
                                                                       url=url,
                                                                       registry_url=registry_url,
                                                                       registry_username=registry_username,
                                                                       registry_password=registry_password,
                                                                       cuda_version=cuda_version,
                                                                       framework=framework,
                                                                       framework_version=framework_version,
                                                                       domain=domain,
                                                                       task=task,
                                                                       min_hardware_generation=min_hardware_generation))


def destroy(pk: int) -> RawJSONObject:
    return _base_actions.destroy(DOCKER_URL, pk)
