import argparse
from pubmed_fetcher.api import fetch_pubmed_ids, fetch_paper_details
from pubmed_fetcher.parser import parse_papers
from pubmed_fetcher.writer import save_to_csv, print_results

def main():
    parser = argparse.ArgumentParser(description="Fetch research papers from PubMed")
    parser.add_argument("query", type=str, help="Search query for PubMed")
    parser.add_argument("-f", "--file", type=str, help="Save results to a CSV file")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode")

    args = parser.parse_args()
    
    if args.debug:
        print("Fetching PubMed IDs...")

    pubmed_ids = fetch_pubmed_ids(args.query)
    xml_data = fetch_paper_details(pubmed_ids)
    papers = parse_papers(xml_data)

    if args.file:
        save_to_csv(papers, args.file)
    else:
        print_results(papers)

if __name__ == "__main__":
    main()
