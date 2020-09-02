from wai.json.raw import RawJSONObject

from ..._UFDLServerContext import UFDLServerContext

# ===================== #
# TranscriptionsViewSet #
# ===================== #


def get_transcriptions(context: UFDLServerContext, url: str, pk: int) -> RawJSONObject:
    return context.get(f"{url}/{pk}/transcriptions").json()


def get_transcription_for_file(context: UFDLServerContext, url: str, pk: int, filename: str) -> RawJSONObject:
    return context.get(f"{url}/{pk}/transcriptions/{filename}").json()


def set_transcription_for_file(context: UFDLServerContext, url: str, pk: int, filename: str, transcription: str) -> RawJSONObject:
    return context.post(f"{url}/{pk}/transcriptions/" + filename, {"transcription": transcription}).json()
