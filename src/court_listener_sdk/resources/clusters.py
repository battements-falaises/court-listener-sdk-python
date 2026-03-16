# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date, datetime
from typing_extensions import Literal

import httpx

from ..types import cluster_list_params, cluster_retrieve_params
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
from ..types.cluster import Cluster

__all__ = ["ClustersResource", "AsyncClustersResource"]


class ClustersResource(SyncAPIResource):
    """Opinion clusters grouping related decisions from a single hearing."""

    @cached_property
    def with_raw_response(self) -> ClustersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/battements-falaises/court-listener-sdk-python#accessing-raw-response-data-eg-headers
        """
        return ClustersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ClustersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/battements-falaises/court-listener-sdk-python#with_streaming_response
        """
        return ClustersResourceWithStreamingResponse(self)

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
    ) -> Cluster:
        """Look up a cluster by its ID.

        The cluster ID matches the ID used in CourtListener
        case law URLs (e.g. `/opinion/2812209/obergefell-v-hodges/` corresponds to
        cluster ID `2812209`).

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
            f"/clusters/{id}/",
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
                    cluster_retrieve_params.ClusterRetrieveParams,
                ),
            ),
            cast_to=Cluster,
        )

    def list(
        self,
        *,
        id: int | Omit = omit,
        citation: str | Omit = omit,
        count: Literal["on"] | Omit = omit,
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
        docket: int | Omit = omit,
        docket_court: str | Omit = omit,
        docket_docket_number: str | Omit = omit,
        fields: str | Omit = omit,
        format: Literal["json", "xml", "html"] | Omit = omit,
        id_gt: int | Omit = omit,
        id_gte: int | Omit = omit,
        id_lt: int | Omit = omit,
        id_lte: int | Omit = omit,
        id_range: str | Omit = omit,
        judges: str | Omit = omit,
        omit: str | Omit = omit,
        order_by: str | Omit = omit,
        page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorURLPage[Cluster]:
        """Returns a paginated list of opinion clusters.

        Each cluster groups together
        opinions from the same panel hearing (e.g. majority, dissent, concurrence). The
        cluster `id` is used in CourtListener case law URLs.

        Args:
          id: Filter by cluster ID.

          citation: Filter by citation.

          count: Set to `on` to return only the total count of matching items without result
              data. When enabled, pagination parameters are ignored.

          cursor: Cursor token for deep pagination. Returned in the `next` / `previous` fields of
              paginated responses. Available when ordering by `id`, `date_modified`, or
              `date_created`.

          date_filed: Filter by the date the cluster was filed.

          docket: Filter by parent docket ID.

          docket_court: Filter by the court of the parent docket (e.g. `scotus`).

          docket_docket_number: Filter by the docket number of the parent docket.

          fields: Comma-separated list of fields to include. Supports nested fields via
              double-underscore notation (e.g. `educations__id`).

          format: Response serialization format. JSON is default when no `Accept` header is
              provided.

          id_range: Inclusive range (e.g. `100,500`).

          judges: Filter by judge name string.

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
            "/clusters/",
            page=SyncCursorURLPage[Cluster],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "citation": citation,
                        "count": count,
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
                        "docket": docket,
                        "docket_court": docket_court,
                        "docket_docket_number": docket_docket_number,
                        "fields": fields,
                        "format": format,
                        "id_gt": id_gt,
                        "id_gte": id_gte,
                        "id_lt": id_lt,
                        "id_lte": id_lte,
                        "id_range": id_range,
                        "judges": judges,
                        "omit": omit,
                        "order_by": order_by,
                        "page": page,
                    },
                    cluster_list_params.ClusterListParams,
                ),
            ),
            model=Cluster,
        )


