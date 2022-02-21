from typing import Optional

from ufdl.json.core.filter import FilterSpec
from ufdl.json.core.jobs import JobTemplateSpec, CreateJobSpec

from wai.json.raw import RawJSONObject, RawJSONArray

from .....constants import JOB_TEMPLATES_URL
from ....._UFDLServerContext import UFDLServerContext
from .... import _base_actions
from ... import _mixin_actions


def list(context: UFDLServerContext, filter_spec: Optional[FilterSpec] = None) -> RawJSONArray:
    return _base_actions.list(context, JOB_TEMPLATES_URL, filter_spec)


def retrieve(context: UFDLServerContext, pk: int) -> RawJSONObject:
    return _base_actions.retrieve(context, JOB_TEMPLATES_URL, pk)


def destroy(context: UFDLServerContext, pk: int):
    _base_actions.destroy(context, JOB_TEMPLATES_URL, pk)


def create_job(
        context: UFDLServerContext,
        pk: int,
        specification: CreateJobSpec
) -> RawJSONObject:
    return _mixin_actions.create_job(
        context,
        JOB_TEMPLATES_URL,
        pk,
        specification
    )


def hard_delete(context: UFDLServerContext, pk: int) -> RawJSONObject:
    return _mixin_actions.hard_delete(context, JOB_TEMPLATES_URL, pk)


def reinstate(context: UFDLServerContext, pk: int) -> RawJSONObject:
    return _mixin_actions.reinstate(context, JOB_TEMPLATES_URL, pk)


def import_template(context: UFDLServerContext, template: JobTemplateSpec) -> RawJSONObject:
    return _mixin_actions.import_template(context, JOB_TEMPLATES_URL, template)


def export_template(context: UFDLServerContext, pk: int) -> RawJSONObject:
    return _mixin_actions.export_template(context, JOB_TEMPLATES_URL, pk)


def get_all_matching_templates(
        context: UFDLServerContext,
        contract_name: str,
        **types: str
) -> RawJSONArray:
    return _mixin_actions.get_all_matching_templates(
        context,
        JOB_TEMPLATES_URL,
        contract_name,
        **types
    )


def get_all_parameters(
        context: UFDLServerContext,
        pk: int
) -> RawJSONObject:
    return _mixin_actions.get_all_parameters(context, JOB_TEMPLATES_URL, pk)


def get_types(
        context: UFDLServerContext,
        pk: int
) -> RawJSONObject:
    return _mixin_actions.get_types(context, JOB_TEMPLATES_URL, pk)


def get_outputs(
        context: UFDLServerContext,
        pk: int
) -> RawJSONObject:
    return _mixin_actions.get_outputs(context, JOB_TEMPLATES_URL, pk)
