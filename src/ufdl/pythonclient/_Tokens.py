class Tokens:
    """
    Represents a pair of access/refresh JWT tokens.
    """
    def __init__(self, access: str, refresh: str):
        self._access: str = access
        self._refresh: str = refresh

    @property
    def access(self) -> str:
        return self._access

    @property
    def refresh(self):
        return self._refresh
