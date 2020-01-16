from typing import Any, Dict


def partial_kwargs(**kwargs) -> Dict[str, Any]:
    """
    Takes the kwargs provided to an action and removes any
    that are valued None so that the server uses the default
    value it specifies.

    :param kwargs:  The full set of keyword arguments.
    :return:        The keyword arguments with set values.
    """
    return {
        key: value
        for key, value in kwargs.items()
        if value is not None
    }
