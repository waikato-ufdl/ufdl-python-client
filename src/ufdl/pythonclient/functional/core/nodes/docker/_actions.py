from typing import Optional

from ufdl.json.core.filter import FilterSpec

from wai.json.object import OptionallyPresent, Absent
from wai.json.raw import RawJSONObject, RawJSONArray

from .....constants import DOCKER_URL
from .....util import partial_kwargs
from ....._UFDLServerContext import UFDLServerContext
from .... import _base_actions


def list(context: UFDLServerContext, filter_spec: Optional[FilterSpec] = None) -> RawJSONArray:
    return _base_actions.list(context, DOCKER_URL, filter_spec)


def create(context: UFDLServerContext, name: str,
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
           min_hardware_generation: Optional[str],
           cpu: bool) -> RawJSONObject:
    return _base_actions.create(context, DOCKER_URL, {"name": name,
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
                                                      "min_hardware_generation": min_hardware_generation,
                                                      "cpu": cpu})


def retrieve(context: UFDLServerContext, pk: int) -> RawJSONObject:
    return _base_actions.retrieve(context, DOCKER_URL, pk)


def update(context: UFDLServerContext, pk: int, *,
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
           min_hardware_generation: Optional[str],
           cpu: bool) -> RawJSONObject:
    return _base_actions.update(context, DOCKER_URL, pk, {"name": name,
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
                                                          "min_hardware_generation": min_hardware_generation,
                                                          "cpu": cpu})


def partial_update(context: UFDLServerContext, pk: int, *,
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
                   min_hardware_generation: OptionallyPresent[Optional[str]] = Absent,
                   cpu: OptionallyPresent[bool] = Absent) -> RawJSONObject:
    return _base_actions.partial_update(context, DOCKER_URL, pk, partial_kwargs(name=name,
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
                                                                                min_hardware_generation=min_hardware_generation,
                                                                                cpu=cpu))


def destroy(context: UFDLServerContext, pk: int) -> RawJSONObject:
    return _base_actions.destroy(context, DOCKER_URL, pk)
