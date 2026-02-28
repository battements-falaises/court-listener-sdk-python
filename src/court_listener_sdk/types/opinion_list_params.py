# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["OpinionListParams"]


class OpinionListParams(TypedDict, total=False):
    id: int
    """Filter by opinion ID."""

    cited_opinion: int
    """Filter opinions that cite this opinion ID."""

    cluster: int
    """Filter by parent cluster ID."""

    cluster_docket_court: Annotated[str, PropertyInfo(alias="cluster__docket__court")]
    """Filter by court via the cluster's docket (e.g. `scotus`)."""

    cluster_docket_docket_number: Annotated[str, PropertyInfo(alias="cluster__docket__docket_number")]
    """Filter by docket number via the cluster's docket."""

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

    date_created: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    date_created_gte: Annotated[Union[str, datetime], PropertyInfo(alias="date_created__gte", format="iso8601")]

    date_created_lte: Annotated[Union[str, datetime], PropertyInfo(alias="date_created__lte", format="iso8601")]

    date_modified: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    date_modified_gte: Annotated[Union[str, datetime], PropertyInfo(alias="date_modified__gte", format="iso8601")]

    date_modified_lte: Annotated[Union[str, datetime], PropertyInfo(alias="date_modified__lte", format="iso8601")]

    fields: str
    """Comma-separated list of fields to include.

    Supports nested fields via double-underscore notation (e.g. `educations__id`).
    """

    format: Literal["json", "xml", "html"]
    """Response serialization format.

    JSON is default when no `Accept` header is provided.
    """

    id_gt: Annotated[int, PropertyInfo(alias="id__gt")]

    id_gte: Annotated[int, PropertyInfo(alias="id__gte")]

    id_lt: Annotated[int, PropertyInfo(alias="id__lt")]

    id_lte: Annotated[int, PropertyInfo(alias="id__lte")]

    id_range: Annotated[str, PropertyInfo(alias="id__range")]

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

    type: str
    """Filter by opinion type.

    Values are prefixed with numbers for sort order. Common types include combined
    opinion, lead opinion, concurrence, dissent, etc.
    """
