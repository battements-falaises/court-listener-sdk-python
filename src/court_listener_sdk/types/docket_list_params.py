# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date, datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["DocketListParams"]


class DocketListParams(TypedDict, total=False):
    id: int
    """Filter by docket ID (exact)."""

    blocked: bool
    """Filter for blocked/unblocked dockets."""

    case_name: str
    """Filter by case name."""

    cause: str
    """Filter by cause."""

    count: Literal["on"]
    """Set to `on` to return only the total count of matching items without result
    data.

    When enabled, pagination parameters are ignored.
    """

    court: str
    """Filter by court identifier (e.g.

    `scotus`). Supports related court filters via `court__` prefix.
    """

    query_court_jurisdiction_1: Annotated[str, PropertyInfo(alias="court__jurisdiction")]
    """Filter by the court's jurisdiction type (e.g. `F`, `FD`, `S`)."""

    query_court_jurisdiction_2: Annotated[str, PropertyInfo(alias="court__jurisdiction!")]
    """Exclude dockets from this jurisdiction type."""

    cursor: str
    """Cursor token for deep pagination.

    Returned in the `next` / `previous` fields of paginated responses. Available
    when ordering by `id`, `date_modified`, or `date_created`.
    """

    date_created: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filter by exact creation date."""

    date_created_gte: Annotated[Union[str, datetime], PropertyInfo(alias="date_created__gte", format="iso8601")]
    """Created on or after this date."""

    date_created_lte: Annotated[Union[str, datetime], PropertyInfo(alias="date_created__lte", format="iso8601")]
    """Created on or before this date."""

    date_filed: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """Filter by filing date."""

    date_filed_gte: Annotated[Union[str, date], PropertyInfo(alias="date_filed__gte", format="iso8601")]
    """Filed on or after this date."""

    date_filed_lte: Annotated[Union[str, date], PropertyInfo(alias="date_filed__lte", format="iso8601")]
    """Filed on or before this date."""

    date_modified: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filter by exact modification date."""

    date_modified_gte: Annotated[Union[str, datetime], PropertyInfo(alias="date_modified__gte", format="iso8601")]
    """Modified on or after this date."""

    date_modified_lte: Annotated[Union[str, datetime], PropertyInfo(alias="date_modified__lte", format="iso8601")]
    """Modified on or before this date."""

    date_terminated: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """Filter by termination date."""

    date_terminated_gte: Annotated[Union[str, date], PropertyInfo(alias="date_terminated__gte", format="iso8601")]

    date_terminated_lte: Annotated[Union[str, date], PropertyInfo(alias="date_terminated__lte", format="iso8601")]

    docket_number: str
    """Filter by exact docket number (e.g. `23A994`)."""

    fields: str
    """Comma-separated list of fields to include.

    Supports nested fields via double-underscore notation (e.g. `educations__id`).
    """

    format: Literal["json", "xml", "html"]
    """Response serialization format.

    JSON is default when no `Accept` header is provided.
    """

    id_gt: Annotated[int, PropertyInfo(alias="id__gt")]
    """Docket IDs greater than this value."""

    id_gte: Annotated[int, PropertyInfo(alias="id__gte")]
    """Docket IDs greater than or equal to this value."""

    id_lt: Annotated[int, PropertyInfo(alias="id__lt")]
    """Docket IDs less than this value."""

    id_lte: Annotated[int, PropertyInfo(alias="id__lte")]
    """Docket IDs less than or equal to this value."""

    id_range: Annotated[str, PropertyInfo(alias="id__range")]
    """Docket IDs within an inclusive range (e.g. `500,1000`)."""

    nature_of_suit: str
    """Filter by nature of suit."""

    omit: str
    """Comma-separated list of fields to exclude.

    Supports nested fields via double-underscore notation.
    """

    order_by: str
    """Comma-separated list of fields to order by.

    Prefix with `-` for descending order. Use a secondary field as a tie-breaker for
    deterministic ordering (e.g. `date_filed,id`).
    """

    page: int
    """Page number for standard pagination (limited to 100 pages)."""

    source: int
    """Filter by docket source."""
