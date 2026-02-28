# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
import base64
from typing import TYPE_CHECKING, Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Headers,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import courts, dockets, clusters, opinions
    from .resources.courts import CourtsResource, AsyncCourtsResource
    from .resources.dockets import DocketsResource, AsyncDocketsResource
    from .resources.clusters import ClustersResource, AsyncClustersResource
    from .resources.opinions import OpinionsResource, AsyncOpinionsResource

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "CourtListener",
    "AsyncCourtListener",
    "Client",
    "AsyncClient",
]


class CourtListener(SyncAPIClient):
    # client options
    api_key: str | None
    username: str | None
    password: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        username: str | None = None,
        password: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous CourtListener client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `api_key` from `COURT_LISTENER_API_KEY`
        - `username` from `COURT_LISTENER_USERNAME`
        - `password` from `COURT_LISTENER_PASSWORD`
        """
        if api_key is None:
            api_key = os.environ.get("COURT_LISTENER_API_KEY")
        self.api_key = api_key

        if username is None:
            username = os.environ.get("COURT_LISTENER_USERNAME")
        self.username = username

        if password is None:
            password = os.environ.get("COURT_LISTENER_PASSWORD")
        self.password = password

        if base_url is None:
            base_url = os.environ.get("COURT_LISTENER_BASE_URL")
        if base_url is None:
            base_url = f"https://www.courtlistener.com/api/rest/v4"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def courts(self) -> CourtsResource:
        """Metadata about courts in the CourtListener database."""
        from .resources.courts import CourtsResource

        return CourtsResource(self)

    @cached_property
    def dockets(self) -> DocketsResource:
        """Case-level metadata sitting at the top of the object hierarchy."""
        from .resources.dockets import DocketsResource

        return DocketsResource(self)

    @cached_property
    def clusters(self) -> ClustersResource:
        """Opinion clusters grouping related decisions from a single hearing."""
        from .resources.clusters import ClustersResource

        return ClustersResource(self)

    @cached_property
    def opinions(self) -> OpinionsResource:
        """Individual judicial opinions with full text and metadata."""
        from .resources.opinions import OpinionsResource

        return OpinionsResource(self)

    @cached_property
    def with_raw_response(self) -> CourtListenerWithRawResponse:
        return CourtListenerWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CourtListenerWithStreamedResponse:
        return CourtListenerWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        return {**self._token_auth, **self._basic_auth}

    @property
    def _token_auth(self) -> dict[str, str]:
        api_key = self.api_key
        if api_key is None:
            return {}
        return {"Authorization": f"Token {api_key}"}

    @property
    def _basic_auth(self) -> dict[str, str]:
        if self.username is None:
            return {}
        if self.password is None:
            return {}
        credentials = f"{self.username}:{self.password}".encode("ascii")
        header = f"Basic {base64.b64encode(credentials).decode('ascii')}"
        return {"Authorization": header}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    @override
    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if headers.get("Authorization") or isinstance(custom_headers.get("Authorization"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected either api_key, username or password to be set. Or for one of the `Authorization` or `Authorization` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        api_key: str | None = None,
        username: str | None = None,
        password: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            username=username or self.username,
            password=password or self.password,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncCourtListener(AsyncAPIClient):
    # client options
    api_key: str | None
    username: str | None
    password: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        username: str | None = None,
        password: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncCourtListener client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `api_key` from `COURT_LISTENER_API_KEY`
        - `username` from `COURT_LISTENER_USERNAME`
        - `password` from `COURT_LISTENER_PASSWORD`
        """
        if api_key is None:
            api_key = os.environ.get("COURT_LISTENER_API_KEY")
        self.api_key = api_key

        if username is None:
            username = os.environ.get("COURT_LISTENER_USERNAME")
        self.username = username

        if password is None:
            password = os.environ.get("COURT_LISTENER_PASSWORD")
        self.password = password

        if base_url is None:
            base_url = os.environ.get("COURT_LISTENER_BASE_URL")
        if base_url is None:
            base_url = f"https://www.courtlistener.com/api/rest/v4"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def courts(self) -> AsyncCourtsResource:
        """Metadata about courts in the CourtListener database."""
        from .resources.courts import AsyncCourtsResource

        return AsyncCourtsResource(self)

    @cached_property
    def dockets(self) -> AsyncDocketsResource:
        """Case-level metadata sitting at the top of the object hierarchy."""
        from .resources.dockets import AsyncDocketsResource

        return AsyncDocketsResource(self)

    @cached_property
    def clusters(self) -> AsyncClustersResource:
        """Opinion clusters grouping related decisions from a single hearing."""
        from .resources.clusters import AsyncClustersResource

        return AsyncClustersResource(self)

    @cached_property
    def opinions(self) -> AsyncOpinionsResource:
        """Individual judicial opinions with full text and metadata."""
        from .resources.opinions import AsyncOpinionsResource

        return AsyncOpinionsResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncCourtListenerWithRawResponse:
        return AsyncCourtListenerWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCourtListenerWithStreamedResponse:
        return AsyncCourtListenerWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        return {**self._token_auth, **self._basic_auth}

    @property
    def _token_auth(self) -> dict[str, str]:
        api_key = self.api_key
        if api_key is None:
            return {}
        return {"Authorization": f"Token {api_key}"}

    @property
    def _basic_auth(self) -> dict[str, str]:
        if self.username is None:
            return {}
        if self.password is None:
            return {}
        credentials = f"{self.username}:{self.password}".encode("ascii")
        header = f"Basic {base64.b64encode(credentials).decode('ascii')}"
        return {"Authorization": header}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    @override
    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if headers.get("Authorization") or isinstance(custom_headers.get("Authorization"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected either api_key, username or password to be set. Or for one of the `Authorization` or `Authorization` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        api_key: str | None = None,
        username: str | None = None,
        password: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            username=username or self.username,
            password=password or self.password,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class CourtListenerWithRawResponse:
    _client: CourtListener

    def __init__(self, client: CourtListener) -> None:
        self._client = client

    @cached_property
    def courts(self) -> courts.CourtsResourceWithRawResponse:
        """Metadata about courts in the CourtListener database."""
        from .resources.courts import CourtsResourceWithRawResponse

        return CourtsResourceWithRawResponse(self._client.courts)

    @cached_property
    def dockets(self) -> dockets.DocketsResourceWithRawResponse:
        """Case-level metadata sitting at the top of the object hierarchy."""
        from .resources.dockets import DocketsResourceWithRawResponse

        return DocketsResourceWithRawResponse(self._client.dockets)

    @cached_property
    def clusters(self) -> clusters.ClustersResourceWithRawResponse:
        """Opinion clusters grouping related decisions from a single hearing."""
        from .resources.clusters import ClustersResourceWithRawResponse

        return ClustersResourceWithRawResponse(self._client.clusters)

    @cached_property
    def opinions(self) -> opinions.OpinionsResourceWithRawResponse:
        """Individual judicial opinions with full text and metadata."""
        from .resources.opinions import OpinionsResourceWithRawResponse

        return OpinionsResourceWithRawResponse(self._client.opinions)


class AsyncCourtListenerWithRawResponse:
    _client: AsyncCourtListener

    def __init__(self, client: AsyncCourtListener) -> None:
        self._client = client

    @cached_property
    def courts(self) -> courts.AsyncCourtsResourceWithRawResponse:
        """Metadata about courts in the CourtListener database."""
        from .resources.courts import AsyncCourtsResourceWithRawResponse

        return AsyncCourtsResourceWithRawResponse(self._client.courts)

    @cached_property
    def dockets(self) -> dockets.AsyncDocketsResourceWithRawResponse:
        """Case-level metadata sitting at the top of the object hierarchy."""
        from .resources.dockets import AsyncDocketsResourceWithRawResponse

        return AsyncDocketsResourceWithRawResponse(self._client.dockets)

    @cached_property
    def clusters(self) -> clusters.AsyncClustersResourceWithRawResponse:
        """Opinion clusters grouping related decisions from a single hearing."""
        from .resources.clusters import AsyncClustersResourceWithRawResponse

        return AsyncClustersResourceWithRawResponse(self._client.clusters)

    @cached_property
    def opinions(self) -> opinions.AsyncOpinionsResourceWithRawResponse:
        """Individual judicial opinions with full text and metadata."""
        from .resources.opinions import AsyncOpinionsResourceWithRawResponse

        return AsyncOpinionsResourceWithRawResponse(self._client.opinions)


class CourtListenerWithStreamedResponse:
    _client: CourtListener

    def __init__(self, client: CourtListener) -> None:
        self._client = client

    @cached_property
    def courts(self) -> courts.CourtsResourceWithStreamingResponse:
        """Metadata about courts in the CourtListener database."""
        from .resources.courts import CourtsResourceWithStreamingResponse

        return CourtsResourceWithStreamingResponse(self._client.courts)

    @cached_property
    def dockets(self) -> dockets.DocketsResourceWithStreamingResponse:
        """Case-level metadata sitting at the top of the object hierarchy."""
        from .resources.dockets import DocketsResourceWithStreamingResponse

        return DocketsResourceWithStreamingResponse(self._client.dockets)

    @cached_property
    def clusters(self) -> clusters.ClustersResourceWithStreamingResponse:
        """Opinion clusters grouping related decisions from a single hearing."""
        from .resources.clusters import ClustersResourceWithStreamingResponse

        return ClustersResourceWithStreamingResponse(self._client.clusters)

    @cached_property
    def opinions(self) -> opinions.OpinionsResourceWithStreamingResponse:
        """Individual judicial opinions with full text and metadata."""
        from .resources.opinions import OpinionsResourceWithStreamingResponse

        return OpinionsResourceWithStreamingResponse(self._client.opinions)


class AsyncCourtListenerWithStreamedResponse:
    _client: AsyncCourtListener

    def __init__(self, client: AsyncCourtListener) -> None:
        self._client = client

    @cached_property
    def courts(self) -> courts.AsyncCourtsResourceWithStreamingResponse:
        """Metadata about courts in the CourtListener database."""
        from .resources.courts import AsyncCourtsResourceWithStreamingResponse

        return AsyncCourtsResourceWithStreamingResponse(self._client.courts)

    @cached_property
    def dockets(self) -> dockets.AsyncDocketsResourceWithStreamingResponse:
        """Case-level metadata sitting at the top of the object hierarchy."""
        from .resources.dockets import AsyncDocketsResourceWithStreamingResponse

        return AsyncDocketsResourceWithStreamingResponse(self._client.dockets)

    @cached_property
    def clusters(self) -> clusters.AsyncClustersResourceWithStreamingResponse:
        """Opinion clusters grouping related decisions from a single hearing."""
        from .resources.clusters import AsyncClustersResourceWithStreamingResponse

        return AsyncClustersResourceWithStreamingResponse(self._client.clusters)

    @cached_property
    def opinions(self) -> opinions.AsyncOpinionsResourceWithStreamingResponse:
        """Individual judicial opinions with full text and metadata."""
        from .resources.opinions import AsyncOpinionsResourceWithStreamingResponse

        return AsyncOpinionsResourceWithStreamingResponse(self._client.opinions)


Client = CourtListener

AsyncClient = AsyncCourtListener
