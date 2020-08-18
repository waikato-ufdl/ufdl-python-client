"""
Contains actions implemented as mixin views on the server.
"""
from typing import Union, IO, Iterator, List, Tuple, Dict

from wai.json.object import OptionallyPresent, Absent
from wai.json.raw import RawJSONObject

from ...util import detail_url, partial_kwargs
from ..._UFDLServerContext import UFDLServerContext

# ================= #
# AcquireJobViewSet #
# ================= #


def acquire_job(context: UFDLServerContext, url: str, pk: int) -> RawJSONObject:
    return context.get(detail_url(url, pk) + "acquire").json()


# =================== #
# AddJobOutputViewSet #
# =================== #


def add_output(context: UFDLServerContext, url: str, pk: int, name: str, type: str, data: Union[bytes, IO[bytes]]) -> RawJSONObject:
    return context.upload(detail_url(url, pk) + f"outputs/{name}/{type}", name, data).json()


def delete_output(context: UFDLServerContext, url: str, pk: int, name: str) -> RawJSONObject:
    return context.delete(detail_url(url, pk) + "outputs/" + name).json()


def get_output(context: UFDLServerContext, url: str, pk: int, name: str) -> Iterator[bytes]:
    return context.download(detail_url(url, pk) + "outputs/" + name).iter_content(chunk_size=None)


# =============== #
# CopyableViewSet #
# =============== #


def copy(context: UFDLServerContext, url: str, pk: int, **params) -> RawJSONObject:
    return context.post(detail_url(url, pk) + "copy", params).json()


# ================ #
# CreateJobViewSet #
# ================ #


def create_job(context: UFDLServerContext, url: str, pk: int,
               docker_image: Union[int, Tuple[str, str]],
               input_values: Dict[str, str],
               parameter_values: OptionallyPresent[Dict[str, str]] = Absent) -> RawJSONObject:
    return context.post(detail_url(url, pk) + "create-job",
                        json=partial_kwargs(
                            docker_image= (docker_image
                                           if isinstance(docker_image, int)
                                           else {"name": docker_image[0], "version": docker_image[1]}),
                            input_values=input_values,
                            parameter_values=parameter_values)).json()


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


# ============================ #
# GetHardwareGenerationViewSet #
# ============================ #


def get_hardware_generation(context: UFDLServerContext, url: str, compute: float) -> RawJSONObject:
    return context.get(url + f"get-hardware-generation/{compute}").json()


# ======================= #
# InputsParametersViewSet #
# ======================= #


def add_input(context: UFDLServerContext, url: str, pk: int,
              name: str,
              type: str,
              options: OptionallyPresent[str] = Absent,
              help: OptionallyPresent[str] = Absent) -> RawJSONObject:
    return context.post(detail_url(url, pk) + "inputs/" + name, partial_kwargs(type=type, options=options, help=help)).json()


def delete_input(context: UFDLServerContext, url: str, pk: int, name: str) -> RawJSONObject:
    return context.delete(detail_url(url, pk) + "inputs/" + name).json()


def add_parameter(context: UFDLServerContext, url: str, pk: int,
                  name: str,
                  type: str,
                  default: OptionallyPresent[str] = Absent,
                  help: OptionallyPresent[str] = Absent) -> RawJSONObject:
    return context.post(detail_url(url, pk) + "parameters/" + name, partial_kwargs(type=type, default=default, help=help)).json()


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

