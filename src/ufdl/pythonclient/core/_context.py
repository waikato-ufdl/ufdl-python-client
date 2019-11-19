"""
Core module containing the common context for all calls made by the API.
Currently this is just the host/port the UFDL API server is listening to.
"""
# The context
_host: str = ""
_port: int = 0


def set_context(host: str, port: int):
    """
    Sets the context for the client.

    :param host:    The UFDL server host.
    :param port:    The UFDL server port.
    """
    global _host, _port
    _host = host
    _port = port


def get_host() -> str:
    """
    Gets the UFDL server host set in the context.
    """
    return _host


def get_port() -> int:
    """
    Gets the UFDL server port set in the context.
    """
    return _port
