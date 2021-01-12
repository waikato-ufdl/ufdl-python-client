from typing import Optional

from ufdl.json.core.filter import FilterSpec

from wai.json.object import OptionallyPresent, Absent
from wai.json.raw import RawJSONObject, RawJSONArray

from ....constants import USERS_URL
from ....util import partial_kwargs
from ...._UFDLServerContext import UFDLServerContext
from ... import _base_actions


def list(context: UFDLServerContext, filter_spec: Optional[FilterSpec] = None) -> RawJSONArray:
    return _base_actions.list(context, USERS_URL, filter_spec)


def create(context: UFDLServerContext,
           username: str,
           password: str,
           email: str,
           first_name: str = "",
           last_name: str = "") -> RawJSONObject:
    return _base_actions.create(context, USERS_URL, {"username": username,
                                                     "password": password,
                                                     "email": email,
                                                     "first_name": first_name,
                                                     "last_name": last_name})


def retrieve(context: UFDLServerContext, pk: int) -> RawJSONObject:
    return _base_actions.retrieve(context, USERS_URL, pk)


def update(context: UFDLServerContext, pk: int, *,
           username: str,
           password: str,
           first_name: str,
           last_name: str,
           email: str,
           is_active: bool) -> RawJSONObject:
    return _base_actions.update(context, USERS_URL, pk, {"username": username,
                                                         "password": password,
                                                         "email": email,
                                                         "first_name": first_name,
                                                         "last_name": last_name,
                                                         "is_active": is_active})


def partial_update(context: UFDLServerContext, pk: int, *,
                   username: OptionallyPresent[str] = Absent,
                   password: OptionallyPresent[str] = Absent,
                   first_name: OptionallyPresent[str] = Absent,
                   last_name: OptionallyPresent[str] = Absent,
                   email: OptionallyPresent[str] = Absent,
                   is_active: OptionallyPresent[bool] = Absent) -> RawJSONObject:
    return _base_actions.partial_update(context, USERS_URL, pk, partial_kwargs(username=username,
                                                                               password=password,
                                                                               first_name=first_name,
                                                                               last_name=last_name,
                                                                               email=email,
                                                                               is_active=is_active))


def destroy(context: UFDLServerContext, pk: int):
    return _base_actions.destroy(context, USERS_URL, pk)
