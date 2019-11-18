from wai.common.json import RawJSONObject, RawJSONArray

from ..core import get, post, patch, put, delete


def list(url: str) -> RawJSONArray:
    return get(url).json()


def create(url: str, **params):
    post(url, params)


def retrieve(url: str, pk: int) -> RawJSONObject:
    return get(object_url(url, pk)).json()


def update(url: str, pk: int, **params):
    put(object_url(url, pk), params)


def partial_update(url: str, pk: int, **params):
    patch(object_url(url, pk), params)


def destroy(url: str, pk: int):
    delete(object_url(url, pk))


def object_url(base_url: str, object_pk: int) -> str:
    """
    Combines a base model URL with the primary key of a
    particular instance of the model into an instance-
    specific URL.

    :param base_url:    The base URL of the model.
    :param object_pk:   The primary key of the instance.
    :return:            The instance-specific URL.
    """
    return base_url + str(object_pk) + "/"
