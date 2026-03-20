# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import opinion_list_params, opinion_retrieve_params
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
from .._base_client import AsyncPaginator, make_request_options
from ..types.opinion import Opinion

__all__ = ["OpinionsResource", "AsyncOpinionsResource"]


class OpinionsResource(SyncAPIResource):
    """Individual judicial opinions with full text and metadata."""

    @cached_property
    def with_raw_response(self) -> OpinionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/battements-falaises/court-listener-sdk-python#accessing-raw-response-data-eg-headers
        """
        return OpinionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OpinionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/battements-falaises/court-listener-sdk-python#with_streaming_response
        """
        return OpinionsResourceWithStreamingResponse(self)

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
    ) -> Opinion:
        """Look up an opinion by its ID.

        Note that opinion IDs do **not** reliably match
        cluster IDs. If you have a CourtListener case URL, use the cluster API to look
        it up.

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
            path_template("/opinions/{id}/", id=id),
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
                    opinion_retrieve_params.OpinionRetrieveParams,
                ),
            ),
            cast_to=Opinion,
        )

    def list(
        self,
        *,
        id: int | Omit = omit,
        cited_opinion: int | Omit = omit,
        cluster: int | Omit = omit,
        cluster_docket_court: str | Omit = omit,
        cluster_docket_docket_number: str | Omit = omit,
        count: Literal["on"] | Omit = omit,
        cursor: str | Omit = omit,
        date_created: Union[str, datetime] | Omit = omit,
        date_created_gte: Union[str, datetime] | Omit = omit,
        date_created_lte: Union[str, datetime] | Omit = omit,
        date_modified: Union[str, datetime] | Omit = omit,
        date_modified_gte: Union[str, datetime] | Omit = omit,
        date_modified_lte: Union[str, datetime] | Omit = omit,
        fields: str | Omit = omit,
        format: Literal["json", "xml", "html"] | Omit = omit,
        id_gt: int | Omit = omit,
        id_gte: int | Omit = omit,
        id_lt: int | Omit = omit,
        id_lte: int | Omit = omit,
        id_range: str | Omit = omit,
        omit: str | Omit = omit,
        order_by: str | Omit = omit,
        page: int | Omit = omit,
        type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorURLPage[Opinion]:
        """Returns a paginated list of opinions.

        Each opinion contains the text of a
        judicial decision and metadata about the authoring judge.

        **Tip**: Prefer the `html_with_citations` field for opinion text — it contains
        the raw text with identified and linked citations, and is the field used on the
        CourtListener website.

        Use `fields` / `omit` parameters to exclude large text fields you don't need.

        Args:
          id: Filter by opinion ID.

          cited_opinion: Filter opinions that cite this opinion ID.

          cluster: Filter by parent cluster ID.

          cluster_docket_court: Filter by court via the cluster's docket (e.g. `scotus`).

          cluster_docket_docket_number: Filter by docket number via the cluster's docket.

          count: Set to `on` to return only the total count of matching items without result
              data. When enabled, pagination parameters are ignored.

          cursor: Cursor token for deep pagination. Returned in the `next` / `previous` fields of
              paginated responses. Available when ordering by `id`, `date_modified`, or
              `date_created`.

          fields: Comma-separated list of fields to include. Supports nested fields via
              double-underscore notation (e.g. `educations__id`).

          format: Response serialization format. JSON is default when no `Accept` header is
              provided.

          omit: Comma-separated list of fields to exclude. Supports nested fields via
              double-underscore notation.

          order_by: Comma-separated list of fields to order by. Prefix with `-` for descending
              order. Use a secondary field as a tie-breaker for deterministic ordering (e.g.
              `date_filed,id`).

          page: Page number for standard pagination (limited to 100 pages).

          type: Filter by opinion type. Values are prefixed with numbers for sort order. Common
              types include combined opinion, lead opinion, concurrence, dissent, etc.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/opinions/",
            page=SyncCursorURLPage[Opinion],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "cited_opinion": cited_opinion,
                        "cluster": cluster,
                        "cluster_docket_court": cluster_docket_court,
                        "cluster_docket_docket_number": cluster_docket_docket_number,
                        "count": count,
                        "cursor": cursor,
                        "date_created": date_created,
                        "date_created_gte": date_created_gte,
                        "date_created_lte": date_created_lte,
                        "date_modified": date_modified,
                        "date_modified_gte": date_modified_gte,
                        "date_modified_lte": date_modified_lte,
                        "fields": fields,
                        "format": format,
                        "id_gt": id_gt,
                        "id_gte": id_gte,
                        "id_lt": id_lt,
                        "id_lte": id_lte,
                        "id_range": id_range,
                        "omit": omit,
                        "order_by": order_by,
                        "page": page,
                        "type": type,
                    },
                    opinion_list_params.OpinionListParams,
                ),
            ),
            model=Opinion,
        )


