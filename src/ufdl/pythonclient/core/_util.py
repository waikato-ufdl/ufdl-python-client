from typing import Dict

from ._context import get_host, get_port


def format_url(url: str) -> str:
    return f"http://{get_host()}:{get_port()}/{url}"


def get_auth_headers() -> Dict[str, str]:
    from ..auth import get_access_token
    return {"Authorization": f"Bearer {get_access_token()}"}
