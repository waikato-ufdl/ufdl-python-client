from typing import Optional

from wai.common.json import RawJSONObject, RawJSONArray

from ....constants import PROJECTS_URL
from ... import _base_actions
from ..._util import partial_kwargs


def list() -> RawJSONArray:
    return _base_actions.list(PROJECTS_URL)


def create(name: str,
           team: int):
    _base_actions.create(PROJECTS_URL,
                         name=name,
                         team=team)


def retrieve(pk: int) -> RawJSONObject:
    return _base_actions.retrieve(PROJECTS_URL, pk)


def update(pk: int, *,
           name: str,
           team: int):
    _base_actions.update(PROJECTS_URL, pk,
                         name=name,
                         team=team)


def partial_update(pk: int, *,
                   name: Optional[str] = None,
                   team: Optional[int] = None):
    _base_actions.partial_update(PROJECTS_URL, pk, **partial_kwargs(name=name,
                                                                    team=team))


def destroy(pk: int):
    _base_actions.destroy(PROJECTS_URL, pk)