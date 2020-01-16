"""
Contains actions implemented as mixin views on the server.
"""
from typing import Union, IO, Iterator, Optional

from wai.common.json import RawJSONObject

from ..core import post, upload, download as core_download, delete
from ._util import detail_url

# =============== #
# CopyableViewSet #
# =============== #


def copy(url: str, pk: int, **params) -> RawJSONObject:
    return post(detail_url(url, pk) + "copy", params).json()


# =================== #
# DownloadableViewSet #
# =================== #


def download(url: str, pk: int, file_format: str, **params) -> Iterator[bytes]:
    return core_download(detail_url(url, pk) + "download",
                         file_format=file_format, **params).iter_content(chunk_size=None)


# ==================== #
# FileContainerViewSet #
# ==================== #


def add_file(url: str, pk: int, filename: str, data: Union[bytes, IO[bytes]]):
    return upload(detail_url(url, pk) + "files/" + filename, filename, data)


def get_file(url: str, pk: int, filename: str):
    return core_download(detail_url(url, pk) + "files/" + filename)


def delete_file(url: str, pk: int, filename: str):
    return delete(detail_url(url, pk) + "files/" + filename)


# ================= #
# MembershipViewSet #
# ================= #


def add_member(url: str, pk: int, username: str, permissions: Optional[str] = "R"):
    return post(detail_url(url, pk) + "add-member", {"username": username, "permissions": permissions})
