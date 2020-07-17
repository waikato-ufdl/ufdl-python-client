"""
Contains actions implemented as mixin views on the server.
"""
from typing import Union, IO, Iterator, List

from wai.json.raw import RawJSONObject

from ...util import detail_url
from ..._UFDLServerContext import UFDLServerContext

# =============== #
# CopyableViewSet #
# =============== #


def copy(context: UFDLServerContext, url: str, pk: int, **params) -> RawJSONObject:
    return context.post(detail_url(url, pk) + "copy", params).json()


# =================== #
# DownloadableViewSet #
# =================== #


def download(context: UFDLServerContext, url: str, pk: int, filetype: str, **params) -> Iterator[bytes]:
    return context.download(detail_url(url, pk) + "download",
                            filetype=filetype, **params).iter_content(chunk_size=None)


# ==================== #
# FileContainerViewSet #
# ==================== #


def add_file(context: UFDLServerContext, url: str, pk: int, filename: str, data: Union[bytes, IO[bytes]]) -> RawJSONObject:
    return context.upload(detail_url(url, pk) + "files/" + filename, filename, data).json()


def get_file(context: UFDLServerContext, url: str, pk: int, filename: str) -> Iterator[bytes]:
    return context.download(detail_url(url, pk) + "files/" + filename).iter_content(chunk_size=None)


def delete_file(context: UFDLServerContext, url: str, pk: int, filename: str) -> RawJSONObject:
    return context.delete(detail_url(url, pk) + "files/" + filename).json()


def set_metadata(context: UFDLServerContext, url: str, pk: int, filename: str, metadata: str) -> str:
    return context.post(detail_url(url, pk) + "metadata/" + filename, {"metadata": metadata}).json()['metadata']


def get_metadata(context: UFDLServerContext, url: str, pk: int, filename: str) -> str:
    return context.get(detail_url(url, pk) + "metadata/" + filename).json()['metadata']


# =========================== #
# LicenceSubdescriptorViewSet #
# =========================== #


def add_subdescriptors(context: UFDLServerContext, url: str, pk: int, type: str, names: List[Union[int, str]]) -> RawJSONObject:
    return context.patch(detail_url(url, pk) + "subdescriptors/", {"method": "add", "type": type, "names": names}).json()


def remove_subdescriptors(context: UFDLServerContext, url: str, pk: int, type: str, names: List[Union[int, str]]) -> RawJSONObject:
    return context.patch(detail_url(url, pk) + "subdescriptors/", {"method": "remove", "type": type, "names": names}).json()


# ================= #
# MembershipViewSet #
# ================= #


def add_membership(context: UFDLServerContext, url: str, pk: int, username: str, permissions: str = "R") -> RawJSONObject:
    return context.patch(detail_url(url, pk) + "memberships", {"method": "add", "username": username, "permissions": permissions}).json()


def remove_membership(context: UFDLServerContext, url: str, pk: int, username: str) -> RawJSONObject:
    return context.patch(detail_url(url, pk) + "memberships", {"method": "remove", "username": username}).json()


def update_membership(context: UFDLServerContext, url: str, pk: int, username: str, permissions: str = "R") -> RawJSONObject:
    return context.patch(detail_url(url, pk) + "memberships", {"method": "update", "username": username, "permissions": permissions}).json()


# ================= #
# SoftDeleteViewSet #
# ================= #

def hard_delete(context: UFDLServerContext, url: str, pk: int) -> RawJSONObject:
    return context.delete(detail_url(url, pk) + "hard").json()


def reinstate(context: UFDLServerContext, url: str, pk: int) -> RawJSONObject:
    return context.delete(detail_url(url, pk) + "reinstate").json()
