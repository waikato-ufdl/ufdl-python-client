"""
Utility methods for working with requests.
"""
from typing import Dict

from ._context import get_host, get_port


def format_url(url: str) -> str:
    """
    Takes the URL for the API end-point and constructs
    the entire URL from it.

    :param url:     The end-point URL relative to the server.
    :return:        The complete URL.
    """
    return f"http://{get_host()}:{get_port()}/{url}"


def get_auth_headers() -> Dict[str, str]:
    """
    Creates the authorisation header required for access to
    the server.

    :return:    The authorisation header.
    """
    from ..auth import get_access_token
    return {"Authorization": f"Bearer {get_access_token()}"}
