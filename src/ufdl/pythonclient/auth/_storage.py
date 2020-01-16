"""
Module with functions for handling the storage and retrieval of
JWT tokens cached to disk. This is so users can reuse tokens
between application runs.
"""
import os
import json

from ._typing import TOKEN_FILE_TYPE, TOKEN_PAIR_TYPE


def get_ufdl_config_dir() -> str:
    """
    Gets the directory in which to store app configuration. Based on
    code from https://stackoverflow.com/a/3250952.

    On Windows, %APPDATA%\\ufdl\
    On Linux, $XDG_CONFIG_HOME/ufdl/

    If the relevant environment variable for the platform is not set,
    defaults to ~/.config/ufdl/

    :return:    The directory string.
    """
    # Get the system app configuration standard location
    config_dir = os.environ['APPDATA'] if 'APPDATA' in os.environ \
        else os.environ['XDG_CONFIG_HOME'] if 'XDG_CONFIG_HOME' in os.environ \
        else os.path.join(os.environ['HOME'], '.config')

    # Define a folder for our configuration in the standard location
    ufdl_config_dir = os.path.join(config_dir, 'ufdl')

    # Make sure the location exists
    if not os.path.exists(ufdl_config_dir):
        os.mkdir(ufdl_config_dir)

    return ufdl_config_dir


# The file to store the token cache in
TOKEN_FILE = os.path.join(get_ufdl_config_dir(), "tokens.json")


def store_token_pair(username: str, access_token: str, refresh_token: str):
    """
    Stores a pair of access/refresh tokens against the given user
    in the token file.

    :param username:        The username of the user.
    :param access_token:    The access token.
    :param refresh_token:   The refresh token.
    """
    # Load the token file as it currently stands
    tokens = load_token_file()

    # Update the given user's tokens
    tokens[username] = (access_token, refresh_token)

    # Re-save the token file
    save_token_file(tokens)


def load_token_pair(username: str) -> TOKEN_PAIR_TYPE:
    """
    Loads the access/refresh tokens for a particular user
    from the token file.

    :param username:    The username of the user.
    :return:            Access token, refresh token.
    """
    # Load the token file
    tokens = load_token_file()

    # Default to empty tokens for missing users.
    if username not in tokens:
        return "", ""

    return tokens[username]


def load_token_file() -> TOKEN_FILE_TYPE:
    """
    Loads the token cache from disk.

    :return:    The token cache.
    """
    # Make sure the file exists
    if not os.path.exists(TOKEN_FILE):
        return {}

    # Load and parse the file
    with open(TOKEN_FILE, "r") as file:
        tokens = json.load(file)

    # Arrays are converted to Python lists by default.
    # Reformat to tuples instead for the token pairs
    tokens = {user: tuple(token_pair) for user, token_pair in tokens.items()}

    return tokens


def save_token_file(tokens: TOKEN_FILE_TYPE):
    """
    Saves the token cache to disk.

    :param tokens:  The token cache.
    """
    with open(TOKEN_FILE, "w") as file:
        json.dump(tokens, file, indent=2)
