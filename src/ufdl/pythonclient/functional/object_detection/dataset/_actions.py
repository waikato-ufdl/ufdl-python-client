from typing import List, Iterator, Union, IO, Optional

from ufdl.json.core.filter import FilterSpec
from ufdl.json.object_detection import Annotation

from wai.json.object import OptionallyPresent, Absent
from wai.json.raw import RawJSONObject, RawJSONArray

from ....constants import OBJECT_DETECTION_DATASETS_URL
from ....util import partial_kwargs
from ...._UFDLServerContext import UFDLServerContext
from ... import _base_actions
from .. import _mixin_actions

from ...core import (
    copy as core_copy,
    download as core_download,
    add_file as core_add_file,
    get_file as core_get_file,
    delete_file_fc as core_delete_file,
    set_metadata as core_set_metadata,
    get_metadata as core_get_metadata,
    get_all_metadata as core_get_all_metadata,
    hard_delete as core_hard_delete,
    reinstate as core_reinstate,
    merge as core_merge
)


def list(context: UFDLServerContext, filter_spec: Optional[FilterSpec] = None) -> RawJSONArray:
    return _base_actions.list(context, OBJECT_DETECTION_DATASETS_URL, filter_spec)


def create(context: UFDLServerContext,
           name: str,
           project: int,
           licence: int,
           description: str = "",
           is_public: bool = False,
           tags: str = "") -> RawJSONObject:
    return _base_actions.create(context, OBJECT_DETECTION_DATASETS_URL, {"name": name,
                                                                         "project": project,
                                                                         "description": description,
                                                                         "licence": licence,
                                                                         "is_public": is_public,
                                                                         "tags": tags})


def retrieve(context: UFDLServerContext, pk: int) -> RawJSONObject:
    return _base_actions.retrieve(context, OBJECT_DETECTION_DATASETS_URL, pk)


def update(context: UFDLServerContext, pk: int, *,
           name: str,
           description: str,
           project: int,
           licence: int,
           is_public: bool,
           tags: str) -> RawJSONObject:
    return _base_actions.update(context, OBJECT_DETECTION_DATASETS_URL, pk, {"name": name,
                                                                             "project": project,
                                                                             "description": description,
                                                                             "licence": licence,
                                                                             "is_public": is_public,
                                                                             "tags": tags})


def partial_update(context: UFDLServerContext, pk: int, *,
                   name: OptionallyPresent[str] = Absent,
                   description: OptionallyPresent[str] = Absent,
                   project: OptionallyPresent[int] = Absent,
                   licence: OptionallyPresent[int] = Absent,
                   is_public: OptionallyPresent[bool] = Absent,
                   tags: OptionallyPresent[str] = Absent) -> RawJSONObject:
    return _base_actions.partial_update(context, OBJECT_DETECTION_DATASETS_URL, pk, partial_kwargs(name=name,
                                                                                                   description=description,
                                                                                                   project=project,
                                                                                                   licence=licence,
                                                                                                   is_public=is_public,
                                                                                                   tags=tags))


def destroy(context: UFDLServerContext, pk: int) -> RawJSONObject:
    return _base_actions.destroy(context, OBJECT_DETECTION_DATASETS_URL, pk)


def download(context: UFDLServerContext, pk: int,
             filetype: OptionallyPresent[str] = Absent,
             annotations_args: OptionallyPresent[List[str]] = Absent) -> Iterator[bytes]:
    return core_download(context, OBJECT_DETECTION_DATASETS_URL,
                         pk,
                         filetype,
                         **partial_kwargs(annotations_args=annotations_args))


def add_file(context: UFDLServerContext, pk: int, filename: str, data: Union[bytes, IO[bytes]]) -> RawJSONObject:
    return core_add_file(context, OBJECT_DETECTION_DATASETS_URL, pk, filename, data)


def get_file(context: UFDLServerContext, pk: int, filename: str) -> Iterator[bytes]:
    return core_get_file(context, OBJECT_DETECTION_DATASETS_URL, pk, filename)


def delete_file(context: UFDLServerContext, pk: int, filename: str) -> RawJSONObject:
    return core_delete_file(context, OBJECT_DETECTION_DATASETS_URL, pk, filename)


def set_metadata(context: UFDLServerContext, pk: int, filename: str, metadata: str) -> str:
    return core_set_metadata(context, OBJECT_DETECTION_DATASETS_URL, pk, filename, metadata)


def get_metadata(context: UFDLServerContext, pk: int, filename: str) -> str:
    return core_get_metadata(context, OBJECT_DETECTION_DATASETS_URL, pk, filename)


def get_all_metadata(context: UFDLServerContext, pk: int) -> str:
    return core_get_all_metadata(context, OBJECT_DETECTION_DATASETS_URL, pk)


def copy(context: UFDLServerContext, pk: int, new_name: OptionallyPresent[str] = Absent) -> RawJSONObject:
    return core_copy(context, OBJECT_DETECTION_DATASETS_URL, pk, **partial_kwargs(new_name=new_name))


def merge(context: UFDLServerContext, pk: int, source_pk: int, delete: bool, hard: OptionallyPresent[bool] = Absent) -> RawJSONObject:
    return core_merge(context, OBJECT_DETECTION_DATASETS_URL, pk, source_pk, delete, hard)


def hard_delete(context: UFDLServerContext, pk: int) -> RawJSONObject:
    return core_hard_delete(context, OBJECT_DETECTION_DATASETS_URL, pk)


def reinstate(context: UFDLServerContext, pk: int) -> RawJSONObject:
    return core_reinstate(context, OBJECT_DETECTION_DATASETS_URL, pk)


def get_annotations(context: UFDLServerContext, pk: int) -> RawJSONObject:
    return _mixin_actions.get_annotations(context, OBJECT_DETECTION_DATASETS_URL, pk)


def get_annotations_for_image(context: UFDLServerContext, pk: int, image: str) -> RawJSONObject:
    return _mixin_actions.get_annotations_for_image(context, OBJECT_DETECTION_DATASETS_URL, pk, image)


def set_annotations_for_image(context: UFDLServerContext, pk: int, image: str, annotations: List[Annotation]):
    _mixin_actions.set_annotations_for_image(context, OBJECT_DETECTION_DATASETS_URL, pk, image, annotations)


def delete_annotations_for_image(context: UFDLServerContext, pk: int, image: str):
    _mixin_actions.delete_annotations_for_image(context, OBJECT_DETECTION_DATASETS_URL, pk, image)
