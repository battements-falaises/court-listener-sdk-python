# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from court_listener_sdk import CourtListener, AsyncCourtListener
from court_listener_sdk.types import Cluster
from court_listener_sdk._utils import parse_date, parse_datetime
from court_listener_sdk.pagination import SyncCursorURLPage, AsyncCursorURLPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestClusters:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: CourtListener) -> None:
        cluster = client.clusters.retrieve(
            id=0,
        )
        assert_matches_type(Cluster, cluster, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: CourtListener) -> None:
        cluster = client.clusters.retrieve(
            id=0,
            fields="fields",
            format="json",
            omit="omit",
        )
        assert_matches_type(Cluster, cluster, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: CourtListener) -> None:
        response = client.clusters.with_raw_response.retrieve(
            id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cluster = response.parse()
        assert_matches_type(Cluster, cluster, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: CourtListener) -> None:
        with client.clusters.with_streaming_response.retrieve(
            id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cluster = response.parse()
            assert_matches_type(Cluster, cluster, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: CourtListener) -> None:
        cluster = client.clusters.list()
        assert_matches_type(SyncCursorURLPage[Cluster], cluster, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: CourtListener) -> None:
        cluster = client.clusters.list(
            id=0,
            citation="citation",
            count="on",
            cursor="cursor",
            date_created=parse_datetime("2019-12-27T18:11:19.117Z"),
            date_created_gte=parse_datetime("2019-12-27T18:11:19.117Z"),
            date_created_lte=parse_datetime("2019-12-27T18:11:19.117Z"),
            date_filed=parse_date("2019-12-27"),
            date_filed_gte=parse_date("2019-12-27"),
            date_filed_lte=parse_date("2019-12-27"),
            date_modified=parse_datetime("2019-12-27T18:11:19.117Z"),
            date_modified_gte=parse_datetime("2019-12-27T18:11:19.117Z"),
            date_modified_lte=parse_datetime("2019-12-27T18:11:19.117Z"),
            docket=0,
            docket_court="docket__court",
            docket_docket_number="docket__docket_number",
            fields="fields",
            format="json",
            id_gt=0,
            id_gte=0,
            id_lt=0,
            id_lte=0,
            id_range="id__range",
            judges="judges",
            omit="omit",
            order_by="order_by",
            page=1,
        )
        assert_matches_type(SyncCursorURLPage[Cluster], cluster, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: CourtListener) -> None:
        response = client.clusters.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cluster = response.parse()
        assert_matches_type(SyncCursorURLPage[Cluster], cluster, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: CourtListener) -> None:
        with client.clusters.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cluster = response.parse()
            assert_matches_type(SyncCursorURLPage[Cluster], cluster, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncClusters:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCourtListener) -> None:
        cluster = await async_client.clusters.retrieve(
            id=0,
        )
        assert_matches_type(Cluster, cluster, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncCourtListener) -> None:
        cluster = await async_client.clusters.retrieve(
            id=0,
            fields="fields",
            format="json",
            omit="omit",
        )
        assert_matches_type(Cluster, cluster, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCourtListener) -> None:
        response = await async_client.clusters.with_raw_response.retrieve(
            id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cluster = await response.parse()
        assert_matches_type(Cluster, cluster, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCourtListener) -> None:
        async with async_client.clusters.with_streaming_response.retrieve(
            id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cluster = await response.parse()
            assert_matches_type(Cluster, cluster, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncCourtListener) -> None:
        cluster = await async_client.clusters.list()
        assert_matches_type(AsyncCursorURLPage[Cluster], cluster, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCourtListener) -> None:
        cluster = await async_client.clusters.list(
            id=0,
            citation="citation",
            count="on",
            cursor="cursor",
            date_created=parse_datetime("2019-12-27T18:11:19.117Z"),
            date_created_gte=parse_datetime("2019-12-27T18:11:19.117Z"),
            date_created_lte=parse_datetime("2019-12-27T18:11:19.117Z"),
            date_filed=parse_date("2019-12-27"),
            date_filed_gte=parse_date("2019-12-27"),
            date_filed_lte=parse_date("2019-12-27"),
            date_modified=parse_datetime("2019-12-27T18:11:19.117Z"),
            date_modified_gte=parse_datetime("2019-12-27T18:11:19.117Z"),
            date_modified_lte=parse_datetime("2019-12-27T18:11:19.117Z"),
            docket=0,
            docket_court="docket__court",
            docket_docket_number="docket__docket_number",
            fields="fields",
            format="json",
            id_gt=0,
            id_gte=0,
            id_lt=0,
            id_lte=0,
            id_range="id__range",
            judges="judges",
            omit="omit",
            order_by="order_by",
            page=1,
        )
        assert_matches_type(AsyncCursorURLPage[Cluster], cluster, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCourtListener) -> None:
        response = await async_client.clusters.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        cluster = await response.parse()
        assert_matches_type(AsyncCursorURLPage[Cluster], cluster, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCourtListener) -> None:
        async with async_client.clusters.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            cluster = await response.parse()
            assert_matches_type(AsyncCursorURLPage[Cluster], cluster, path=["response"])

        assert cast(Any, response.is_closed) is True
