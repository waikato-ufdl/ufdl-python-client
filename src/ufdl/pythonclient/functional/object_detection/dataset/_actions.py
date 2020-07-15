from typing import List, Iterator, Union, IO

from ufdl.json.object_detection import Annotation

from wai.json.object import OptionallyPresent, Absent
from wai.json.raw import RawJSONObject, RawJSONArray

from .. import _mixin_actions
from ....constants import OBJECT_DETECTION_DATASETS_URL
from ..._util import partial_kwargs
from ... import _base_actions

from ...core import (
    copy as core_copy,
    download as core_download,
    add_file as core_add_file,
    get_file as core_get_file,
    delete_file as core_delete_file,
    set_metadata as core_set_metadata,
    get_metadata as core_get_metadata,
    hard_delete as core_hard_delete,
    reinstate as core_reinstate
)


def list() -> RawJSONArray:
    return _base_actions.list(OBJECT_DETECTION_DATASETS_URL)


def create(name: str,
           project: int,
           licence: int,
           description: str = "",
           is_public: bool = False,
           tags: str = "") -> RawJSONObject:
    return _base_actions.create(OBJECT_DETECTION_DATASETS_URL, {"name": name,
                                                                "project": project,
                                                                "description": description,
                                                                "licence": licence,
                                                                "is_public": is_public,
                                                                "tags": tags})


def retrieve(pk: int) -> RawJSONObject:
    return _base_actions.retrieve(OBJECT_DETECTION_DATASETS_URL, pk)


def update(pk: int, *,
           name: str,
           description: str,
           project: int,
           licence: int,
           is_public: bool,
           tags: str) -> RawJSONObject:
    return _base_actions.update(OBJECT_DETECTION_DATASETS_URL, pk, {"name": name,
                                                                    "project": project,
                                                                    "description": description,
                                                                    "licence": licence,
                                                                    "is_public": is_public,
                                                                    "tags": tags})


def partial_update(pk: int, *,
                   name: OptionallyPresent[str] = Absent,
                   description: OptionallyPresent[str] = Absent,
                   project: OptionallyPresent[int] = Absent,
                   licence: OptionallyPresent[int] = Absent,
                   is_public: OptionallyPresent[bool] = Absent,
                   tags: OptionallyPresent[str] = Absent) -> RawJSONObject:
    return _base_actions.partial_update(OBJECT_DETECTION_DATASETS_URL, pk, partial_kwargs(name=name,
                                                                                          description=description,
                                                                                          project=project,
                                                                                          licence=licence,
                                                                                          is_public=is_public,
                                                                                          tags=tags))


def destroy(pk: int) -> RawJSONObject:
    return _base_actions.destroy(OBJECT_DETECTION_DATASETS_URL, pk)


def download(pk: int,
             filetype: str = "zip",
             annotations_args: OptionallyPresent[List[str]] = Absent) -> Iterator[bytes]:
    return core_download(OBJECT_DETECTION_DATASETS_URL,
                         pk,
                         filetype,
                         **partial_kwargs(annotations_args=annotations_args))


def add_file(pk: int, filename: str, data: Union[bytes, IO[bytes]]) -> RawJSONObject:
    return core_add_file(OBJECT_DETECTION_DATASETS_URL, pk, filename, data)


def get_file(pk: int, filename: str) -> Iterator[bytes]:
    return core_get_file(OBJECT_DETECTION_DATASETS_URL, pk, filename)


def delete_file(pk: int, filename: str) -> RawJSONObject:
    return core_delete_file(OBJECT_DETECTION_DATASETS_URL, pk, filename)


def set_metadata(pk: int, filename: str, metadata: str) -> str:
    return core_set_metadata(OBJECT_DETECTION_DATASETS_URL, pk, filename, metadata)


def get_metadata(pk: int, filename: str) -> str:
    return core_get_metadata(OBJECT_DETECTION_DATASETS_URL, pk, filename)


def copy(pk: int, new_name: OptionallyPresent[str] = Absent) -> RawJSONObject:
    return core_copy(OBJECT_DETECTION_DATASETS_URL, pk, **partial_kwargs(new_name=new_name))


def hard_delete(pk: int) -> RawJSONObject:
    return core_hard_delete(OBJECT_DETECTION_DATASETS_URL, pk)


def reinstate(pk: int) -> RawJSONObject:
    return core_reinstate(OBJECT_DETECTION_DATASETS_URL, pk)


def get_annotations(pk: int) -> RawJSONObject:
    return _mixin_actions.get_annotations(OBJECT_DETECTION_DATASETS_URL, pk)


def get_annotations_for_image(pk: int, image: str) -> RawJSONObject:
    return _mixin_actions.get_annotations_for_image(OBJECT_DETECTION_DATASETS_URL, pk, image)


def set_annotations_for_image(pk: int, image: str, annotations: List[Annotation]):
    _mixin_actions.set_annotations_for_image(OBJECT_DETECTION_DATASETS_URL, pk, image, annotations)


def delete_annotations_for_image(pk: int, image: str):
    _mixin_actions.delete_annotations_for_image(OBJECT_DETECTION_DATASETS_URL, pk, image)
