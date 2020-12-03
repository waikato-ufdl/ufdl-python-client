from typing import Optional, Dict, Tuple

from ufdl.json.core.filter import FilterSpec
from ufdl.json.core.jobs import JobTemplateSpec

from wai.json.object import OptionallyPresent, Absent
from wai.json.raw import RawJSONObject, RawJSONArray

from .....constants import JOB_TEMPLATES_URL
from ....._UFDLServerContext import UFDLServerContext
from .... import _base_actions
from ... import _mixin_actions


def list(context: UFDLServerContext, filter_spec: Optional[FilterSpec] = None) -> RawJSONArray:
    return _base_actions.list(context, JOB_TEMPLATES_URL, filter_spec)


def retrieve(context: UFDLServerContext, pk: int) -> RawJSONObject:
    return _base_actions.retrieve(context, JOB_TEMPLATES_URL, pk)


def destroy(context: UFDLServerContext, pk: int) -> RawJSONObject:
    return _base_actions.destroy(context, JOB_TEMPLATES_URL, pk)


def create_job(
        context: UFDLServerContext, pk: int,
        input_values: Dict[str, Tuple[str, str]],
        parameter_values: OptionallyPresent[Dict[str, str]] = Absent,
        description: OptionallyPresent[str] = Absent
) -> RawJSONObject:
    return _mixin_actions.create_job(
        context,
        JOB_TEMPLATES_URL,
        pk,
        input_values,
        parameter_values,
        description
    )


def hard_delete(context: UFDLServerContext, pk: int) -> RawJSONObject:
    return _mixin_actions.hard_delete(context, JOB_TEMPLATES_URL, pk)


def reinstate(context: UFDLServerContext, pk: int) -> RawJSONObject:
    return _mixin_actions.reinstate(context, JOB_TEMPLATES_URL, pk)


def import_template(context: UFDLServerContext, template: JobTemplateSpec) -> RawJSONObject:
    return _mixin_actions.import_template(context, JOB_TEMPLATES_URL, template)


def export_template(context: UFDLServerContext, pk: int) -> RawJSONObject:
    return _mixin_actions.export_template(context, JOB_TEMPLATES_URL, pk)
