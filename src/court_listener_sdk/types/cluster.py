# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date, datetime

from .._models import BaseModel

__all__ = ["Cluster", "Citation"]


class Citation(BaseModel):
    """A parallel citation for an opinion cluster."""

    page: Optional[str] = None
    """The starting page number in the reporter."""

    reporter: Optional[str] = None
    """The reporter abbreviation (e.g. "U.S.", "S. Ct.")."""

    type: Optional[int] = None
    """The citation type identifier."""

    volume: Optional[int] = None
    """The volume number of the reporter."""


class Cluster(BaseModel):
    id: Optional[int] = None
    """Cluster ID — used in CourtListener case law URLs."""

    absolute_url: Optional[str] = None
    """Relative URL path on CourtListener."""

    blocked: Optional[bool] = None

    case_name: Optional[str] = None
    """Case name frozen at decision time (does not change)."""

    case_name_full: Optional[str] = None

    case_name_short: Optional[str] = None

    citation_count: Optional[int] = None
    """Number of times this cluster has been cited."""

    citations: Optional[List[Citation]] = None
    """List of parallel citation objects for this cluster."""

    correction: Optional[str] = None

    cross_reference: Optional[str] = None

    date_blocked: Optional[date] = None

    date_created: Optional[datetime] = None

    date_filed: Optional[date] = None

    date_filed_is_approximate: Optional[bool] = None

    date_modified: Optional[datetime] = None

    disposition: Optional[str] = None

    docket: Optional[str] = None
    """API URL of the parent docket."""

    headnotes: Optional[str] = None

    history: Optional[str] = None

    judges: Optional[str] = None
    """Judge name(s) as a string (not yet normalized)."""

    non_participating_judges: Optional[List[str]] = None
    """API URLs of non-participating judges."""

    other_dates: Optional[str] = None

    panel: Optional[List[str]] = None
    """API URLs of judges on the panel (normalized)."""

    precedential_status: Optional[str] = None
    """Whether this cluster is published, unpublished, etc."""

    resource_uri: Optional[str] = None

    slug: Optional[str] = None

    source: Optional[str] = None
    """Source of this cluster data."""

    sub_opinions: Optional[List[str]] = None
    """API URLs of opinions in this cluster."""

    summary: Optional[str] = None

    syllabus: Optional[str] = None
