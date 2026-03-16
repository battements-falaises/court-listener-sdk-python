# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date, datetime
from typing_extensions import Literal

import httpx

from ..types import docket_list_params, docket_retrieve_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncCursorURLPage, AsyncCursorURLPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.docket import Docket

__all__ = ["DocketsResource", "AsyncDocketsResource"]


class DocketsResource(SyncAPIResource):
    """Case-level metadata sitting at the top of the object hierarchy."""

    @cached_property
    def with_raw_response(self) -> DocketsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/battements-falaises/court-listener-sdk-python#accessing-raw-response-data-eg-headers
        """
        return DocketsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DocketsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/battements-falaises/court-listener-sdk-python#with_streaming_response
        """
        return DocketsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        id: int,
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
    ) -> Docket:
        """
        Retrieve a single docket

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
        return self._get(
            f"/dockets/{id}/",
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
                    docket_retrieve_params.DocketRetrieveParams,
                ),
            ),
            cast_to=Docket,
        )

    def list(
        self,
        *,
        id: int | Omit = omit,
        blocked: bool | Omit = omit,
        case_name: str | Omit = omit,
        cause: str | Omit = omit,
        count: Literal["on"] | Omit = omit,
        court: str | Omit = omit,
        query_court_jurisdiction_1: str | Omit = omit,
        query_court_jurisdiction_2: str | Omit = omit,
        cursor: str | Omit = omit,
        date_created: Union[str, datetime] | Omit = omit,
        date_created_gte: Union[str, datetime] | Omit = omit,
        date_created_lte: Union[str, datetime] | Omit = omit,
        date_filed: Union[str, date] | Omit = omit,
        date_filed_gte: Union[str, date] | Omit = omit,
        date_filed_lte: Union[str, date] | Omit = omit,
        date_modified: Union[str, datetime] | Omit = omit,
        date_modified_gte: Union[str, datetime] | Omit = omit,
        date_modified_lte: Union[str, datetime] | Omit = omit,
        date_terminated: Union[str, date] | Omit = omit,
        date_terminated_gte: Union[str, date] | Omit = omit,
        date_terminated_lte: Union[str, date] | Omit = omit,
        docket_number: str | Omit = omit,
        fields: str | Omit = omit,
        format: Literal["json", "xml", "html"] | Omit = omit,
        id_gt: int | Omit = omit,
        id_gte: int | Omit = omit,
        id_lt: int | Omit = omit,
        id_lte: int | Omit = omit,
        id_range: str | Omit = omit,
        nature_of_suit: str | Omit = omit,
        omit: str | Omit = omit,
        order_by: str | Omit = omit,
        page: int | Omit = omit,
        source: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorURLPage[Docket]:
        """Returns a paginated list of dockets.

        Dockets sit at the top of the case law
        hierarchy, linking to clusters of opinions.

        **Note**: The response does not inline docket entries, parties, or attorneys
        (this does not scale). Use the PACER/RECAP APIs for those.

        Args:
          id: Filter by docket ID (exact).

          blocked: Filter for blocked/unblocked dockets.

          case_name: Filter by case name.

          cause: Filter by cause.

          count: Set to `on` to return only the total count of matching items without result
              data. When enabled, pagination parameters are ignored.

          court: Filter by court identifier (e.g. `scotus`). Supports related court filters via
              `court__` prefix.

          query_court_jurisdiction_1: Filter by the court's jurisdiction type (e.g. `F`, `FD`, `S`).

          query_court_jurisdiction_2: Exclude dockets from this jurisdiction type.

          cursor: Cursor token for deep pagination. Returned in the `next` / `previous` fields of
              paginated responses. Available when ordering by `id`, `date_modified`, or
              `date_created`.

          date_created: Filter by exact creation date.

          date_created_gte: Created on or after this date.

          date_created_lte: Created on or before this date.

          date_filed: Filter by filing date.

          date_filed_gte: Filed on or after this date.

          date_filed_lte: Filed on or before this date.

          date_modified: Filter by exact modification date.

          date_modified_gte: Modified on or after this date.

          date_modified_lte: Modified on or before this date.

          date_terminated: Filter by termination date.

          docket_number: Filter by exact docket number (e.g. `23A994`).

          fields: Comma-separated list of fields to include. Supports nested fields via
              double-underscore notation (e.g. `educations__id`).

          format: Response serialization format. JSON is default when no `Accept` header is
              provided.

          id_gt: Docket IDs greater than this value.

          id_gte: Docket IDs greater than or equal to this value.

          id_lt: Docket IDs less than this value.

          id_lte: Docket IDs less than or equal to this value.

          id_range: Docket IDs within an inclusive range (e.g. `500,1000`).

          nature_of_suit: Filter by nature of suit.

          omit: Comma-separated list of fields to exclude. Supports nested fields via
              double-underscore notation.

          order_by: Comma-separated list of fields to order by. Prefix with `-` for descending
              order. Use a secondary field as a tie-breaker for deterministic ordering (e.g.
              `date_filed,id`).

          page: Page number for standard pagination (limited to 100 pages).

          source: Filter by docket source.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/dockets/",
            page=SyncCursorURLPage[Docket],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "blocked": blocked,
                        "case_name": case_name,
                        "cause": cause,
                        "count": count,
                        "court": court,
                        "query_court_jurisdiction_1": query_court_jurisdiction_1,
                        "query_court_jurisdiction_2": query_court_jurisdiction_2,
                        "cursor": cursor,
                        "date_created": date_created,
                        "date_created_gte": date_created_gte,
                        "date_created_lte": date_created_lte,
                        "date_filed": date_filed,
                        "date_filed_gte": date_filed_gte,
                        "date_filed_lte": date_filed_lte,
                        "date_modified": date_modified,
                        "date_modified_gte": date_modified_gte,
                        "date_modified_lte": date_modified_lte,
                        "date_terminated": date_terminated,
                        "date_terminated_gte": date_terminated_gte,
                        "date_terminated_lte": date_terminated_lte,
                        "docket_number": docket_number,
                        "fields": fields,
                        "format": format,
                        "id_gt": id_gt,
                        "id_gte": id_gte,
                        "id_lt": id_lt,
                        "id_lte": id_lte,
                        "id_range": id_range,
                        "nature_of_suit": nature_of_suit,
                        "omit": omit,
                        "order_by": order_by,
                        "page": page,
                        "source": source,
                    },
                    docket_list_params.DocketListParams,
                ),
            ),
            model=Docket,
        )


