from wai.json.object import StrictJSONObject
from wai.json.object.property import StringProperty


class TokenPair(StrictJSONObject['TokenPair']):
    """
    Represents a single token pair (access/refresh) as JSON.
    """
    # The access token
    access: str = StringProperty()

    # The refresh token
    refresh: str = StringProperty()
