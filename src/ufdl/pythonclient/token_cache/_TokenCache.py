from abc import ABC, abstractmethod
from typing import Optional

from .._Tokens import Tokens


class TokenCache(ABC):
    """
    An abstract cache of token pairs.
    """
    @abstractmethod
    def get_cached_tokens(self, host: str, username: str) -> Optional[Tokens]:
        """
        Gets the tokens cached for the given user on the given host, if
        there are any.

        :param host:        The UFDL server host address.
        :param username:    The user on the server.
        :return:            The tokens, or None if no tokens cached for the user.
        """
        pass

    @abstractmethod
    def set_cached_tokens(self, host: str, username: str, tokens: Tokens):
        """
        Writes the tokens to the cache for the given user on the given host.

        :param host:        The UFDL server host address.
        :param username:    The user on the server.
        :param tokens:      The tokens for the user.
        """
        pass
