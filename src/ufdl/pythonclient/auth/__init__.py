"""
Package for managing user authentication/authorisation.

Provides the ability to set a user context (username, password), which
is then used to manage JWT tokens for the user. Tokens are stored in
a disk cache so that they can be reused between application runs/user
switches.
"""
from ._context import set_context, get_access_token, get_refresh_token, get_token_pair, refresh
from ._typing import TOKEN_PAIR_TYPE
