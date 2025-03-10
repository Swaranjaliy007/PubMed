from pubmed_fetcher.api import fetch_pubmed_ids, fetch_paper_details
from pubmed_fetcher.parser import parse_papers
from pubmed_fetcher.writer import save_to_csv, print_results

query = "cancer therapy"
pubmed_ids = fetch_pubmed_ids(query)
xml_data = fetch_paper_details(pubmed_ids)
papers = parse_papers(xml_data)

print_results(papers)
save_to_csv(papers, "papers.csv")
