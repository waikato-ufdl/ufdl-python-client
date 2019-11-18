from typing import Tuple

import requests

from ..core import post
from ..constants import JWT_OBTAIN_TOKEN_URL, JWT_REFRESH_TOKEN_URL, JWT_VERIFY_TOKEN_URL


def jwt_obtain(username: str, password: str) -> Tuple[str, str]:
    response = post(JWT_OBTAIN_TOKEN_URL,
                    {"username": username, "password": password},
                    auth=False)

    json = response.json()

    return json["access"], json["refresh"]


def jwt_refresh(refresh_token: str) -> str:
    response = post(JWT_REFRESH_TOKEN_URL,
                    {"refresh": refresh_token},
                    auth=False)

    json = response.json()

    return json["access"]


def jwt_verify(token: str) -> bool:
    try:
        response = post(JWT_VERIFY_TOKEN_URL,
                        {"token": token},
                        auth=False)
    except requests.HTTPError:
        return False
