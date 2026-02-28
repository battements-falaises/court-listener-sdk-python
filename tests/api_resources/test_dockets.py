# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from court_listener_sdk import CourtListener, AsyncCourtListener
from court_listener_sdk.types import Docket
from court_listener_sdk._utils import parse_date, parse_datetime
from court_listener_sdk.pagination import SyncCursorURLPage, AsyncCursorURLPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDockets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: CourtListener) -> None:
        docket = client.dockets.retrieve(
            id=0,
        )
        assert_matches_type(Docket, docket, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: CourtListener) -> None:
        docket = client.dockets.retrieve(
            id=0,
            fields="fields",
            format="json",
            omit="omit",
        )
        assert_matches_type(Docket, docket, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: CourtListener) -> None:
        response = client.dockets.with_raw_response.retrieve(
            id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        docket = response.parse()
        assert_matches_type(Docket, docket, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: CourtListener) -> None:
        with client.dockets.with_streaming_response.retrieve(
            id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            docket = response.parse()
            assert_matches_type(Docket, docket, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: CourtListener) -> None:
        docket = client.dockets.list()
        assert_matches_type(SyncCursorURLPage[Docket], docket, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: CourtListener) -> None:
        docket = client.dockets.list(
            id=0,
            blocked=True,
            case_name="case_name",
            cause="cause",
            count="on",
            court="court",
            query_court_jurisdiction_1="court__jurisdiction",
            query_court_jurisdiction_2="court__jurisdiction!",
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
            date_terminated=parse_date("2019-12-27"),
            date_terminated_gte=parse_date("2019-12-27"),
            date_terminated_lte=parse_date("2019-12-27"),
            docket_number="docket_number",
            fields="fields",
            format="json",
            id_gt=0,
            id_gte=0,
            id_lt=0,
            id_lte=0,
            id_range="id__range",
            nature_of_suit="nature_of_suit",
            omit="omit",
            order_by="order_by",
            page=1,
            source=0,
        )
        assert_matches_type(SyncCursorURLPage[Docket], docket, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: CourtListener) -> None:
        response = client.dockets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        docket = response.parse()
        assert_matches_type(SyncCursorURLPage[Docket], docket, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: CourtListener) -> None:
        with client.dockets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            docket = response.parse()
            assert_matches_type(SyncCursorURLPage[Docket], docket, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDockets:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCourtListener) -> None:
        docket = await async_client.dockets.retrieve(
            id=0,
        )
        assert_matches_type(Docket, docket, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncCourtListener) -> None:
        docket = await async_client.dockets.retrieve(
            id=0,
            fields="fields",
            format="json",
            omit="omit",
        )
        assert_matches_type(Docket, docket, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCourtListener) -> None:
        response = await async_client.dockets.with_raw_response.retrieve(
            id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        docket = await response.parse()
        assert_matches_type(Docket, docket, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCourtListener) -> None:
        async with async_client.dockets.with_streaming_response.retrieve(
            id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            docket = await response.parse()
            assert_matches_type(Docket, docket, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncCourtListener) -> None:
        docket = await async_client.dockets.list()
        assert_matches_type(AsyncCursorURLPage[Docket], docket, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCourtListener) -> None:
        docket = await async_client.dockets.list(
            id=0,
            blocked=True,
            case_name="case_name",
            cause="cause",
            count="on",
            court="court",
            query_court_jurisdiction_1="court__jurisdiction",
            query_court_jurisdiction_2="court__jurisdiction!",
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
            date_terminated=parse_date("2019-12-27"),
            date_terminated_gte=parse_date("2019-12-27"),
            date_terminated_lte=parse_date("2019-12-27"),
            docket_number="docket_number",
            fields="fields",
            format="json",
            id_gt=0,
            id_gte=0,
            id_lt=0,
            id_lte=0,
            id_range="id__range",
            nature_of_suit="nature_of_suit",
            omit="omit",
            order_by="order_by",
            page=1,
            source=0,
        )
        assert_matches_type(AsyncCursorURLPage[Docket], docket, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCourtListener) -> None:
        response = await async_client.dockets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        docket = await response.parse()
        assert_matches_type(AsyncCursorURLPage[Docket], docket, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCourtListener) -> None:
        async with async_client.dockets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            docket = await response.parse()
            assert_matches_type(AsyncCursorURLPage[Docket], docket, path=["response"])

        assert cast(Any, response.is_closed) is True
