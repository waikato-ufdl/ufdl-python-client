from wai.json.raw import RawJSONObject

from ...core import get, post
from .._util import detail_url

# ===================== #
# TranscriptionsViewSet #
# ===================== #


def get_transcriptions(url: str, pk: int) -> RawJSONObject:
    return get(detail_url(url, pk) + "transcriptions").json()


def get_transcription_for_file(url: str, pk: int, filename: str) -> RawJSONObject:
    return get(detail_url(url, pk) + "transcriptions/" + filename).json()


def set_transcription_for_file(url: str, pk: int, filename: str, transcription: str) -> RawJSONObject:
    return post(detail_url(url, pk) + "transcriptions/" + filename, {"transcription": transcription}).json()
