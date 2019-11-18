import requests

from ..functional import jwt_obtain, jwt_refresh
from ._storage import load_token_pair, store_token_pair
from ._typing import TOKEN_PAIR_TYPE


# The context
_username: str = ""
_password: str = ""
_access_token: str = ""
_refresh_token: str = ""


def set_context(username: str, password: str):
    """
    Sets the username and password to use.

    :param username:    The username.
    :param password:    The password.
    """
    global _username, _password

    _username = username
    _password = password

    clear_token_context()


def get_access_token() -> str:
    """
    Gets the current user's access token.

    :return:    The access token.
    """
    return get_token_pair()[0]


def get_refresh_token() -> str:
    """
    Gets the current user's refresh token.

    :return:    The refresh token.
    """
    return get_token_pair()[1]


def get_token_pair() -> TOKEN_PAIR_TYPE:
    """
    Gets the current user's token pair.

    :return:    The token pair.
    """
    global _access_token, _refresh_token

    # Create the token context if it's not already established.
    if _access_token == "":
        set_token_context()

    return _access_token, _refresh_token


def refresh():
    """
    Refreshes the access token using the refresh token.
    """
    global _username, _access_token, _refresh_token

    # If the token context is not yet set, set it, and
    # only continue with refresh if we didn't obtain a
    # new token pair in creating the token context
    if _refresh_token == "":
        if set_token_context():
            return

    # Attempt to refresh the access token using the refresh token
    try:
        _access_token = jwt_refresh(_refresh_token)
        store_token_pair(_username, _access_token, _refresh_token)
    except requests.HTTPError as e:
        # If we errored because the refresh token is invalid,
        # obtain a brand-new token pair
        if e.response.status_code == requests.codes.unauthorized:
            _access_token, _refresh_token = obtain_tokens_from_server()

        # Re-raise any other errors
        else:
            raise


def set_token_context() -> bool:
    """
    Sets the token context by either loading the tokens from
    cache, or obtaining new tokens from the server.

    :return:    True if the tokens were obtained from the server,
                False if loaded from cache.
    """
    global _username, _access_token, _refresh_token

    # Make sure a user has been set
    if _username == "":
        raise ValueError("Username not set. Call auth.set_context(username, password)")

    # Attempt to load the tokens from cache
    _access_token, _refresh_token = load_token_pair(_username)

    # If cache missed, obtain tokens from server
    if _access_token == "":
        _access_token, _refresh_token = obtain_tokens_from_server()
        return True

    return False


def obtain_tokens_from_server() -> TOKEN_PAIR_TYPE:
    """
    Gets tokens for the current user from the server.

    :return:    The tokens.
    """
    global _username, _password, _access_token, _refresh_token

    # Network call
    tokens = jwt_obtain(_username, _password)

    # Cache the tokens
    store_token_pair(_username, *tokens)

    return tokens


def clear_token_context():
    """
    Clears the tokens from the context so they will be regenerated
    on next request.
    """
    global _access_token, _refresh_token
    _access_token = _refresh_token = ""
