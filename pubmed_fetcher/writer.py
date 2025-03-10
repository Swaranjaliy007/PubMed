import pandas as pd
from typing import List, Dict

def save_to_csv(papers: List[Dict], filename: str):
    """Save extracted paper details to a CSV file."""
    df = pd.DataFrame(papers)
    df.to_csv(filename, index=False)
    print(f"Results saved to {filename}")

def print_results(papers: List[Dict]):
    """Print results to the console."""
    for paper in papers:
        print(f"Pubmed ID: {paper['PubmedID']}")
        print(f"Title: {paper['Title']}")
        print(f"Publication Date: {paper['Publication Date']}")
        print(f"Non-academic Author(s): {paper['Non-academic Author(s)']}")
        print(f"Company Affiliation(s): {paper['Company Affiliation(s)']}")
        print(f"Corresponding Author Email: {paper['Corresponding Author Email']}")
        print("-" * 50)
