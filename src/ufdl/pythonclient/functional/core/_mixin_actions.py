"""
Contains actions implemented as mixin views on the server.
"""
from typing import Union, IO, Iterator, List, Tuple, Dict

from ufdl.json.core.jobs import JobTemplateMigrationSpec

from wai.json.object import OptionallyPresent, Absent
from wai.json.raw import RawJSONObject

from ...util import partial_kwargs
from ..._UFDLServerContext import UFDLServerContext

# region AcquireJobViewSet


def acquire_job(context: UFDLServerContext, url: str, pk: int) -> RawJSONObject:
    return context.get(f"{url}/{pk}/acquire").json()


def start_job(context: UFDLServerContext, url: str, pk: int, send_notification: str) -> RawJSONObject:
    return context.post(f"{url}/{pk}/start", {"send_notification": send_notification}).json()


def finish_job(context: UFDLServerContext, url: str, pk: int,
               success: bool,
               send_notification: str,
               error: OptionallyPresent[str] = Absent) -> RawJSONObject:
    return context.post(f"{url}/{pk}/finish", partial_kwargs(success=success,
                                                             send_notification=send_notification,
                                                             error=error)).json()


def reset_job(context: UFDLServerContext, url: str, pk: int) -> RawJSONObject:
    return context.delete(f"{url}/{pk}/reset").json()

# endregion

# region AddJobOutputViewSet


def add_output(context: UFDLServerContext, url: str, pk: int, name: str, type: str, data: Union[bytes, IO[bytes]]) -> RawJSONObject:
    return context.upload(f"{url}/{pk}/outputs/{name}/{type}", name, data).json()


def delete_output(context: UFDLServerContext, url: str, pk: int, name: str, type: str) -> RawJSONObject:
    return context.delete(f"{url}/{pk}/outputs/{name}/{type}").json()


def get_output(context: UFDLServerContext, url: str, pk: int, name: str, type: str) -> Iterator[bytes]:
    return context.download(f"{url}/{pk}/outputs/{name}/{type}").iter_content(chunk_size=None)

# endregion

# region ClearDatasetViewSet


def clear(context: UFDLServerContext, url: str, pk: int) -> RawJSONObject:
    return context.delete(f"{url}/{pk}/clear").json()

# endregion

# region CopyableViewSet


def copy(context: UFDLServerContext, url: str, pk: int, **params) -> RawJSONObject:
    return context.post(f"{url}/{pk}/copy", params).json()

# endregion

# region CreateJobViewSet


def create_job(context: UFDLServerContext, url: str, pk: int,
               docker_image: Union[int, Tuple[str, str]],
               input_values: Dict[str, str],
               parameter_values: OptionallyPresent[Dict[str, str]] = Absent,
               description: OptionallyPresent[str] = Absent) -> RawJSONObject:
    return context.post(f"{url}/{pk}/create-job",
                        json=partial_kwargs(
                            docker_image= (docker_image
                                           if isinstance(docker_image, int)
                                           else {"name": docker_image[0], "version": docker_image[1]}),
                            input_values=input_values,
                            parameter_values=parameter_values,
                            description=description)).json()

# endregion

# region DownloadableViewSet


def download(context: UFDLServerContext, url: str, pk: int,
             filetype: OptionallyPresent[str] = Absent,
             **params) -> Iterator[bytes]:
    return context.download(f"{url}/{pk}/download", partial_kwargs(filetype=filetype,
                                                                   params=params)).iter_content(chunk_size=None)

# endregion

# region FileContainerViewSet


def add_file(context: UFDLServerContext, url: str, pk: int, filename: str, data: Union[bytes, IO[bytes]]) -> RawJSONObject:
    return context.upload(f"{url}/{pk}/files/{filename}", filename, data).json()


def get_file(context: UFDLServerContext, url: str, pk: int, filename: str) -> Iterator[bytes]:
    return context.download(f"{url}/{pk}/files/{filename}").iter_content(chunk_size=None)


def delete_file_fc(context: UFDLServerContext, url: str, pk: int, filename: str) -> RawJSONObject:
    return context.delete(f"{url}/{pk}/files/{filename}").json()


def set_metadata(context: UFDLServerContext, url: str, pk: int, filename: str, metadata: str) -> str:
    return context.post(f"{url}/{pk}/metadata/{filename}", {"metadata": metadata}).json()['metadata']


def get_metadata(context: UFDLServerContext, url: str, pk: int, filename: str) -> str:
    return context.get(f"{url}/{pk}/metadata/{filename}").json()['metadata']


