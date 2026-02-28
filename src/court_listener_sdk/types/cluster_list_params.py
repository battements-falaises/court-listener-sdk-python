# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date, datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ClusterListParams"]


class ClusterListParams(TypedDict, total=False):
    id: int
    """Filter by cluster ID."""

    citation: str
    """Filter by citation."""

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

    date_filed: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """Filter by the date the cluster was filed."""

    date_filed_gte: Annotated[Union[str, date], PropertyInfo(alias="date_filed__gte", format="iso8601")]

    date_filed_lte: Annotated[Union[str, date], PropertyInfo(alias="date_filed__lte", format="iso8601")]

    date_modified: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    date_modified_gte: Annotated[Union[str, datetime], PropertyInfo(alias="date_modified__gte", format="iso8601")]

    date_modified_lte: Annotated[Union[str, datetime], PropertyInfo(alias="date_modified__lte", format="iso8601")]

    docket: int
    """Filter by parent docket ID."""

    docket_court: Annotated[str, PropertyInfo(alias="docket__court")]
    """Filter by the court of the parent docket (e.g. `scotus`)."""

    docket_docket_number: Annotated[str, PropertyInfo(alias="docket__docket_number")]
    """Filter by the docket number of the parent docket."""

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
    """Inclusive range (e.g. `100,500`)."""

    judges: str
    """Filter by judge name string."""

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
