# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import court_list_params, court_retrieve_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncCursorURLPage, AsyncCursorURLPage
from ..types.court import Court
from .._base_client import AsyncPaginator, make_request_options

__all__ = ["CourtsResource", "AsyncCourtsResource"]


class CourtsResource(SyncAPIResource):
    """Metadata about courts in the CourtListener database."""

    @cached_property
    def with_raw_response(self) -> CourtsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/battements-falaises/court-listener-sdk-python#accessing-raw-response-data-eg-headers
        """
        return CourtsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CourtsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/battements-falaises/court-listener-sdk-python#with_streaming_response
        """
        return CourtsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        id: str,
        *,
        fields: str | Omit = omit,
        format: Literal["json", "xml", "html"] | Omit = omit,
        omit: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Court:
        """
        Retrieve a single court

        Args:
          fields: Comma-separated list of fields to include. Supports nested fields via
              double-underscore notation (e.g. `educations__id`).

          format: Response serialization format. JSON is default when no `Accept` header is
              provided.

          omit: Comma-separated list of fields to exclude. Supports nested fields via
              double-underscore notation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/courts/{id}/", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "fields": fields,
                        "format": format,
                        "omit": omit,
                    },
                    court_retrieve_params.CourtRetrieveParams,
                ),
            ),
            cast_to=Court,
        )

    def list(
        self,
        *,
        id: str | Omit = omit,
        count: Literal["on"] | Omit = omit,
        cursor: str | Omit = omit,
        date_modified: Union[str, datetime] | Omit = omit,
        date_modified_gte: Union[str, datetime] | Omit = omit,
        date_modified_lte: Union[str, datetime] | Omit = omit,
        fields: str | Omit = omit,
        format: Literal["json", "xml", "html"] | Omit = omit,
        full_name: str | Omit = omit,
        full_name_startswith: str | Omit = omit,
        id_in: str | Omit = omit,
        jurisdiction: str | Omit = omit,
        omit: str | Omit = omit,
        order_by: str | Omit = omit,
        page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorURLPage[Court]:
        """Returns a paginated list of courts.

        Results can generally be cached as court
        data changes infrequently.

        Args:
          id: Filter by court identifier (e.g. `scotus`, `ca9`, `dcd`).

          count: Set to `on` to return only the total count of matching items without result
              data. When enabled, pagination parameters are ignored.

          cursor: Cursor token for deep pagination. Returned in the `next` / `previous` fields of
              paginated responses. Available when ordering by `id`, `date_modified`, or
              `date_created`.

          date_modified: Filter by exact date modified (ISO-8601).

          date_modified_gte: Filter courts modified on or after this date.

          date_modified_lte: Filter courts modified on or before this date.

          fields: Comma-separated list of fields to include. Supports nested fields via
              double-underscore notation (e.g. `educations__id`).

          format: Response serialization format. JSON is default when no `Accept` header is
              provided.

          full_name: Filter by the full name of the court.

          full_name_startswith: Filter courts whose full name starts with the given value.

          id_in: Filter by multiple court identifiers (comma-separated).

          jurisdiction: Filter by jurisdiction type. Common values: `F` (Federal Appellate), `FD`
              (Federal District), `FB` (Federal Bankruptcy), `FBP` (Federal Bankruptcy Panel),
              `FS` (Federal Special), `S` (State Supreme), `SA` (State Appellate), `ST` (State
              Trial), `SS` (State Special), `SAG` (State Attorney General), `T` (Tribal), `I`
              (International), `C` (Committee), `TES` (Testing).

          omit: Comma-separated list of fields to exclude. Supports nested fields via
              double-underscore notation.

          order_by: Comma-separated list of fields to order by. Prefix with `-` for descending
              order. Use a secondary field as a tie-breaker for deterministic ordering (e.g.
              `date_filed,id`).

          page: Page number for standard pagination (limited to 100 pages).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/courts/",
            page=SyncCursorURLPage[Court],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "count": count,
                        "cursor": cursor,
                        "date_modified": date_modified,
                        "date_modified_gte": date_modified_gte,
                        "date_modified_lte": date_modified_lte,
                        "fields": fields,
                        "format": format,
                        "full_name": full_name,
                        "full_name_startswith": full_name_startswith,
                        "id_in": id_in,
                        "jurisdiction": jurisdiction,
                        "omit": omit,
                        "order_by": order_by,
                        "page": page,
                    },
                    court_list_params.CourtListParams,
                ),
            ),
            model=Court,
        )


