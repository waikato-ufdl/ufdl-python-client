import os
from typing import Optional

from wai.json.error import JSONSerialisationError

from ...util import get_ufdl_config_dir
from ..._Tokens import Tokens
from .._TokenCache import TokenCache
from ._TokenCacheFile import TokenCacheFile
from ._TokenPair import TokenPair


class JSONTokenCache(TokenCache):
    """
    A token cache that stores the tokens on disk in a JSON file.
    """
    def __init__(self, filename: Optional[str] = None):
        # If no filename is provided, default to 'tokens.json' in the
        # default UFDL config directory
        if filename is None:
            filename = os.path.join(get_ufdl_config_dir(), "tokens.json")

        self._filename: str = filename

    def get_cached_tokens(self, host: str, username: str) -> Optional[Tokens]:
        # Load the cache file
        cache = self._load_file()

        # If there are no cached tokens for the host, return None
        if host not in cache:
            return None

        # Get the user -> token map for the host
        user_map = cache[host]

        # If the user isn't in the map, return None
        if username not in user_map:
            return None

        # Get the tokens for the user
        tokens = user_map[username]

        return Tokens(tokens.access, tokens.refresh)

    def set_cached_tokens(self, host: str, username: str, tokens: Tokens):
        # Load the cache file
        cache = self._load_file()

        # If there are no cached tokens for the host, create an empty user-map
        if host not in cache:
            cache[host] = {}

        # Convert the tokens to JSON
        json_tokens = TokenPair(access=tokens.access, refresh=tokens.refresh)

        # Set the tokens in the user-map
        cache[host][username] = json_tokens

        # Save the cache to disk
        cache.save_json_to_file(self._filename, 2)

    def _load_file(self) -> TokenCacheFile:
        """
        Loads the token cache file from disk, creating it if it doesn't exist.

        :return:    The token cache file.
        """
        if not os.path.exists(self._filename):
            return TokenCacheFile()

        try:
            return TokenCacheFile.load_json_from_file(self._filename)
        except JSONSerialisationError:
            return TokenCacheFile()
