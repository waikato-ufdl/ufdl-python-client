from wai.json.raw import RawJSONObject

from .....constants import JOB_OUTPUTS_URL
from ....._UFDLServerContext import UFDLServerContext
from .... import _base_actions


def retrieve(context: UFDLServerContext, pk: int) -> RawJSONObject:
    return _base_actions.retrieve(context, JOB_OUTPUTS_URL, pk)
