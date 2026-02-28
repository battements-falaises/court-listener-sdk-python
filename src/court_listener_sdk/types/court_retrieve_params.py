# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["CourtRetrieveParams"]


class CourtRetrieveParams(TypedDict, total=False):
    fields: str
    """Comma-separated list of fields to include.

    Supports nested fields via double-underscore notation (e.g. `educations__id`).
    """

    format: Literal["json", "xml", "html"]
    """Response serialization format.

    JSON is default when no `Accept` header is provided.
    """

    omit: str
    """Comma-separated list of fields to exclude.

    Supports nested fields via double-underscore notation.
    """
