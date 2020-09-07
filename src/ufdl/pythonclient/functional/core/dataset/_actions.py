from typing import Union, IO, Iterator, Optional

from ufdl.json.core.filter import FilterSpec

from wai.json.object import Absent, OptionallyPresent
from wai.json.raw import RawJSONObject, RawJSONArray

from ....constants import DATASETS_URL
from ....util import partial_kwargs
from ...._UFDLServerContext import UFDLServerContext
from ... import _base_actions
from .. import _mixin_actions


def list(context: UFDLServerContext, filter_spec: Optional[FilterSpec] = None) -> RawJSONArray:
    return _base_actions.list(context, DATASETS_URL, filter_spec)


def create(context: UFDLServerContext,
           name: str,
           project: int,
           licence: int,
           description: str = "",
           is_public: bool = False,
           tags: str = "") -> RawJSONObject:
    return _base_actions.create(context, DATASETS_URL, {"name": name,
                                                        "project": project,
                                                        "description": description,
                                                        "licence": licence,
                                                        "is_public": is_public,
                                                        "tags": tags})


def retrieve(context: UFDLServerContext, pk: int) -> RawJSONObject:
    return _base_actions.retrieve(context, DATASETS_URL, pk)


def update(context: UFDLServerContext, pk: int, *,
           name: str,
           description: str,
           project: int,
           licence: int,
           is_public: bool,
           tags: str) -> RawJSONObject:
    return _base_actions.update(context, DATASETS_URL, pk, {"name": name,
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
    return _base_actions.partial_update(context, DATASETS_URL, pk, partial_kwargs(name=name,
                                                                                  description=description,
                                                                                  project=project,
                                                                                  licence=licence,
                                                                                  is_public=is_public,
                                                                                  tags=tags))


def destroy(context: UFDLServerContext, pk: int) -> RawJSONObject:
    return _base_actions.destroy(context, DATASETS_URL, pk)


def download(context: UFDLServerContext, pk: int, filetype: str = "zip") -> Iterator[bytes]:
    return _mixin_actions.download(context, DATASETS_URL, pk, filetype)


def add_file(context: UFDLServerContext, pk: int, filename: str, data: Union[bytes, IO[bytes]]) -> RawJSONObject:
    return _mixin_actions.add_file(context, DATASETS_URL, pk, filename, data)


def get_file(context: UFDLServerContext, pk: int, filename: str) -> Iterator[bytes]:
    return _mixin_actions.get_file(context, DATASETS_URL, pk, filename)


def delete_file(context: UFDLServerContext, pk: int, filename: str) -> RawJSONObject:
    return _mixin_actions.delete_file_fc(context, DATASETS_URL, pk, filename)


def set_metadata(context: UFDLServerContext, pk: int, filename: str, metadata: str) -> str:
    return _mixin_actions.set_metadata(context, DATASETS_URL, pk, filename, metadata)


def get_metadata(context: UFDLServerContext, pk: int, filename: str) -> str:
    return _mixin_actions.get_metadata(context, DATASETS_URL, pk, filename)


def copy(context: UFDLServerContext, pk: int, new_name: OptionallyPresent[str] = Absent) -> RawJSONObject:
    return _mixin_actions.copy(context, DATASETS_URL, pk, **partial_kwargs(new_name=new_name))


def merge(context: UFDLServerContext, pk: int, source_pk: int, delete: bool, hard: OptionallyPresent[bool] = Absent) -> RawJSONObject:
    return _mixin_actions.merge(context, DATASETS_URL, pk, source_pk, delete, hard)


def hard_delete(context: UFDLServerContext, pk: int) -> RawJSONObject:
    return _mixin_actions.hard_delete(context, DATASETS_URL, pk)


def reinstate(context: UFDLServerContext, pk: int) -> RawJSONObject:
    return _mixin_actions.reinstate(context, DATASETS_URL, pk)