class AsyncClustersResource(AsyncAPIResource):
    """Opinion clusters grouping related decisions from a single hearing."""

    @cached_property
    def with_raw_response(self) -> AsyncClustersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/battements-falaises/court-listener-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncClustersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncClustersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/battements-falaises/court-listener-sdk-python#with_streaming_response
        """
        return AsyncClustersResourceWithStreamingResponse(self)

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
    ) -> Cluster:
        """Look up a cluster by its ID.

        The cluster ID matches the ID used in CourtListener
        case law URLs (e.g. `/opinion/2812209/obergefell-v-hodges/` corresponds to
        cluster ID `2812209`).

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
            f"/clusters/{id}/",
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
                    cluster_retrieve_params.ClusterRetrieveParams,
                ),
            ),
            cast_to=Cluster,
        )

    def list(
        self,
        *,
        id: int | Omit = omit,
        citation: str | Omit = omit,
        count: Literal["on"] | Omit = omit,
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
        docket: int | Omit = omit,
        docket_court: str | Omit = omit,
        docket_docket_number: str | Omit = omit,
        fields: str | Omit = omit,
        format: Literal["json", "xml", "html"] | Omit = omit,
        id_gt: int | Omit = omit,
        id_gte: int | Omit = omit,
        id_lt: int | Omit = omit,
        id_lte: int | Omit = omit,
        id_range: str | Omit = omit,
        judges: str | Omit = omit,
        omit: str | Omit = omit,
        order_by: str | Omit = omit,
        page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Cluster, AsyncCursorURLPage[Cluster]]:
        """Returns a paginated list of opinion clusters.

        Each cluster groups together
        opinions from the same panel hearing (e.g. majority, dissent, concurrence). The
        cluster `id` is used in CourtListener case law URLs.

        Args:
          id: Filter by cluster ID.

          citation: Filter by citation.

          count: Set to `on` to return only the total count of matching items without result
              data. When enabled, pagination parameters are ignored.

          cursor: Cursor token for deep pagination. Returned in the `next` / `previous` fields of
              paginated responses. Available when ordering by `id`, `date_modified`, or
              `date_created`.

          date_filed: Filter by the date the cluster was filed.

          docket: Filter by parent docket ID.

          docket_court: Filter by the court of the parent docket (e.g. `scotus`).

          docket_docket_number: Filter by the docket number of the parent docket.

          fields: Comma-separated list of fields to include. Supports nested fields via
              double-underscore notation (e.g. `educations__id`).

          format: Response serialization format. JSON is default when no `Accept` header is
              provided.

          id_range: Inclusive range (e.g. `100,500`).

          judges: Filter by judge name string.

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
            "/clusters/",
            page=AsyncCursorURLPage[Cluster],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "citation": citation,
                        "count": count,
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
                        "docket": docket,
                        "docket_court": docket_court,
                        "docket_docket_number": docket_docket_number,
                        "fields": fields,
                        "format": format,
                        "id_gt": id_gt,
                        "id_gte": id_gte,
                        "id_lt": id_lt,
                        "id_lte": id_lte,
                        "id_range": id_range,
                        "judges": judges,
                        "omit": omit,
                        "order_by": order_by,
                        "page": page,
                    },
                    cluster_list_params.ClusterListParams,
                ),
            ),
            model=Cluster,
        )


class ClustersResourceWithRawResponse:
    def __init__(self, clusters: ClustersResource) -> None:
        self._clusters = clusters

        self.retrieve = to_raw_response_wrapper(
            clusters.retrieve,
        )
        self.list = to_raw_response_wrapper(
            clusters.list,
        )


class AsyncClustersResourceWithRawResponse:
    def __init__(self, clusters: AsyncClustersResource) -> None:
        self._clusters = clusters

        self.retrieve = async_to_raw_response_wrapper(
            clusters.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            clusters.list,
        )


class ClustersResourceWithStreamingResponse:
    def __init__(self, clusters: ClustersResource) -> None:
        self._clusters = clusters

        self.retrieve = to_streamed_response_wrapper(
            clusters.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            clusters.list,
        )


class AsyncClustersResourceWithStreamingResponse:
    def __init__(self, clusters: AsyncClustersResource) -> None:
        self._clusters = clusters

        self.retrieve = async_to_streamed_response_wrapper(
            clusters.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            clusters.list,
        )
