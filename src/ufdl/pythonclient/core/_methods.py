from typing import Any, Dict

import requests

from ._util import format_url, get_auth_headers


def raise_for_response(response: requests.Response) -> requests.Response:
    """
    Calls raise_for_status on the given response object, or returns the
    same object if it doesn't raise.

    :param response:    The response object.
    :return:            The same response object.
    """
    # Call raise for status
    response.raise_for_status()

    return response


def set_auth_headers(kwargs):
    """
    Sets the authentication headers in the given method keyword arguments.

    :param kwargs:  The keyword arguments.
    """
    headers = kwargs.pop("headers", {})
    headers.update(get_auth_headers())
    kwargs["headers"] = headers


def retry_on_expired_access_token(method, *args, **kwargs) -> requests.Response:
    """
    Calls the provided method with the given arguments, and if it errors
    because the access token is expired, attempts to refresh it and retry the call.

    :param method:      The method to call.
    :param args:        The method positional arguments.
    :param kwargs:      The method keyword arguments.
    :return:            The result of calling the method.
    """
    try:
        set_auth_headers(kwargs)
        return raise_for_response(method(*args, **kwargs))
    except requests.HTTPError as e:
        # If we errored on an expired token, refresh and retry
        if e.response.status_code == requests.codes.unauthorized:
            # Refresh
            from ..auth import refresh
            refresh()

            # Retry
            set_auth_headers(kwargs)
            return raise_for_response(method(*args, **kwargs))

        # Re-raise any other errors
        else:
            raise


def handle_auth(auth: bool, method, *args, **kwargs) -> requests.Response:
    """
    Handles the application of authentication to the given method call.

    :param auth:    Whether to use authentication.
    :param method:  The requests HTTP verb method.
    :param args:    Any positional arguments.
    :param kwargs:  Any keyword arguments.
    :return:        The response from the method call.
    """
    if auth:
        return retry_on_expired_access_token(method, *args, **kwargs)
    else:
        return raise_for_response(method(*args, **kwargs))


def post(url: str, json: Dict[str, Any], *, auth: bool = True) -> requests.Response:
    return handle_auth(auth, requests.post, format_url(url), json=json)


def get(url: str, *, auth: bool = True) -> requests.Response:
    return handle_auth(auth, requests.get, format_url(url))


def put(url: str, json: Dict[str, Any], *, auth: bool = True) -> requests.Response:
    return handle_auth(auth, requests.put, format_url(url), json=json)


def patch(url: str, json: Dict[str, Any], *, auth: bool = True) -> requests.Response:
    return handle_auth(auth, requests.patch, format_url(url), json=json)


def delete(url: str, *, auth: bool = True) -> requests.Response:
    return handle_auth(auth, requests.delete, format_url(url))
