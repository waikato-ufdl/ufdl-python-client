"""
Core module containing the common context for all calls made by the API.
This is the host/port the UFDL API is listening to, and the username/password
to use for authentication.
"""
# The context
_host: str = ""
_port: int = 0


def set_context(host: str, port: int):
    global _host, _port
    _host = host
    _port = port


def get_host() -> str:
    return _host


def get_port() -> int:
    return _port
