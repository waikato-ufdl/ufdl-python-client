from typing import Optional, Union, Tuple, Dict

from ufdl.json.core.filter import FilterSpec

from wai.json.object import OptionallyPresent, Absent
from wai.json.raw import RawJSONObject, RawJSONArray

from .....constants import JOB_TEMPLATES_URL
from .....util import partial_kwargs
from ....._UFDLServerContext import UFDLServerContext
from .... import _base_actions
from ... import _mixin_actions


def list(context: UFDLServerContext, filter_spec: Optional[FilterSpec] = None) -> RawJSONArray:
    return _base_actions.list(context, JOB_TEMPLATES_URL, filter_spec)


def create(context: UFDLServerContext,
           name: str,
           version: str,
           scope: str,
           framework: int,
           domain: str,
           type: str,
           executor_class: str,
           required_packages: str,
           body: str) -> RawJSONObject:
    return _base_actions.create(context, JOB_TEMPLATES_URL, {"name": name,
                                                             "version": version,
                                                             "scope": scope,
                                                             "framework": framework,
                                                             "domain": domain,
                                                             "type": type,
                                                             "executor_class": executor_class,
                                                             "required_packages": required_packages,
                                                             "body": body})


def retrieve(context: UFDLServerContext, pk: int) -> RawJSONObject:
    return _base_actions.retrieve(context, JOB_TEMPLATES_URL, pk)


def update(context: UFDLServerContext, pk: int, *,
           name: str,
           version: str,
           scope: str,
           framework: int,
           domain: str,
           type: str,
           executor_class: str,
           required_packages: str,
           body: str) -> RawJSONObject:
    return _base_actions.update(context, JOB_TEMPLATES_URL, pk, {"name": name,
                                                                 "version": version,
                                                                 "scope": scope,
                                                                 "framework": framework,
                                                                 "domain": domain,
                                                                 "type": type,
                                                                 "executor_class": executor_class,
                                                                 "required_packages": required_packages,
                                                                 "body": body})


def partial_update(context: UFDLServerContext, pk: int, *,
                   name: OptionallyPresent[str] = Absent,
                   version: OptionallyPresent[str] = Absent,
                   scope: OptionallyPresent[str] = Absent,
                   framework: OptionallyPresent[int] = Absent,
                   domain: OptionallyPresent[str] = Absent,
                   type: OptionallyPresent[str] = Absent,
                   executor_class: OptionallyPresent[str] = Absent,
                   required_packages: OptionallyPresent[str] = Absent,
                   body: OptionallyPresent[str] = Absent) -> RawJSONObject:
    return _base_actions.partial_update(context, JOB_TEMPLATES_URL, pk, partial_kwargs(name=name,
                                                                                       version=version,
                                                                                       scope=scope,
                                                                                       framework=framework,
                                                                                       domain=domain,
                                                                                       type=type,
                                                                                       executor_class=executor_class,
                                                                                       required_packages=required_packages,
                                                                                       body=body))


def destroy(context: UFDLServerContext, pk: int) -> RawJSONObject:
    return _base_actions.destroy(context, JOB_TEMPLATES_URL, pk)


def create_job(context: UFDLServerContext, pk: int,
               docker_image: Union[int, Tuple[str, str]],
               input_values: Dict[str, str],
               parameter_values: Optional[Dict[str, str]] = None) -> RawJSONObject:
    return _mixin_actions.create_job(context, JOB_TEMPLATES_URL, pk,
                                     docker_image, input_values, parameter_values)


def add_input(context: UFDLServerContext, pk: int, name: str, type: str, options: str) -> RawJSONObject:
    return _mixin_actions.add_input(context, JOB_TEMPLATES_URL, pk, name, type, options)


def delete_input(context: UFDLServerContext, pk: int, name: str) -> RawJSONObject:
    return _mixin_actions.delete_input(context, JOB_TEMPLATES_URL, pk, name)


def add_parameter(context: UFDLServerContext, pk: int, name: str, type: str, default: str) -> RawJSONObject:
    return _mixin_actions.add_parameter(context, JOB_TEMPLATES_URL, pk, name, type, default)


def delete_parameter(context: UFDLServerContext, pk: int, name: str) -> RawJSONObject:
    return _mixin_actions.delete_parameter(context, JOB_TEMPLATES_URL, pk, name)


def hard_delete(context: UFDLServerContext, pk: int) -> RawJSONObject:
    return _mixin_actions.hard_delete(context, JOB_TEMPLATES_URL, pk)


def reinstate(context: UFDLServerContext, pk: int) -> RawJSONObject:
    return _mixin_actions.reinstate(context, JOB_TEMPLATES_URL, pk)

