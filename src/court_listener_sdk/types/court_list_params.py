# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CourtListParams"]


class CourtListParams(TypedDict, total=False):
    id: str
    """Filter by court identifier (e.g. `scotus`, `ca9`, `dcd`)."""

    count: Literal["on"]
    """Set to `on` to return only the total count of matching items without result
    data.

    When enabled, pagination parameters are ignored.
    """

    cursor: str
    """Cursor token for deep pagination.

    Returned in the `next` / `previous` fields of paginated responses. Available
    when ordering by `id`, `date_modified`, or `date_created`.
    """

    date_modified: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Filter by exact date modified (ISO-8601)."""

    date_modified_gte: Annotated[Union[str, datetime], PropertyInfo(alias="date_modified__gte", format="iso8601")]
    """Filter courts modified on or after this date."""

    date_modified_lte: Annotated[Union[str, datetime], PropertyInfo(alias="date_modified__lte", format="iso8601")]
    """Filter courts modified on or before this date."""

    fields: str
    """Comma-separated list of fields to include.

    Supports nested fields via double-underscore notation (e.g. `educations__id`).
    """

    format: Literal["json", "xml", "html"]
    """Response serialization format.

    JSON is default when no `Accept` header is provided.
    """

    full_name: str
    """Filter by the full name of the court."""

    full_name_startswith: Annotated[str, PropertyInfo(alias="full_name__startswith")]
    """Filter courts whose full name starts with the given value."""

    id_in: Annotated[str, PropertyInfo(alias="id__in")]
    """Filter by multiple court identifiers (comma-separated)."""

    jurisdiction: str
    """Filter by jurisdiction type.

    Common values: `F` (Federal Appellate), `FD` (Federal District), `FB` (Federal
    Bankruptcy), `FBP` (Federal Bankruptcy Panel), `FS` (Federal Special), `S`
    (State Supreme), `SA` (State Appellate), `ST` (State Trial), `SS` (State
    Special), `SAG` (State Attorney General), `T` (Tribal), `I` (International), `C`
    (Committee), `TES` (Testing).
    """

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
