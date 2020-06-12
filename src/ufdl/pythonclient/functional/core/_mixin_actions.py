"""
Contains actions implemented as mixin views on the server.
"""
from typing import Union, IO, Iterator, Optional, List

from wai.json.raw import RawJSONObject

from ...core import get, post, upload, download as core_download, delete, patch
from .._util import detail_url

# =============== #
# CopyableViewSet #
# =============== #


def copy(url: str, pk: int, **params) -> RawJSONObject:
    return post(detail_url(url, pk) + "copy", params).json()


# =================== #
# DownloadableViewSet #
# =================== #


def download(url: str, pk: int, filetype: str, **params) -> Iterator[bytes]:
    return core_download(detail_url(url, pk) + "download",
                         filetype=filetype, **params).iter_content(chunk_size=None)


# ==================== #
# FileContainerViewSet #
# ==================== #


def add_file(url: str, pk: int, filename: str, data: Union[bytes, IO[bytes]]) -> RawJSONObject:
    return upload(detail_url(url, pk) + "files/" + filename, filename, data).json()


def get_file(url: str, pk: int, filename: str) -> Iterator[bytes]:
    return core_download(detail_url(url, pk) + "files/" + filename).iter_content(chunk_size=None)


def delete_file(url: str, pk: int, filename: str) -> RawJSONObject:
    return delete(detail_url(url, pk) + "files/" + filename).json()


def set_metadata(url: str, pk: int, filename: str, metadata: str) -> str:
    return post(detail_url(url, pk) + "metadata/" + filename, {"metadata": metadata}).json()['metadata']


def get_metadata(url: str, pk: int, filename: str) -> str:
    return get(detail_url(url, pk) + "metadata/" + filename).json()['metadata']


# =========================== #
# LicenceSubdescriptorViewSet #
# =========================== #


def add_subdescriptors(url: str, pk: int, type: str, names: List[Union[int, str]]) -> RawJSONObject:
    return patch(detail_url(url, pk) + "subdescriptors/", {"method": "add", "type": type, "names": names}).json()


def remove_subdescriptors(url: str, pk: int, type: str, names: List[Union[int, str]]) -> RawJSONObject:
    return patch(detail_url(url, pk) + "subdescriptors/", {"method": "remove", "type": type, "names": names}).json()


# ================= #
# MembershipViewSet #
# ================= #


def add_membership(url: str, pk: int, username: str, permissions: Optional[str] = "R") -> RawJSONObject:
    return patch(detail_url(url, pk) + "memberships", {"method": "add", "username": username, "permissions": permissions}).json()


def remove_membership(url: str, pk: int, username: str) -> RawJSONObject:
    return patch(detail_url(url, pk) + "memberships", {"method": "remove", "username": username}).json()


def update_membership(url: str, pk: int, username: str, permissions: Optional[str] = "R") -> RawJSONObject:
    return patch(detail_url(url, pk) + "memberships", {"method": "update", "username": username, "permissions": permissions}).json()