class AsyncCourtsResource(AsyncAPIResource):
    """Metadata about courts in the CourtListener database."""

    @cached_property
    def with_raw_response(self) -> AsyncCourtsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/battements-falaises/court-listener-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCourtsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCourtsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/battements-falaises/court-listener-sdk-python#with_streaming_response
        """
        return AsyncCourtsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        id: str,
        *,
        fields: str | Omit = omit,
        format: Literal["json", "xml", "html"] | Omit = omit,
        omit: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Court:
        """
        Retrieve a single court

        Args:
          fields: Comma-separated list of fields to include. Supports nested fields via
              double-underscore notation (e.g. `educations__id`).

          format: Response serialization format. JSON is default when no `Accept` header is
              provided.

          omit: Comma-separated list of fields to exclude. Supports nested fields via
              double-underscore notation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/courts/{id}/", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "fields": fields,
                        "format": format,
                        "omit": omit,
                    },
                    court_retrieve_params.CourtRetrieveParams,
                ),
            ),
            cast_to=Court,
        )

    def list(
        self,
        *,
        id: str | Omit = omit,
        count: Literal["on"] | Omit = omit,
        cursor: str | Omit = omit,
        date_modified: Union[str, datetime] | Omit = omit,
        date_modified_gte: Union[str, datetime] | Omit = omit,
        date_modified_lte: Union[str, datetime] | Omit = omit,
        fields: str | Omit = omit,
        format: Literal["json", "xml", "html"] | Omit = omit,
        full_name: str | Omit = omit,
        full_name_startswith: str | Omit = omit,
        id_in: str | Omit = omit,
        jurisdiction: str | Omit = omit,
        omit: str | Omit = omit,
        order_by: str | Omit = omit,
        page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Court, AsyncCursorURLPage[Court]]:
        """Returns a paginated list of courts.

        Results can generally be cached as court
        data changes infrequently.

        Args:
          id: Filter by court identifier (e.g. `scotus`, `ca9`, `dcd`).

          count: Set to `on` to return only the total count of matching items without result
              data. When enabled, pagination parameters are ignored.

          cursor: Cursor token for deep pagination. Returned in the `next` / `previous` fields of
              paginated responses. Available when ordering by `id`, `date_modified`, or
              `date_created`.

          date_modified: Filter by exact date modified (ISO-8601).

          date_modified_gte: Filter courts modified on or after this date.

          date_modified_lte: Filter courts modified on or before this date.

          fields: Comma-separated list of fields to include. Supports nested fields via
              double-underscore notation (e.g. `educations__id`).

          format: Response serialization format. JSON is default when no `Accept` header is
              provided.

          full_name: Filter by the full name of the court.

          full_name_startswith: Filter courts whose full name starts with the given value.

          id_in: Filter by multiple court identifiers (comma-separated).

          jurisdiction: Filter by jurisdiction type. Common values: `F` (Federal Appellate), `FD`
              (Federal District), `FB` (Federal Bankruptcy), `FBP` (Federal Bankruptcy Panel),
              `FS` (Federal Special), `S` (State Supreme), `SA` (State Appellate), `ST` (State
              Trial), `SS` (State Special), `SAG` (State Attorney General), `T` (Tribal), `I`
              (International), `C` (Committee), `TES` (Testing).

          omit: Comma-separated list of fields to exclude. Supports nested fields via
              double-underscore notation.

          order_by: Comma-separated list of fields to order by. Prefix with `-` for descending
              order. Use a secondary field as a tie-breaker for deterministic ordering (e.g.
              `date_filed,id`).

          page: Page number for standard pagination (limited to 100 pages).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/courts/",
            page=AsyncCursorURLPage[Court],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "count": count,
                        "cursor": cursor,
                        "date_modified": date_modified,
                        "date_modified_gte": date_modified_gte,
                        "date_modified_lte": date_modified_lte,
                        "fields": fields,
                        "format": format,
                        "full_name": full_name,
                        "full_name_startswith": full_name_startswith,
                        "id_in": id_in,
                        "jurisdiction": jurisdiction,
                        "omit": omit,
                        "order_by": order_by,
                        "page": page,
                    },
                    court_list_params.CourtListParams,
                ),
            ),
            model=Court,
        )


class CourtsResourceWithRawResponse:
    def __init__(self, courts: CourtsResource) -> None:
        self._courts = courts

        self.retrieve = to_raw_response_wrapper(
            courts.retrieve,
        )
        self.list = to_raw_response_wrapper(
            courts.list,
        )


class AsyncCourtsResourceWithRawResponse:
    def __init__(self, courts: AsyncCourtsResource) -> None:
        self._courts = courts

        self.retrieve = async_to_raw_response_wrapper(
            courts.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            courts.list,
        )


class CourtsResourceWithStreamingResponse:
    def __init__(self, courts: CourtsResource) -> None:
        self._courts = courts

        self.retrieve = to_streamed_response_wrapper(
            courts.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            courts.list,
        )


class AsyncCourtsResourceWithStreamingResponse:
    def __init__(self, courts: AsyncCourtsResource) -> None:
        self._courts = courts

        self.retrieve = async_to_streamed_response_wrapper(
            courts.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            courts.list,
        )
