from typing import IO, Iterator, List, Optional, Union

from ufdl.json.core.filter import FilterSpec
from wai.json.object import Absent, OptionallyPresent
from wai.json.raw import RawJSONArray, RawJSONObject

from .. import _mixin_actions
from ... import _base_actions
from ...core import (
    add_file as core_add_file,
    clear as core_clear,
    copy as core_copy,
    delete_file_fc as core_delete_file,
    download as core_download,
    get_all_metadata as core_get_all_metadata,
    get_file as core_get_file,
    get_metadata as core_get_metadata,
    hard_delete as core_hard_delete,
    merge as core_merge,
    reinstate as core_reinstate,
    set_metadata as core_set_metadata
)
from ...._UFDLServerContext import UFDLServerContext
from ....constants import IMAGE_SEGMENTATION_DATASETS_URL
from ....util import partial_kwargs


def list(
        context: UFDLServerContext,
        filter_spec: Optional[FilterSpec] = None
) -> RawJSONArray:
    return _base_actions.list(
        context,
        IMAGE_SEGMENTATION_DATASETS_URL,
        filter_spec
    )


def create(
        context: UFDLServerContext,
        name: str,
        project: int,
        licence: int,
        description: str = "",
        is_public: bool = False,
        tags: str = ""
) -> RawJSONObject:
    return _base_actions.create(
        context,
        IMAGE_SEGMENTATION_DATASETS_URL,
        {
            "name": name,
            "project": project,
            "description": description,
            "licence": licence,
            "is_public": is_public,
            "tags": tags
        }
    )


def retrieve(
        context: UFDLServerContext,
        pk: int
) -> RawJSONObject:
    return _base_actions.retrieve(
        context,
        IMAGE_SEGMENTATION_DATASETS_URL,
        pk
    )


def update(
        context: UFDLServerContext,
        pk: int,
        *,
        name: str,
        description: str,
        project: int,
        licence: int,
        is_public: bool,
        tags: str
) -> RawJSONObject:
    return _base_actions.update(
        context,
        IMAGE_SEGMENTATION_DATASETS_URL,
        pk,
        {
            "name": name,
            "project": project,
            "description": description,
            "licence": licence,
            "is_public": is_public,
            "tags": tags
        }
    )


def partial_update(
        context: UFDLServerContext,
        pk: int,
        *,
        name: OptionallyPresent[str] = Absent,
        description: OptionallyPresent[str] = Absent,
        project: OptionallyPresent[int] = Absent,
        licence: OptionallyPresent[int] = Absent,
        is_public: OptionallyPresent[bool] = Absent,
        tags: OptionallyPresent[str] = Absent
) -> RawJSONObject:
    return _base_actions.partial_update(
        context,
        IMAGE_SEGMENTATION_DATASETS_URL,
        pk,
        partial_kwargs(
            name=name,
            description=description,
            project=project,
            licence=licence,
            is_public=is_public,
            tags=tags
        )
    )


def destroy(
        context: UFDLServerContext,
        pk: int
) -> RawJSONObject:
    return _base_actions.destroy(
        context,
        IMAGE_SEGMENTATION_DATASETS_URL,
        pk
    )


def download(
        context: UFDLServerContext,
        pk: int,
        filetype: OptionallyPresent[str] = Absent,
        annotations_args: OptionallyPresent[List[str]] = Absent
) -> Iterator[bytes]:
    return core_download(
        context,
        IMAGE_SEGMENTATION_DATASETS_URL,
        pk,
        filetype,
        **partial_kwargs(
            annotations_args=annotations_args
        )
    )


def add_file(
        context: UFDLServerContext,
        pk: int,
        filename: str,
        data: Union[bytes, IO[bytes]]
) -> RawJSONObject:
    return core_add_file(
        context,
        IMAGE_SEGMENTATION_DATASETS_URL,
        pk,
        filename,
        data
    )


def get_file(
        context: UFDLServerContext,
        pk: int,
        filename: str
) -> Iterator[bytes]:
    return core_get_file(
        context,
        IMAGE_SEGMENTATION_DATASETS_URL,
        pk,
        filename
    )


def delete_file(
        context: UFDLServerContext,
        pk: int,
        filename: str
) -> RawJSONObject:
    return core_delete_file(
        context,
        IMAGE_SEGMENTATION_DATASETS_URL,
        pk,
        filename
    )


def set_metadata(
        context: UFDLServerContext,
        pk: int,
        filename: str,
        metadata: str
) -> str:
    return core_set_metadata(
        context,
        IMAGE_SEGMENTATION_DATASETS_URL,
        pk,
        filename,
        metadata
    )


def get_metadata(
        context: UFDLServerContext,
        pk: int,
        filename: str
) -> str:
    return core_get_metadata(
        context,
        IMAGE_SEGMENTATION_DATASETS_URL,
        pk,
        filename
    )


def get_all_metadata(
        context: UFDLServerContext,
        pk: int
) -> str:
    return core_get_all_metadata(
        context,
        IMAGE_SEGMENTATION_DATASETS_URL,
        pk
    )


def copy(
        context: UFDLServerContext,
        pk: int,
        new_name: OptionallyPresent[str] = Absent
) -> RawJSONObject:
    return core_copy(
        context,
        IMAGE_SEGMENTATION_DATASETS_URL,
        pk,
        **partial_kwargs(
            new_name=new_name
        )
    )


def merge(
        context: UFDLServerContext,
        pk: int,
        source_pk: int,
        delete: bool,
        hard: OptionallyPresent[bool] = Absent
) -> RawJSONObject:
    return core_merge(
        context,
        IMAGE_SEGMENTATION_DATASETS_URL,
        pk,
        source_pk,
        delete,
        hard
    )


def hard_delete(
        context: UFDLServerContext,
        pk: int
) -> RawJSONObject:
    return core_hard_delete(
        context,
        IMAGE_SEGMENTATION_DATASETS_URL,
        pk
    )


def reinstate(
        context: UFDLServerContext,
        pk: int
) -> RawJSONObject:
    return core_reinstate(
        context,
        IMAGE_SEGMENTATION_DATASETS_URL,
        pk
    )


def clear(
        context: UFDLServerContext,
        pk: int
) -> RawJSONObject:
    return core_clear(
        context,
        IMAGE_SEGMENTATION_DATASETS_URL,
        pk
    )


def get_layer(
        context: UFDLServerContext,
        pk: int,
        filename: str,
        label: str
) -> Iterator[bytes]:
    return _mixin_actions.get_layer(
        context,
        IMAGE_SEGMENTATION_DATASETS_URL,
        pk,
        filename,
        label
    )


def set_layer(
        context: UFDLServerContext,
        pk: int,
        filename: str,
        label: str,
        mask: Union[bytes, IO[bytes]]
) -> str:
    return _mixin_actions.set_layer(
        context,
        IMAGE_SEGMENTATION_DATASETS_URL,
        pk,
        filename,
        label,
        mask
    )


def get_labels(
        context: UFDLServerContext,
        pk: int
) -> List[str]:
    return _mixin_actions.get_labels(
        context,
        IMAGE_SEGMENTATION_DATASETS_URL,
        pk
    )


def set_labels(
        context: UFDLServerContext,
        pk: int,
        labels: List[str]
) -> List[str]:
    return _mixin_actions.set_labels(
        context,
        IMAGE_SEGMENTATION_DATASETS_URL,
        pk,
        labels
    )
