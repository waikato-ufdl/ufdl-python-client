from typing import List, Optional, Iterator, Union, IO

from wai.json.raw import RawJSONObject, RawJSONArray

from .. import _mixin_actions
from ....constants import IMAGE_CLASSIFICATION_DATASETS_URL
from ..._util import partial_kwargs
from ... import _base_actions

from ...core import (
    copy as core_copy,
    download as core_download,
    add_file as core_add_file,
    get_file as core_get_file,
    delete_file as core_delete_file,
)


def list() -> RawJSONArray:
    return _base_actions.list(IMAGE_CLASSIFICATION_DATASETS_URL)


def create(name: str,
           project: int,
           version: int = 1,
           licence: str = "proprietary",
           is_public: bool = False,
           tags: str = "") -> RawJSONObject:
    return _base_actions.create(IMAGE_CLASSIFICATION_DATASETS_URL,
                                name=name,
                                project=project,
                                version=version,
                                licence=licence,
                                is_public=is_public,
                                tags=tags)


def retrieve(pk: int) -> RawJSONObject:
    return _base_actions.retrieve(IMAGE_CLASSIFICATION_DATASETS_URL, pk)


def update(pk: int, *,
           name: str,
           version: int,
           project: int,
           licence: str,
           is_public: bool,
           tags: str) -> RawJSONObject:
    return _base_actions.update(IMAGE_CLASSIFICATION_DATASETS_URL, pk,
                                name=name,
                                version=version,
                                project=project,
                                licence=licence,
                                is_public=is_public,
                                tags=tags)


def partial_update(pk: int, *,
                   name: Optional[str] = None,
                   version: Optional[int] = None,
                   project: Optional[int] = None,
                   licence: Optional[str] = None,
                   is_public: Optional[bool] = None,
                   tags: Optional[str] = None) -> RawJSONObject:
    return _base_actions.partial_update(IMAGE_CLASSIFICATION_DATASETS_URL, pk, **partial_kwargs(name=name,
                                                                           version=version,
                                                                           project=project,
                                                                           licence=licence,
                                                                           is_public=is_public,
                                                                           tags=tags))


def destroy(pk: int) -> RawJSONObject:
    return _base_actions.destroy(IMAGE_CLASSIFICATION_DATASETS_URL, pk)


def download(pk: int, filetype: str = "zip") -> Iterator[bytes]:
    return core_download(IMAGE_CLASSIFICATION_DATASETS_URL, pk, filetype)


def add_file(pk: int, filename: str, data: Union[bytes, IO[bytes]]) -> RawJSONObject:
    return core_add_file(IMAGE_CLASSIFICATION_DATASETS_URL, pk, filename, data)


def get_file(pk: int, filename: str) -> Iterator[bytes]:
    return core_get_file(IMAGE_CLASSIFICATION_DATASETS_URL, pk, filename)


def delete_file(pk: int, filename: str) -> RawJSONObject:
    return core_delete_file(IMAGE_CLASSIFICATION_DATASETS_URL, pk, filename)


def copy(pk: int, new_name: Optional[str] = None) -> RawJSONObject:
    params = {"new_name": new_name} if new_name is not None else {}
    return core_copy(IMAGE_CLASSIFICATION_DATASETS_URL, pk, **params)


def get_categories(pk: int) -> RawJSONObject:
    return _mixin_actions.get_categories(IMAGE_CLASSIFICATION_DATASETS_URL, pk)


def add_categories(pk: int, images: List[str], categories: List[str]) -> RawJSONObject:
    return _mixin_actions.add_categories(IMAGE_CLASSIFICATION_DATASETS_URL, pk, images, categories)


def remove_categories(pk: int, images: List[str], categories: List[str]) -> RawJSONObject:
    return _mixin_actions.remove_categories(IMAGE_CLASSIFICATION_DATASETS_URL, pk, images, categories)
