from typing import Optional

from ufdl.json.core.filter import FilterSpec

from wai.json.raw import RawJSONObject, RawJSONArray

from ....constants import DOMAINS_URL
from ...._UFDLServerContext import UFDLServerContext
from ... import _base_actions


def list(context: UFDLServerContext, filter_spec: Optional[FilterSpec] = None) -> RawJSONArray:
    return _base_actions.list(context, DOMAINS_URL, filter_spec)


def retrieve(context: UFDLServerContext, pk: int) -> RawJSONObject:
    return _base_actions.retrieve(context, DOMAINS_URL, pk)