def get_all_metadata(context: UFDLServerContext, url: str, pk: int) -> str:
    return context.get(f"{url}/{pk}/metadata").json()

# endregion

# region GetHardwareGenerationViewSet


def get_hardware_generation(context: UFDLServerContext, url: str, compute: float) -> RawJSONObject:
    return context.get(f"{url}/get-hardware-generation/{compute}").json()

# endregion

# region ImportTemplateViewSet


def import_template(context: UFDLServerContext, url: str, template: JobTemplateMigrationSpec) -> RawJSONObject:
    return context.post(f"{url}/import", template.to_raw_json()).json()


def export_template(context: UFDLServerContext, url: str, pk: int) -> RawJSONObject:
    return context.get(f"{url}/{pk}/export").json()


# endregion

# region InputsParametersViewSet


def add_input(context: UFDLServerContext, url: str, pk: int,
              name: str,
              type: str,
              options: OptionallyPresent[str] = Absent,
              help: OptionallyPresent[str] = Absent) -> RawJSONObject:
    return context.post(f"{url}/{pk}/inputs/{name}", partial_kwargs(type=type, options=options, help=help)).json()


def delete_input(context: UFDLServerContext, url: str, pk: int, name: str) -> RawJSONObject:
    return context.delete(f"{url}/{pk}/inputs/{name}").json()


def add_parameter(context: UFDLServerContext, url: str, pk: int,
                  name: str,
                  type: str,
                  default: OptionallyPresent[str] = Absent,
                  help: OptionallyPresent[str] = Absent) -> RawJSONObject:
    return context.post(f"{url}/{pk}/parameters/{name}", partial_kwargs(type=type, default=default, help=help)).json()


def delete_parameter(context: UFDLServerContext, url: str, pk: int, name: str) -> RawJSONObject:
    return context.delete(f"{url}/{pk}/parameters/{name}").json()

# endregion

# region LicenceSubdescriptorViewSet


def add_subdescriptors(context: UFDLServerContext, url: str, pk: int, type: str, names: List[Union[int, str]]) -> RawJSONObject:
    return context.patch(f"{url}/{pk}/subdescriptors", {"method": "add", "type": type, "names": names}).json()


def remove_subdescriptors(context: UFDLServerContext, url: str, pk: int, type: str, names: List[Union[int, str]]) -> RawJSONObject:
    return context.patch(f"{url}/{pk}/subdescriptors", {"method": "remove", "type": type, "names": names}).json()

# endregion

# region MembershipViewSet


def add_membership(context: UFDLServerContext, url: str, pk: int, username: str, permissions: str = "R") -> RawJSONObject:
    return context.patch(f"{url}/{pk}/memberships", {"method": "add", "username": username, "permissions": permissions}).json()


def remove_membership(context: UFDLServerContext, url: str, pk: int, username: str) -> RawJSONObject:
    return context.patch(f"{url}/{pk}/memberships", {"method": "remove", "username": username}).json()


def update_membership(context: UFDLServerContext, url: str, pk: int, username: str, permissions: str = "R") -> RawJSONObject:
    return context.patch(f"{url}/{pk}/memberships", {"method": "update", "username": username, "permissions": permissions}).json()


def get_permissions_for_user(context: UFDLServerContext, url: str, pk: int, username: str) -> str:
    return context.get(f"{url}/{pk}/permissions/{username}").json()

# endregion

# region MergeViewSet


def merge(context: UFDLServerContext, url: str, pk: int,
          source_pk: int,
          delete: bool,
          hard: OptionallyPresent[bool] = Absent) -> RawJSONObject:
    return context.post(f"{url}/{pk}/merge/{source_pk}", partial_kwargs(delete=delete, hard=hard)).json()

# endregion

# region SetFileViewSet


def set_file(context: UFDLServerContext, url: str, pk: int, data: Union[bytes, IO[bytes]]) -> RawJSONObject:
    return context.upload(f"{url}/{pk}/data", "data", data).json()


def delete_file_sf(context: UFDLServerContext, url: str, pk: int) -> RawJSONObject:
    return context.delete(f"{url}/{pk}/data").json()

# endregion

# region SoftDeleteViewSet


def hard_delete(context: UFDLServerContext, url: str, pk: int) -> RawJSONObject:
    return context.delete(f"{url}/{pk}/hard").json()


def reinstate(context: UFDLServerContext, url: str, pk: int) -> RawJSONObject:
    return context.delete(f"{url}/{pk}/reinstate").json()

#endregion
