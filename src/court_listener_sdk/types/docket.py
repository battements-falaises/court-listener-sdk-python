# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import date, datetime

from .._models import BaseModel

__all__ = ["Docket"]


class Docket(BaseModel):
    id: Optional[int] = None

    absolute_url: Optional[str] = None
    """Relative URL path on CourtListener."""

    appeal_from: Optional[str] = None
    """API URL of the court this case was appealed from."""

    appeal_from_str: Optional[str] = None

    appellate_case_type_information: Optional[str] = None

    appellate_fee_status: Optional[str] = None

    assigned_to: Optional[str] = None
    """API URL of the assigned judge."""

    assigned_to_str: Optional[str] = None
    """Name of the assigned judge (string, not normalized)."""

    audio_files: Optional[List[str]] = None
    """API URLs of related oral argument audio files."""

    bankruptcy_information: Optional[Dict[str, object]] = None
    """Bankruptcy-specific information, if applicable."""

    blocked: Optional[bool] = None

    case_name: Optional[str] = None
    """Current case name.

    May change over time (e.g. if a named party changes). See also the cluster's
    case_name which is frozen at decision time.
    """

    case_name_full: Optional[str] = None

    case_name_short: Optional[str] = None

    cause: Optional[str] = None

    clusters: Optional[List[str]] = None
    """API URLs of related opinion clusters."""

    court: Optional[str] = None
    """API URL of the court."""

    court_id: Optional[str] = None
    """Court identifier string."""

    date_argued: Optional[date] = None

    date_blocked: Optional[date] = None

    date_cert_denied: Optional[date] = None

    date_cert_granted: Optional[date] = None

    date_created: Optional[datetime] = None

    date_filed: Optional[date] = None

    date_last_filing: Optional[date] = None

    date_last_index: Optional[datetime] = None

    date_modified: Optional[datetime] = None

    date_reargued: Optional[date] = None

    date_reargument_denied: Optional[date] = None

    date_terminated: Optional[date] = None

    docket_number: Optional[str] = None
    """The docket number assigned by the court."""

    docket_number_core: Optional[str] = None
    """Normalized core docket number."""

    filepath_ia: Optional[str] = None
    """URL to the Internet Archive docket file."""

    filepath_ia_json: Optional[str] = None
    """URL to the Internet Archive JSON docket file."""

    ia_date_first_change: Optional[datetime] = None

    ia_needs_upload: Optional[bool] = None

    ia_upload_failure_count: Optional[int] = None

    idb_data: Optional[Dict[str, object]] = None
    """Integrated database data, if available."""

    jurisdiction_type: Optional[str] = None

    jury_demand: Optional[str] = None

    mdl_status: Optional[str] = None

    nature_of_suit: Optional[str] = None

    original_court_info: Optional[Dict[str, object]] = None
    """Original court information, if available."""

    pacer_case_id: Optional[str] = None

    panel: Optional[List[str]] = None
    """API URLs of judges on the panel."""

    panel_str: Optional[str] = None

    referred_to: Optional[str] = None
    """API URL of the referred judge."""

    referred_to_str: Optional[str] = None

    resource_uri: Optional[str] = None

    slug: Optional[str] = None

    source: Optional[int] = None
    """Numeric source identifier."""

    tags: Optional[List[str]] = None
    """API URLs of tags on this docket."""
