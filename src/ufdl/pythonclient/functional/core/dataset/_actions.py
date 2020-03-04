from typing import Optional, Union, IO, Iterator

from wai.json.raw import RawJSONObject, RawJSONArray

from ....constants import DATASETS_URL
from ... import _base_actions
from .. import _mixin_actions
from ..._util import partial_kwargs


def list() -> RawJSONArray:
    return _base_actions.list(DATASETS_URL)


def create(name: str,
           project: int,
           version: int = 1,
           licence: str = "proprietary",
           is_public: bool = False,
           tags: str = "") -> RawJSONObject:
    return _base_actions.create(DATASETS_URL,
                                name=name,
                                project=project,
                                version=version,
                                licence=licence,
                                is_public=is_public,
                                tags=tags)


def retrieve(pk: int) -> RawJSONObject:
    return _base_actions.retrieve(DATASETS_URL, pk)


def update(pk: int, *,
           name: str,
           version: int,
           project: int,
           licence: str,
           is_public: bool,
           tags: str) -> RawJSONObject:
    return _base_actions.update(DATASETS_URL, pk,
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
    return _base_actions.partial_update(DATASETS_URL, pk, **partial_kwargs(name=name,
                                                                           version=version,
                                                                           project=project,
                                                                           licence=licence,
                                                                           is_public=is_public,
                                                                           tags=tags))


def destroy(pk: int) -> RawJSONObject:
    return _base_actions.destroy(DATASETS_URL, pk)


def download(pk: int, filetype: str = "zip") -> Iterator[bytes]:
    return _mixin_actions.download(DATASETS_URL, pk, filetype)


def add_file(pk: int, filename: str, data: Union[bytes, IO[bytes]]) -> RawJSONObject:
    return _mixin_actions.add_file(DATASETS_URL, pk, filename, data)


def get_file(pk: int, filename: str) -> Iterator[bytes]:
    return _mixin_actions.get_file(DATASETS_URL, pk, filename)


def delete_file(pk: int, filename: str) -> RawJSONObject:
    return _mixin_actions.delete_file(DATASETS_URL, pk, filename)


def copy(pk: int, new_name: Optional[str] = None) -> RawJSONObject:
    params = {"new_name": new_name} if new_name is not None else {}
    return _mixin_actions.copy(DATASETS_URL, pk, **params)