class AsyncOpinionsResource(AsyncAPIResource):
    """Individual judicial opinions with full text and metadata."""

    @cached_property
    def with_raw_response(self) -> AsyncOpinionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/battements-falaises/court-listener-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOpinionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOpinionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/battements-falaises/court-listener-sdk-python#with_streaming_response
        """
        return AsyncOpinionsResourceWithStreamingResponse(self)

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
    ) -> Opinion:
        """Look up an opinion by its ID.

        Note that opinion IDs do **not** reliably match
        cluster IDs. If you have a CourtListener case URL, use the cluster API to look
        it up.

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
            path_template("/opinions/{id}/", id=id),
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
                    opinion_retrieve_params.OpinionRetrieveParams,
                ),
            ),
            cast_to=Opinion,
        )

    def list(
        self,
        *,
        id: int | Omit = omit,
        cited_opinion: int | Omit = omit,
        cluster: int | Omit = omit,
        cluster_docket_court: str | Omit = omit,
        cluster_docket_docket_number: str | Omit = omit,
        count: Literal["on"] | Omit = omit,
        cursor: str | Omit = omit,
        date_created: Union[str, datetime] | Omit = omit,
        date_created_gte: Union[str, datetime] | Omit = omit,
        date_created_lte: Union[str, datetime] | Omit = omit,
        date_modified: Union[str, datetime] | Omit = omit,
        date_modified_gte: Union[str, datetime] | Omit = omit,
        date_modified_lte: Union[str, datetime] | Omit = omit,
        fields: str | Omit = omit,
        format: Literal["json", "xml", "html"] | Omit = omit,
        id_gt: int | Omit = omit,
        id_gte: int | Omit = omit,
        id_lt: int | Omit = omit,
        id_lte: int | Omit = omit,
        id_range: str | Omit = omit,
        omit: str | Omit = omit,
        order_by: str | Omit = omit,
        page: int | Omit = omit,
        type: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Opinion, AsyncCursorURLPage[Opinion]]:
        """Returns a paginated list of opinions.

        Each opinion contains the text of a
        judicial decision and metadata about the authoring judge.

        **Tip**: Prefer the `html_with_citations` field for opinion text — it contains
        the raw text with identified and linked citations, and is the field used on the
        CourtListener website.

        Use `fields` / `omit` parameters to exclude large text fields you don't need.

        Args:
          id: Filter by opinion ID.

          cited_opinion: Filter opinions that cite this opinion ID.

          cluster: Filter by parent cluster ID.

          cluster_docket_court: Filter by court via the cluster's docket (e.g. `scotus`).

          cluster_docket_docket_number: Filter by docket number via the cluster's docket.

          count: Set to `on` to return only the total count of matching items without result
              data. When enabled, pagination parameters are ignored.

          cursor: Cursor token for deep pagination. Returned in the `next` / `previous` fields of
              paginated responses. Available when ordering by `id`, `date_modified`, or
              `date_created`.

          fields: Comma-separated list of fields to include. Supports nested fields via
              double-underscore notation (e.g. `educations__id`).

          format: Response serialization format. JSON is default when no `Accept` header is
              provided.

          omit: Comma-separated list of fields to exclude. Supports nested fields via
              double-underscore notation.

          order_by: Comma-separated list of fields to order by. Prefix with `-` for descending
              order. Use a secondary field as a tie-breaker for deterministic ordering (e.g.
              `date_filed,id`).

          page: Page number for standard pagination (limited to 100 pages).

          type: Filter by opinion type. Values are prefixed with numbers for sort order. Common
              types include combined opinion, lead opinion, concurrence, dissent, etc.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/opinions/",
            page=AsyncCursorURLPage[Opinion],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "cited_opinion": cited_opinion,
                        "cluster": cluster,
                        "cluster_docket_court": cluster_docket_court,
                        "cluster_docket_docket_number": cluster_docket_docket_number,
                        "count": count,
                        "cursor": cursor,
                        "date_created": date_created,
                        "date_created_gte": date_created_gte,
                        "date_created_lte": date_created_lte,
                        "date_modified": date_modified,
                        "date_modified_gte": date_modified_gte,
                        "date_modified_lte": date_modified_lte,
                        "fields": fields,
                        "format": format,
                        "id_gt": id_gt,
                        "id_gte": id_gte,
                        "id_lt": id_lt,
                        "id_lte": id_lte,
                        "id_range": id_range,
                        "omit": omit,
                        "order_by": order_by,
                        "page": page,
                        "type": type,
                    },
                    opinion_list_params.OpinionListParams,
                ),
            ),
            model=Opinion,
        )


class OpinionsResourceWithRawResponse:
    def __init__(self, opinions: OpinionsResource) -> None:
        self._opinions = opinions

        self.retrieve = to_raw_response_wrapper(
            opinions.retrieve,
        )
        self.list = to_raw_response_wrapper(
            opinions.list,
        )


class AsyncOpinionsResourceWithRawResponse:
    def __init__(self, opinions: AsyncOpinionsResource) -> None:
        self._opinions = opinions

        self.retrieve = async_to_raw_response_wrapper(
            opinions.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            opinions.list,
        )


class OpinionsResourceWithStreamingResponse:
    def __init__(self, opinions: OpinionsResource) -> None:
        self._opinions = opinions

        self.retrieve = to_streamed_response_wrapper(
            opinions.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            opinions.list,
        )


class AsyncOpinionsResourceWithStreamingResponse:
    def __init__(self, opinions: AsyncOpinionsResource) -> None:
        self._opinions = opinions

        self.retrieve = async_to_streamed_response_wrapper(
            opinions.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            opinions.list,
        )
