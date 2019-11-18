"""
Module for types related to authentication.
"""
from typing import Tuple, Dict

# Type of a pair of access, refresh tokens
TOKEN_PAIR_TYPE = Tuple[str, str]

# Type of the entire token cache
TOKEN_FILE_TYPE = Dict[str, TOKEN_PAIR_TYPE]
