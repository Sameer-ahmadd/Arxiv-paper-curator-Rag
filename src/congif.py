from typing import List

from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


# Default settings for the project
class DefaultSetting(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", extra="ignore", frozen=True, env_nested_delimiter="__"
    )


class ArxivSettings(DefaultSetting):
    """arXiv api client Settings"""

    base_url: str = "https://export.arxiv.org/api/query"
    namespaces: dict = Field(
        default={
            "atom": "http://www.w3.org/2005/Atom",
            "opensearch": "http://a9.com/-/spec/opensearch/1.1/",
            "arxiv": "http://arxiv.org/schemas/atom",
        }
    )
    pdf_cache_dir: str = "./data/arxiv_pdfs"
    rate_limt_delay: float = 3.0  # delay between requests to avoid rate limiting
    timeout_seconds: int = 30
    max_results: int = 100
    search_category: str = "cs.AI"  # default category to search.
