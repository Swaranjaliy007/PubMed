import requests
from typing import List

BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
DETAILS_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"

def fetch_pubmed_ids(query: str) -> List[str]:
    """Fetch PubMed IDs for the given query."""
    params = {
        "db": "pubmed",
        "term": query,
        "retmax": 50,
        "retmode": "json"
    }
    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()
    data = response.json()
    return data.get("esearchresult", {}).get("idlist", [])

def fetch_paper_details(pubmed_ids: List[str]) -> str:
    """Fetch detailed PubMed articles using their IDs."""
    if not pubmed_ids:
        return ""
    
    params = {
        "db": "pubmed",
        "id": ",".join(pubmed_ids),
        "retmode": "xml"
    }
    response = requests.get(DETAILS_URL, params=params)
    response.raise_for_status()
    return response.text
