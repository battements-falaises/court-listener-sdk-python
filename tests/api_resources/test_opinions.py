# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from court_listener_sdk import CourtListener, AsyncCourtListener
from court_listener_sdk.types import Opinion
from court_listener_sdk._utils import parse_datetime
from court_listener_sdk.pagination import SyncCursorURLPage, AsyncCursorURLPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOpinions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: CourtListener) -> None:
        opinion = client.opinions.retrieve(
            id=0,
        )
        assert_matches_type(Opinion, opinion, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: CourtListener) -> None:
        opinion = client.opinions.retrieve(
            id=0,
            fields="fields",
            format="json",
            omit="omit",
        )
        assert_matches_type(Opinion, opinion, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: CourtListener) -> None:
        response = client.opinions.with_raw_response.retrieve(
            id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        opinion = response.parse()
        assert_matches_type(Opinion, opinion, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: CourtListener) -> None:
        with client.opinions.with_streaming_response.retrieve(
            id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            opinion = response.parse()
            assert_matches_type(Opinion, opinion, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: CourtListener) -> None:
        opinion = client.opinions.list()
        assert_matches_type(SyncCursorURLPage[Opinion], opinion, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: CourtListener) -> None:
        opinion = client.opinions.list(
            id=0,
            cited_opinion=0,
            cluster=0,
            cluster_docket_court="cluster__docket__court",
            cluster_docket_docket_number="cluster__docket__docket_number",
            count="on",
            cursor="cursor",
            date_created=parse_datetime("2019-12-27T18:11:19.117Z"),
            date_created_gte=parse_datetime("2019-12-27T18:11:19.117Z"),
            date_created_lte=parse_datetime("2019-12-27T18:11:19.117Z"),
            date_modified=parse_datetime("2019-12-27T18:11:19.117Z"),
            date_modified_gte=parse_datetime("2019-12-27T18:11:19.117Z"),
            date_modified_lte=parse_datetime("2019-12-27T18:11:19.117Z"),
            fields="fields",
            format="json",
            id_gt=0,
            id_gte=0,
            id_lt=0,
            id_lte=0,
            id_range="id__range",
            omit="omit",
            order_by="order_by",
            page=1,
            type="type",
        )
        assert_matches_type(SyncCursorURLPage[Opinion], opinion, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: CourtListener) -> None:
        response = client.opinions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        opinion = response.parse()
        assert_matches_type(SyncCursorURLPage[Opinion], opinion, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: CourtListener) -> None:
        with client.opinions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            opinion = response.parse()
            assert_matches_type(SyncCursorURLPage[Opinion], opinion, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncOpinions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCourtListener) -> None:
        opinion = await async_client.opinions.retrieve(
            id=0,
        )
        assert_matches_type(Opinion, opinion, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncCourtListener) -> None:
        opinion = await async_client.opinions.retrieve(
            id=0,
            fields="fields",
            format="json",
            omit="omit",
        )
        assert_matches_type(Opinion, opinion, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCourtListener) -> None:
        response = await async_client.opinions.with_raw_response.retrieve(
            id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        opinion = await response.parse()
        assert_matches_type(Opinion, opinion, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCourtListener) -> None:
        async with async_client.opinions.with_streaming_response.retrieve(
            id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            opinion = await response.parse()
            assert_matches_type(Opinion, opinion, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncCourtListener) -> None:
        opinion = await async_client.opinions.list()
        assert_matches_type(AsyncCursorURLPage[Opinion], opinion, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCourtListener) -> None:
        opinion = await async_client.opinions.list(
            id=0,
            cited_opinion=0,
            cluster=0,
            cluster_docket_court="cluster__docket__court",
            cluster_docket_docket_number="cluster__docket__docket_number",
            count="on",
            cursor="cursor",
            date_created=parse_datetime("2019-12-27T18:11:19.117Z"),
            date_created_gte=parse_datetime("2019-12-27T18:11:19.117Z"),
            date_created_lte=parse_datetime("2019-12-27T18:11:19.117Z"),
            date_modified=parse_datetime("2019-12-27T18:11:19.117Z"),
            date_modified_gte=parse_datetime("2019-12-27T18:11:19.117Z"),
            date_modified_lte=parse_datetime("2019-12-27T18:11:19.117Z"),
            fields="fields",
            format="json",
            id_gt=0,
            id_gte=0,
            id_lt=0,
            id_lte=0,
            id_range="id__range",
            omit="omit",
            order_by="order_by",
            page=1,
            type="type",
        )
        assert_matches_type(AsyncCursorURLPage[Opinion], opinion, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCourtListener) -> None:
        response = await async_client.opinions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        opinion = await response.parse()
        assert_matches_type(AsyncCursorURLPage[Opinion], opinion, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCourtListener) -> None:
        async with async_client.opinions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            opinion = await response.parse()
            assert_matches_type(AsyncCursorURLPage[Opinion], opinion, path=["response"])

        assert cast(Any, response.is_closed) is True
