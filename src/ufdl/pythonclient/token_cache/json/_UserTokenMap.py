from wai.json.object import JSONObject
from wai.json.object.property import Property

from ._TokenPair import TokenPair


class UserTokenMap(JSONObject['UserTokenMap']):
    """
    A JSON object which maps usernames to token pairs.
    """
    @classmethod
    def _additional_properties_validation(cls) -> Property:
        return TokenPair.as_property(optional=True)
