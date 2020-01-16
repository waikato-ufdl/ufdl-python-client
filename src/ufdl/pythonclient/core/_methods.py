"""
Module for HTTP verb functions (GET, POST, PUT, PATCH, DELETE) specifically
suited to communicating with the UFDL server. Each function takes a URL on
the server (just the host-relative portion), and for methods where it is
relevant (POST, PUT, PATCH), the JSON data payload. Each function also
has a keyword-only argument 'auth', which can be set to False to disable
the use of JWT authentication. The functions all return the response
object from the server, and automatically raise a requests.HTTPError on
4XX/5XX return status.
"""
from typing import Any, Dict, Union, IO

import requests

from ._util import format_url, get_auth_headers, format_params


def raise_for_response(response: requests.Response) -> requests.Response:
    """
    Calls raise_for_status on the given response object, or returns the
    same object if it doesn't raise.

    :param response:    The response object.
    :return:            The same response object.
    """
    # Call raise for status
    try:
        response.raise_for_status()
    except requests.HTTPError as e:
        # Attach the detail message to the error if there is one
        e.detail = response.content.decode()
        raise

    return response


def set_auth_headers(kwargs):
    """
    Sets the authentication headers in the given method keyword arguments.

    :param kwargs:  The keyword arguments.
    """
    # Get the current set of headers from the kwargs, if any
    headers = kwargs.pop("headers", {})

    # Add the authentication headers
    headers.update(get_auth_headers())

    # Put the headers back into the kwargs
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
        # Set the authentication token in the headers
        set_auth_headers(kwargs)

        # Call the method and raise any response errors
        return raise_for_response(method(*args, **kwargs))
    except requests.HTTPError as e:
        # If we errored on an expired token, refresh and retry
        if e.response.status_code == requests.codes.unauthorized:
            # Refresh the access token
            from ..auth import refresh
            refresh()

            # Retry the request (same as try block above)
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


def get(url: str, *, auth: bool = True, **params) -> requests.Response:
    return handle_auth(auth, requests.get, f"{format_url(url)}{format_params(params)}")


def put(url: str, json: Dict[str, Any], *, auth: bool = True) -> requests.Response:
    return handle_auth(auth, requests.put, format_url(url), json=json)


def patch(url: str, json: Dict[str, Any], *, auth: bool = True) -> requests.Response:
    return handle_auth(auth, requests.patch, format_url(url), json=json)


def delete(url: str, *, auth: bool = True) -> requests.Response:
    return handle_auth(auth, requests.delete, format_url(url))


def upload(url: str, filename: str, data: Union[bytes, IO[bytes]], *, auth: bool = True) -> requests.Response:
    return handle_auth(auth, requests.post, format_url(url), data=data,
                       headers={"Content-Disposition": f"attachment; filename={filename}"})


def upload_file(url: str, filename: str, *, auth: bool = True) -> requests.Response:
    with open(filename, 'rb') as file:
        return upload(url, filename, file, auth=auth)
