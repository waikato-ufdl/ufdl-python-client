from typing import Optional

from wai.json.raw import RawJSONObject, RawJSONArray

from ....constants import USERS_URL
from ... import _base_actions
from ..._util import partial_kwargs


def list() -> RawJSONArray:
    return _base_actions.list(USERS_URL)


def create(username: str,
           password: str,
           email: str,
           first_name: str = "",
           last_name: str = "") -> RawJSONObject:
    return _base_actions.create(USERS_URL, {"username": username,
                                            "password": password,
                                            "email": email,
                                            "first_name": first_name,
                                            "last_name": last_name})


def retrieve(pk: int) -> RawJSONObject:
    return _base_actions.retrieve(USERS_URL, pk)


def update(pk: int, *,
           username: str,
           password: str,
           first_name: str,
           last_name: str,
           email: str) -> RawJSONObject:
    return _base_actions.update(USERS_URL, pk, {"username": username,
                                                "password": password,
                                                "email": email,
                                                "first_name": first_name,
                                                "last_name": last_name})


def partial_update(pk: int, *,
                   username: Optional[str] = None,
                   password: Optional[str] = None,
                   first_name: Optional[str] = None,
                   last_name: Optional[str] = None,
                   email: Optional[str] = None) -> RawJSONObject:
    return _base_actions.partial_update(USERS_URL, pk, partial_kwargs(username=username,
                                                                      password=password,
                                                                      first_name=first_name,
                                                                      last_name=last_name,
                                                                      email=email))


def destroy(pk: int) -> RawJSONObject:
    return _base_actions.destroy(USERS_URL, pk)
