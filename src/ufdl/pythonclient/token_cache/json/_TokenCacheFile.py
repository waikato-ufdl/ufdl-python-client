from wai.json.object import JSONObject
from wai.json.object.property import Property

from ._UserTokenMap import UserTokenMap


class TokenCacheFile(JSONObject['TokenCacheFile']):
    """
    The JSON file format for the token cache.
    """
    @classmethod
    def _additional_properties_validation(cls) -> Property:
        return UserTokenMap.as_property(optional=True)
