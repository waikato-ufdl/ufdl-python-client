"""
Contains actions implemented as mixin views on the server.
"""
from typing import Union, IO, Iterator, List

from wai.json.raw import RawJSONObject

from ...util import detail_url
from ..._UFDLServerContext import UFDLServerContext

# =================== #
# AddJobOutputViewSet #
# =================== #


def add_output(context: UFDLServerContext, url: str, pk: int, name: str, data: Union[bytes, IO[bytes]]) -> RawJSONObject:
    return context.upload(detail_url(url, pk) + "outputs/" + name, name, data).json()


def set_output_type(context: UFDLServerContext, url: str, pk: int, name: str, type: str) -> RawJSONObject:
    return context.patch(detail_url(url, pk) + "outputs/" + name, {"type": type}).json()


def delete_output(context: UFDLServerContext, url: str, pk: int, name: str) -> RawJSONObject:
    return context.delete(detail_url(url, pk) + "outputs/" + name).json()


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


def delete_file_fc(context: UFDLServerContext, url: str, pk: int, filename: str) -> RawJSONObject:
    return context.delete(detail_url(url, pk) + "files/" + filename).json()


def set_metadata(context: UFDLServerContext, url: str, pk: int, filename: str, metadata: str) -> str:
    return context.post(detail_url(url, pk) + "metadata/" + filename, {"metadata": metadata}).json()['metadata']


def get_metadata(context: UFDLServerContext, url: str, pk: int, filename: str) -> str:
    return context.get(detail_url(url, pk) + "metadata/" + filename).json()['metadata']


# ======================= #
# InputsParametersViewSet #
# ======================= #


def add_input(context: UFDLServerContext, url: str, pk: int, name: str, type: str, options: str) -> RawJSONObject:
    return context.post(detail_url(url, pk) + "inputs/" + name, {"type": type, "options": options}).json()


def delete_input(context: UFDLServerContext, url: str, pk: int, name: str) -> RawJSONObject:
    return context.delete(detail_url(url, pk) + "inputs/" + name).json()


def add_parameter(context: UFDLServerContext, url: str, pk: int, name: str, type: str, default: str) -> RawJSONObject:
    return context.post(detail_url(url, pk) + "parameters/" + name, {"type": type, "default": default}).json()


def delete_parameter(context: UFDLServerContext, url: str, pk: int, name: str) -> RawJSONObject:
    return context.delete(detail_url(url, pk) + "parameters/" + name).json()


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


def get_permissions_for_user(context: UFDLServerContext, url: str, pk: int, username: str) -> str:
    return context.get(detail_url(url, pk) + "permissions/" + username).json()


# ============== #
# SetFileViewSet #
# ============== #


def set_file(context: UFDLServerContext, url: str, pk: int, data: Union[bytes, IO[bytes]]) -> RawJSONObject:
    return context.upload(detail_url(url, pk) + "data", "data", data).json()


def delete_file_sf(context: UFDLServerContext, url: str, pk: int) -> RawJSONObject:
    return context.delete(detail_url(url, pk) + "data").json()


# ================= #
# SoftDeleteViewSet #
# ================= #

def hard_delete(context: UFDLServerContext, url: str, pk: int) -> RawJSONObject:
    return context.delete(detail_url(url, pk) + "hard").json()


def reinstate(context: UFDLServerContext, url: str, pk: int) -> RawJSONObject:
    return context.delete(detail_url(url, pk) + "reinstate").json()

