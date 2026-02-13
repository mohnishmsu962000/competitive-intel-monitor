from typing import TypedDict

class State(TypedDict):
    company_name: str
    competitors: list[str]
    research_queries: dict[str, list[str]]  
    search_results: dict[str, list[dict]]  
    urls_to_scrape: dict[str, list[str]] 
    scraped_content: dict[str, dict[str, str]] 
    competitors_report: dict[str, str]  
    competitors_summaries: dict[str, str]  
    industry_trend_report: str