class AsyncDocketsResource(AsyncAPIResource):
    """Case-level metadata sitting at the top of the object hierarchy."""

    @cached_property
    def with_raw_response(self) -> AsyncDocketsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/battements-falaises/court-listener-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDocketsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDocketsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/battements-falaises/court-listener-sdk-python#with_streaming_response
        """
        return AsyncDocketsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        id: int,
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
    ) -> Docket:
        """
        Retrieve a single docket

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
        return await self._get(
            f"/dockets/{id}/",
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
                    docket_retrieve_params.DocketRetrieveParams,
                ),
            ),
            cast_to=Docket,
        )

    def list(
        self,
        *,
        id: int | Omit = omit,
        blocked: bool | Omit = omit,
        case_name: str | Omit = omit,
        cause: str | Omit = omit,
        count: Literal["on"] | Omit = omit,
        court: str | Omit = omit,
        query_court_jurisdiction_1: str | Omit = omit,
        query_court_jurisdiction_2: str | Omit = omit,
        cursor: str | Omit = omit,
        date_created: Union[str, datetime] | Omit = omit,
        date_created_gte: Union[str, datetime] | Omit = omit,
        date_created_lte: Union[str, datetime] | Omit = omit,
        date_filed: Union[str, date] | Omit = omit,
        date_filed_gte: Union[str, date] | Omit = omit,
        date_filed_lte: Union[str, date] | Omit = omit,
        date_modified: Union[str, datetime] | Omit = omit,
        date_modified_gte: Union[str, datetime] | Omit = omit,
        date_modified_lte: Union[str, datetime] | Omit = omit,
        date_terminated: Union[str, date] | Omit = omit,
        date_terminated_gte: Union[str, date] | Omit = omit,
        date_terminated_lte: Union[str, date] | Omit = omit,
        docket_number: str | Omit = omit,
        fields: str | Omit = omit,
        format: Literal["json", "xml", "html"] | Omit = omit,
        id_gt: int | Omit = omit,
        id_gte: int | Omit = omit,
        id_lt: int | Omit = omit,
        id_lte: int | Omit = omit,
        id_range: str | Omit = omit,
        nature_of_suit: str | Omit = omit,
        omit: str | Omit = omit,
        order_by: str | Omit = omit,
        page: int | Omit = omit,
        source: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Docket, AsyncCursorURLPage[Docket]]:
        """Returns a paginated list of dockets.

        Dockets sit at the top of the case law
        hierarchy, linking to clusters of opinions.

        **Note**: The response does not inline docket entries, parties, or attorneys
        (this does not scale). Use the PACER/RECAP APIs for those.

        Args:
          id: Filter by docket ID (exact).

          blocked: Filter for blocked/unblocked dockets.

          case_name: Filter by case name.

          cause: Filter by cause.

          count: Set to `on` to return only the total count of matching items without result
              data. When enabled, pagination parameters are ignored.

          court: Filter by court identifier (e.g. `scotus`). Supports related court filters via
              `court__` prefix.

          query_court_jurisdiction_1: Filter by the court's jurisdiction type (e.g. `F`, `FD`, `S`).

          query_court_jurisdiction_2: Exclude dockets from this jurisdiction type.

          cursor: Cursor token for deep pagination. Returned in the `next` / `previous` fields of
              paginated responses. Available when ordering by `id`, `date_modified`, or
              `date_created`.

          date_created: Filter by exact creation date.

          date_created_gte: Created on or after this date.

          date_created_lte: Created on or before this date.

          date_filed: Filter by filing date.

          date_filed_gte: Filed on or after this date.

          date_filed_lte: Filed on or before this date.

          date_modified: Filter by exact modification date.

          date_modified_gte: Modified on or after this date.

          date_modified_lte: Modified on or before this date.

          date_terminated: Filter by termination date.

          docket_number: Filter by exact docket number (e.g. `23A994`).

          fields: Comma-separated list of fields to include. Supports nested fields via
              double-underscore notation (e.g. `educations__id`).

          format: Response serialization format. JSON is default when no `Accept` header is
              provided.

          id_gt: Docket IDs greater than this value.

          id_gte: Docket IDs greater than or equal to this value.

          id_lt: Docket IDs less than this value.

          id_lte: Docket IDs less than or equal to this value.

          id_range: Docket IDs within an inclusive range (e.g. `500,1000`).

          nature_of_suit: Filter by nature of suit.

          omit: Comma-separated list of fields to exclude. Supports nested fields via
              double-underscore notation.

          order_by: Comma-separated list of fields to order by. Prefix with `-` for descending
              order. Use a secondary field as a tie-breaker for deterministic ordering (e.g.
              `date_filed,id`).

          page: Page number for standard pagination (limited to 100 pages).

          source: Filter by docket source.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/dockets/",
            page=AsyncCursorURLPage[Docket],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "blocked": blocked,
                        "case_name": case_name,
                        "cause": cause,
                        "count": count,
                        "court": court,
                        "query_court_jurisdiction_1": query_court_jurisdiction_1,
                        "query_court_jurisdiction_2": query_court_jurisdiction_2,
                        "cursor": cursor,
                        "date_created": date_created,
                        "date_created_gte": date_created_gte,
                        "date_created_lte": date_created_lte,
                        "date_filed": date_filed,
                        "date_filed_gte": date_filed_gte,
                        "date_filed_lte": date_filed_lte,
                        "date_modified": date_modified,
                        "date_modified_gte": date_modified_gte,
                        "date_modified_lte": date_modified_lte,
                        "date_terminated": date_terminated,
                        "date_terminated_gte": date_terminated_gte,
                        "date_terminated_lte": date_terminated_lte,
                        "docket_number": docket_number,
                        "fields": fields,
                        "format": format,
                        "id_gt": id_gt,
                        "id_gte": id_gte,
                        "id_lt": id_lt,
                        "id_lte": id_lte,
                        "id_range": id_range,
                        "nature_of_suit": nature_of_suit,
                        "omit": omit,
                        "order_by": order_by,
                        "page": page,
                        "source": source,
                    },
                    docket_list_params.DocketListParams,
                ),
            ),
            model=Docket,
        )


class DocketsResourceWithRawResponse:
    def __init__(self, dockets: DocketsResource) -> None:
        self._dockets = dockets

        self.retrieve = to_raw_response_wrapper(
            dockets.retrieve,
        )
        self.list = to_raw_response_wrapper(
            dockets.list,
        )


class AsyncDocketsResourceWithRawResponse:
    def __init__(self, dockets: AsyncDocketsResource) -> None:
        self._dockets = dockets

        self.retrieve = async_to_raw_response_wrapper(
            dockets.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            dockets.list,
        )


class DocketsResourceWithStreamingResponse:
    def __init__(self, dockets: DocketsResource) -> None:
        self._dockets = dockets

        self.retrieve = to_streamed_response_wrapper(
            dockets.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            dockets.list,
        )


class AsyncDocketsResourceWithStreamingResponse:
    def __init__(self, dockets: AsyncDocketsResource) -> None:
        self._dockets = dockets

        self.retrieve = async_to_streamed_response_wrapper(
            dockets.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            dockets.list,
        )
