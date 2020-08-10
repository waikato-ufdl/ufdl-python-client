from typing import Optional, Union, IO, Dict, Any

import requests

from wai.json.raw import RawJSONObject

from .util import raise_for_response
from .token_cache import TokenCache
from .token_cache.json import JSONTokenCache
from .constants import JWT_OBTAIN_TOKEN_URL, JWT_REFRESH_TOKEN_URL, JWT_VERIFY_TOKEN_URL
from ._Tokens import Tokens
from ._typing import Headers


class UFDLServerContext:
    """
    The connection context to a UFDL server.
    """
    def __init__(self,
                 host: str,
                 username: str, password: str,
                 token_cache: Optional[TokenCache] = None):
        self._host: str = host
        self._username: str = username
        self._password: str = password

        self._token_cache = token_cache if token_cache is not None else JSONTokenCache()

        self._tokens: Optional[Tokens] = None

    @property
    def host(self) -> str:
        return self._host

    def change_server(self, host: str):
        self._tokens = None
        self._host = host

    @property
    def username(self) -> str:
        return self._username

    @property
    def password(self) -> str:
        return self._password

    def change_user(self, username: str, password: str):
        self._tokens = None
        self._username = username
        self._password = password

    @property
    def _auth_headers(self) -> Headers:
        return {"Authorization": f"Bearer {self.access_token}"}

    @property
    def access_token(self) -> str:
        return self.tokens.access

    @property
    def refresh_token(self) -> str:
        return self.tokens.refresh

    @property
    def tokens(self) -> Tokens:
        if self._tokens is None:
            self._establish_tokens()

        return self._tokens

    @tokens.setter
    def tokens(self, value: Tokens):
        # Save the tokens to the cache
        self._token_cache.set_cached_tokens(self._host, self._username, value)

        # Assign the value
        self._tokens = value

    def _establish_tokens(self):
        """
        Establishes the tokens on first use, from the token cache if possible,
        otherwise from the server.
        """
        # Try to get the tokens from the cache
        self._tokens = self._token_cache.get_cached_tokens(self._host, self._username)

        # If that fails, get them from the UFDL server
        if self._tokens is None:
            self.tokens = self._jwt_obtain()

    def _refresh_access_token(self) -> Tokens:
        """
        Refreshes the access token.
        """
        # Get the current refresh token
        refresh_token = self.refresh_token

        return Tokens(self._jwt_refresh(refresh_token), refresh_token)

    def _refresh(self) -> Tokens:
        """
        Refreshes the access token with the current refresh token, and failing that,
        grabs a new token pair from the server.

        :return:    The refreshed token pair.
        """
        try:
            return self._refresh_access_token()
        except requests.HTTPError as e:
            # If the error is not because the refresh token is expired, re-raise it
            if e.response.status_code != 401:
                raise

            return self._jwt_obtain()

    def _format_url(self, url: str) -> str:
        """
        Takes the URL for the API end-point and constructs
        the entire URL from it.

        :param url:     The end-point URL relative to the server.
        :return:        The complete URL.
        """
        return f"{self._host}/{url}"

    def post(self, url: str, json: RawJSONObject, *, auth: bool = True) -> requests.Response:
        return self.request(auth)(requests.post, url, json=json)

    def get(self, url: str, json: Optional[RawJSONObject] = None, *, auth: bool = True, **params) -> requests.Response:
        return self.request(auth)(requests.get, url, params=params, json={} if json is None else json)

    def put(self, url: str, json: RawJSONObject, *, auth: bool = True) -> requests.Response:
        return self.request(auth)(requests.put, url, json=json)

    def patch(self, url: str, json: RawJSONObject, *, auth: bool = True) -> requests.Response:
        return self.request(auth)(requests.patch, url, json=json)

    def delete(self, url: str, *, auth: bool = True) -> requests.Response:
        return self.request(auth)(requests.delete, url)

    def upload(self, url: str, filename: str, data: Union[bytes, IO[bytes]], *, auth: bool = True) -> requests.Response:
        # Make sure a filename is set
        if filename == "":
            filename = 'UNKNOWN'

        return self.request(auth)(requests.post, url,
                                  data=data,
                                  headers={
                                      "Content-Disposition": f"attachment; filename={filename}",
                                      "Content-Type": "application/data"
                                  })

    def download(self, url: str, *, auth: bool = True, **params) -> requests.Response:
        return self.request(auth)(requests.get, url, params=params, stream=True)

    def request(self, auth: bool):
        """
        Returns a request method to call, adding authorisation if requested.

        :param auth:    Whether to add authorisation.
        :return:        A request method.
        """
        return self._request_with_auth if auth else self._request_without_auth

    def _request_with_auth(self, method, url: str, **kwargs) -> requests.Response:
        # Format the URL
        url = self._format_url(url)

        try:
            # Set the authentication token in the headers
            self._set_auth_headers(kwargs)

            # Call the method and raise any response errors
            return raise_for_response(method(url, **kwargs))
        except requests.HTTPError as e:
            # If we errored on an expired token, refresh and retry
            if e.response.status_code == requests.codes.unauthorized:
                # Refresh the access token
                self.tokens = self._refresh()

                # Retry the request (same as try block above)
                self._set_auth_headers(kwargs)
                return raise_for_response(method(url, **kwargs))

            # Re-raise any other errors
            else:
                raise

    def _request_without_auth(self, method, url: str, **kwargs) -> requests.Response:
        # Format the URL
        url = self._format_url(url)

        return raise_for_response(method(url, **kwargs))

    def _set_auth_headers(self, kwargs: Dict[str, Any]):
        """
        Sets the authentication headers in the given method keyword arguments.

        :param kwargs:  The keyword arguments.
        """
        # Get the current set of headers from the kwargs, if any
        headers = kwargs.pop("headers", {})

        # Add the authentication headers
        headers.update(self._auth_headers)

        # Put the headers back into the kwargs
        kwargs["headers"] = headers

    def _jwt_obtain(self) -> Tokens:
        """
        Obtains a new pair of JWT tokens for the user from the server.

        :return:    The JWT tokens.
        """
        json_tokens = self.post(JWT_OBTAIN_TOKEN_URL, {
            "username": self.username,
            "password": self.password
        }, auth=False).json()

        return Tokens(json_tokens['access'], json_tokens['refresh'])

    def _jwt_refresh(self, refresh_token: str) -> str:
        """
        Obtains a new access token for the user using the given refresh token.

        :param refresh_token:   The refresh token.
        :return:                The new access token.
        """
        return self.post(JWT_REFRESH_TOKEN_URL, {"refresh": refresh_token}, auth=False).json()['access']

    def _jwt_verify(self, token: str) -> bool:
        """
        Verifies a JWT token.

        :param token:   The token to verify.
        :return:        True if the token is valid, False if not.
        """
        try:
            return self.post(JWT_VERIFY_TOKEN_URL, {"token": token}, auth=False).status_code == 200
        except requests.HTTPError:
            return False
