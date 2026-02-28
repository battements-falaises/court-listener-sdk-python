# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["Opinion"]


class Opinion(BaseModel):
    id: Optional[int] = None

    author: Optional[str] = None
    """API URL of the authoring judge (normalized)."""

    author_str: Optional[str] = None
    """Author name as a string (not normalized)."""

    cluster: Optional[str] = None
    """API URL of the parent cluster."""

    date_created: Optional[datetime] = None

    date_modified: Optional[datetime] = None

    download_url: Optional[str] = None
    """Original URL where the opinion was scraped from.

    Often unreliable as many courts do not maintain stable URIs.
    """

    extracted_by_ocr: Optional[bool] = None
    """Whether the text was extracted via OCR."""

    html: Optional[str] = None
    """
    HTML content from court websites (Word Perfect or HTML documents) or
    Resource.org.
    """

    html_anon_2020: Optional[str] = None
    """HTML content from the anonymous 2020 source."""

    html_columbia: Optional[str] = None
    """HTML content from the Columbia collaboration."""

    html_lawbox: Optional[str] = None
    """HTML content from the Lawbox donation."""

    html_with_citations: Optional[str] = None
    """
    **Recommended field.** HTML with citations identified and linked. This is the
    field used on the CourtListener website.
    """

    joined_by: Optional[List[str]] = None
    """API URLs of judges who joined this opinion."""

    local_path: Optional[str] = None
    """Path to the binary file for the decision, if available."""

    opinions_cited: Optional[List[str]] = None
    """API URLs of other opinions cited by this one."""

    ordering_key: Optional[float] = None
    """Sort order within the cluster.

    Only populated for opinions ingested from Harvard or Columbia sources.
    """

    per_curiam: Optional[bool] = None
    """Whether this is a per curiam opinion."""

    plain_text: Optional[str] = None
    """Plain text of the opinion.

    Populated when sourced from a court website as PDF or Microsoft Word document.
    """

    resource_uri: Optional[str] = None

    sha1: Optional[str] = None
    """SHA-1 hash of the opinion content."""

    type: Optional[str] = None
    """Opinion type (e.g.

    combined opinion, lead opinion, concurrence, dissent). Values are
    number-prefixed for sort priority.
    """

    xml_harvard: Optional[str] = None
    """XML content from Harvard's Caselaw Access Project.

    Contains rich data but may have OCR artifacts.
    """
