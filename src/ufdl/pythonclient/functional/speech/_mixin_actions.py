from wai.json.raw import RawJSONObject

from ...util import detail_url
from ..._UFDLServerContext import UFDLServerContext

# ===================== #
# TranscriptionsViewSet #
# ===================== #


def get_transcriptions(context: UFDLServerContext, url: str, pk: int) -> RawJSONObject:
    return context.get(detail_url(url, pk) + "transcriptions").json()


def get_transcription_for_file(context: UFDLServerContext, url: str, pk: int, filename: str) -> RawJSONObject:
    return context.get(detail_url(url, pk) + "transcriptions/" + filename).json()


def set_transcription_for_file(context: UFDLServerContext, url: str, pk: int, filename: str, transcription: str) -> RawJSONObject:
    return context.post(detail_url(url, pk) + "transcriptions/" + filename, {"transcription": transcription}).json()
