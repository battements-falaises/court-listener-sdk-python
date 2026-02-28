# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from court_listener_sdk import CourtListener, AsyncCourtListener
from court_listener_sdk.types import Court
from court_listener_sdk._utils import parse_datetime
from court_listener_sdk.pagination import SyncCursorURLPage, AsyncCursorURLPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCourts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: CourtListener) -> None:
        court = client.courts.retrieve(
            id="id",
        )
        assert_matches_type(Court, court, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: CourtListener) -> None:
        court = client.courts.retrieve(
            id="id",
            fields="fields",
            format="json",
            omit="omit",
        )
        assert_matches_type(Court, court, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: CourtListener) -> None:
        response = client.courts.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        court = response.parse()
        assert_matches_type(Court, court, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: CourtListener) -> None:
        with client.courts.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            court = response.parse()
            assert_matches_type(Court, court, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: CourtListener) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.courts.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    def test_method_list(self, client: CourtListener) -> None:
        court = client.courts.list()
        assert_matches_type(SyncCursorURLPage[Court], court, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: CourtListener) -> None:
        court = client.courts.list(
            id="id",
            count="on",
            cursor="cursor",
            date_modified=parse_datetime("2019-12-27T18:11:19.117Z"),
            date_modified_gte=parse_datetime("2019-12-27T18:11:19.117Z"),
            date_modified_lte=parse_datetime("2019-12-27T18:11:19.117Z"),
            fields="fields",
            format="json",
            full_name="full_name",
            full_name_startswith="full_name__startswith",
            id_in="id__in",
            jurisdiction="jurisdiction",
            omit="omit",
            order_by="order_by",
            page=1,
        )
        assert_matches_type(SyncCursorURLPage[Court], court, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: CourtListener) -> None:
        response = client.courts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        court = response.parse()
        assert_matches_type(SyncCursorURLPage[Court], court, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: CourtListener) -> None:
        with client.courts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            court = response.parse()
            assert_matches_type(SyncCursorURLPage[Court], court, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCourts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCourtListener) -> None:
        court = await async_client.courts.retrieve(
            id="id",
        )
        assert_matches_type(Court, court, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncCourtListener) -> None:
        court = await async_client.courts.retrieve(
            id="id",
            fields="fields",
            format="json",
            omit="omit",
        )
        assert_matches_type(Court, court, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCourtListener) -> None:
        response = await async_client.courts.with_raw_response.retrieve(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        court = await response.parse()
        assert_matches_type(Court, court, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCourtListener) -> None:
        async with async_client.courts.with_streaming_response.retrieve(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            court = await response.parse()
            assert_matches_type(Court, court, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncCourtListener) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.courts.with_raw_response.retrieve(
                id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCourtListener) -> None:
        court = await async_client.courts.list()
        assert_matches_type(AsyncCursorURLPage[Court], court, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCourtListener) -> None:
        court = await async_client.courts.list(
            id="id",
            count="on",
            cursor="cursor",
            date_modified=parse_datetime("2019-12-27T18:11:19.117Z"),
            date_modified_gte=parse_datetime("2019-12-27T18:11:19.117Z"),
            date_modified_lte=parse_datetime("2019-12-27T18:11:19.117Z"),
            fields="fields",
            format="json",
            full_name="full_name",
            full_name_startswith="full_name__startswith",
            id_in="id__in",
            jurisdiction="jurisdiction",
            omit="omit",
            order_by="order_by",
            page=1,
        )
        assert_matches_type(AsyncCursorURLPage[Court], court, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCourtListener) -> None:
        response = await async_client.courts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        court = await response.parse()
        assert_matches_type(AsyncCursorURLPage[Court], court, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCourtListener) -> None:
        async with async_client.courts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            court = await response.parse()
            assert_matches_type(AsyncCursorURLPage[Court], court, path=["response"])

        assert cast(Any, response.is_closed) is True
