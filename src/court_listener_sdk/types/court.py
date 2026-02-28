# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date, datetime

from .._models import BaseModel

__all__ = ["Court"]


class Court(BaseModel):
    id: Optional[str] = None
    """Court identifier (e.g. `scotus`, `ca9`, `dcd`)."""

    citation_string: Optional[str] = None
    """String used for citations from this court."""

    date_created: Optional[datetime] = None

    date_modified: Optional[datetime] = None

    end_date: Optional[date] = None
    """Date the court was dissolved, if applicable."""

    full_name: Optional[str] = None
    """Full name of the court."""

    in_use: Optional[bool] = None
    """Whether this court is currently active."""

    jurisdiction: Optional[str] = None
    """Jurisdiction type code."""

    position: Optional[float] = None
    """Sort position for display."""

    resource_uri: Optional[str] = None
    """Canonical API URL for this court."""

    short_name: Optional[str] = None
    """Short/abbreviated name."""

    start_date: Optional[date] = None
    """Date the court was founded."""

    url: Optional[str] = None
    """Court's website URL."""
