from typing import Iterator

from wai.json.raw import RawJSONObject

from .....constants import JOB_OUTPUTS_URL
from ....._UFDLServerContext import UFDLServerContext
from .... import _base_actions
from ... import _mixin_actions


def retrieve(context: UFDLServerContext, pk: int) -> RawJSONObject:
    return _base_actions.retrieve(context, JOB_OUTPUTS_URL, pk)


def download(
        context: UFDLServerContext,
        pk: int
) -> Iterator[bytes]:
    return _mixin_actions.download(
        context,
        JOB_OUTPUTS_URL,
        pk
    )
